#!/usr/bin/env python3
"""Admit source-backed Markdown and freeze independently checkable cold revisions.

Identity patterns adapted from P4 verify_baseline/verify_brain. No legacy runtime
 dependency. Review receipts record operator decisions, not proof of authorship.
"""
from __future__ import annotations

import argparse
import ctypes
import hashlib
import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile
import uuid
from pathlib import Path

DN = {f'DN-{i:03}' for i in range(1, 41)}
KB = r'KB-[0-9]{3}'
SECTIONS = ['Claim', 'Limits and conflicts', 'Evidence', 'Related']


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def strict(text):
    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, f'duplicate JSON field: {key}')
            out[key] = value
        return out
    return json.loads(text, object_pairs_hook=pairs, parse_constant=lambda x: require(False, f'invalid JSON constant {x}'))


def fields(value, keys):
    require(isinstance(value, dict) and set(value) == set(keys), f'expected fields {sorted(keys)}')


def safe(path):
    path = Path(path).expanduser().absolute()
    require('..' not in path.parts, f'parent traversal is not allowed: {path}')
    for part in [*reversed(path.parents), path]:
        require(not part.is_symlink() and not part.is_junction(), f'link/junction is not allowed: {part}')
        if part.parent.is_dir():
            folded = part.name.casefold()
            matches = [name for name in os.listdir(part.parent) if name.casefold() == folded]
            require(not matches or matches == [part.name], f'case collision or incorrect case: {part}')
    return path.resolve()


def raw(path):
    path = safe(path)
    require(path.is_file(), f'missing regular file: {path}')
    return path.read_bytes()


def text(path):
    return raw(path).decode('utf-8').replace('\r\n', '\n')


def load(path):
    return strict(text(path))


def absent(path):
    path = safe(path)
    require(not path.exists(), f'attempt already exists: {path}')
    return path


def write_new(path, data):
    path = absent(path)
    safe(path.parent).mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)


def save(path, value):
    write_new(path, canonical(value) + b'\n')


def publish_directory(source, destination):
    """Atomic rename with kernel-enforced refusal of an existing destination."""
    absent(destination)
    if os.name == 'nt':
        source.rename(destination)
        return
    libc = ctypes.CDLL(None, use_errno=True)
    if sys.platform == 'darwin':
        rename = libc.renamex_np
        rename.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
        args = (os.fsencode(source), os.fsencode(destination), 4)  # RENAME_EXCL
    else:
        require(hasattr(libc, 'renameat2'), 'atomic no-replace rename is unavailable on this platform')
        rename = libc.renameat2
        rename.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
        args = (-100, os.fsencode(source), -100, os.fsencode(destination), 1)
    rename.restype = ctypes.c_int
    if rename(*args) != 0:
        error = ctypes.get_errno()
        raise OSError(error, os.strerror(error), str(destination))


def tree(root):
    """Validate each directory entry before descending, including junctions."""
    root = safe(root)
    require(root.is_dir(), f'missing directory: {root}')
    for path in sorted(root.iterdir()):
        safe(path)
        yield path
        if path.is_dir():
            yield from tree(path)


def inventory(root):
    root = safe(root)
    require(root.is_dir(), f'missing directory: {root}')
    entries = []
    for path in sorted(tree(root)):
        if path.is_dir():
            continue
        data = raw(path)
        entries.append(dict(path=path.relative_to(root).as_posix(), bytes=len(data), sha256=digest(data)))
    return entries


def identity_changes(expected, actual):
    before = {item['path']: item for item in expected}
    after = {item['path']: item for item in actual}
    return [path for path in sorted(before.keys() | after.keys()) if before.get(path) != after.get(path)]


def source_identity(work, live=True):
    identity = load(work / 'source-manifest.json')
    fields(identity, {'schema_version', 'files', 'root_fingerprint', 'instruction'})
    require(isinstance(identity['files'], list), 'source files must be an array')
    for entry in identity['files']:
        fields(entry, {'path', 'bytes', 'sha256'})
        require(isinstance(entry['path'], str) and type(entry['bytes']) is int and entry['bytes'] >= 0 and isinstance(entry['sha256'], str) and re.fullmatch(r'[0-9a-f]{64}', entry['sha256']), f'{work / "source-manifest.json"}: malformed source identity entry: {entry["path"]}')
    fields(identity['instruction'], {'path', 'sha256'})
    require(identity['instruction']['path'] == str(work / 'shared/controls/SAVED_INSTRUCTION.md') and isinstance(identity['instruction']['sha256'], str) and re.fullmatch(r'[0-9a-f]{64}', identity['instruction']['sha256']), f'{work / "source-manifest.json"}: malformed initial instruction identity for {work / "shared/controls/SAVED_INSTRUCTION.md"}')
    require(type(identity['schema_version']) is int and identity['schema_version'] == 1 and identity['root_fingerprint'] == digest(canonical(identity['files'])), f'source manifest identity differs: {work / "source-manifest.json"}')
    paths = [f['path'] for f in identity['files']]
    expected_paths = {n + '.md' for n in DN}
    bad_paths = (set(paths) ^ expected_paths) | {p for p in paths if paths.count(p) > 1}
    require(not bad_paths, f'{work / "source-manifest.json"}: missing, extra or duplicate source identities: ' + ', '.join(sorted(bad_paths)))
    if live:
        root = work / 'vault/Sources'
        actual = inventory(root)
        changed = identity_changes(identity['files'], actual)
        changed += [p.relative_to(root).as_posix() for p in tree(root) if p.is_dir()]
        require(paths == sorted(paths), f'source identity order differs: {work / "source-manifest.json"}')
        originals = []
        for item in identity['files']:
            path = work / 'shared/case' / item['path']
            try:
                require(digest(raw(path)) == item['sha256'], f'original source changed: {path}')
            except (ValueError, OSError) as exc:
                originals.append(f'{path}: {exc}')
        require(not changed, 'source identity changed/added/missing: ' + ', '.join(str(root / p) for p in changed) + '\n' + '\n'.join(originals))
        require(not originals, '\n'.join(originals))
    return identity


def initialize(work):
    absent(work / 'vault')
    for name in ['source-manifest.json', 'reviews', 'identities', 'cold']:
        absent(work / name)
    case = safe(work / 'shared/case')
    candidates = [p for p in tree(case) if p.name.lower().startswith('dn-')]
    expected = {case / (n + '.md') for n in DN}
    bad = (expected - set(candidates)) | {p for p in candidates if p not in expected or not p.is_file()}
    require(not bad, 'missing, duplicate, or malformed DN packet file: ' + ', '.join(str(p) for p in sorted(bad)))
    files = []
    for p in sorted(candidates):
        data = raw(p)
        files.append(dict(path=p.name, bytes=len(data), sha256=digest(data)))
    rule = work / 'shared/controls/SAVED_INSTRUCTION.md'
    rule_bytes = raw(rule)
    require(rule_bytes.decode().strip(), 'empty saved instruction')
    templates = {n: raw(work / 'shared/controls' / n) for n in ['NOTE_TEMPLATE.md', 'REVIEW_TEMPLATE.md', 'AUDIT_TEMPLATE.md']}
    vault = work / 'vault'
    vault.mkdir()
    for name in ['Sources', 'Drafts', 'Knowledge', 'Reviews', 'Templates']:
        (vault / name).mkdir()
    for p in candidates:
        write_new(vault / 'Sources' / p.name, raw(p))
    for name, data in templates.items():
        write_new(vault / 'Templates' / name, data)
    write_new(vault / 'MOC.md', b'# Knowledge index\n')
    for name in ['reviews', 'identities', 'cold']:
        (work / name).mkdir()
    save(work / 'source-manifest.json', dict(schema_version=1, files=files, root_fingerprint=digest(canonical(files)), instruction=dict(path=str(rule), sha256=digest(rule_bytes))))


def decode_quote(value):
    return '\n'.join(line[2:] if line.startswith('> ') else line[1:] if line.startswith('>') else line for line in value.replace('\r\n', '\n').split('\n'))


def support(work, source, excerpt):
    require(source in DN, f'unknown source: {source}')
    require(isinstance(excerpt, str) and bool(excerpt.strip()), f'empty excerpt: {source}')
    excerpt = excerpt.replace('\r\n', '\n')
    original = text(work / 'vault/Sources' / (source + '.md'))
    starts = [m.start() for m in re.finditer('(?=' + re.escape(excerpt) + ')', original)]
    require(len(starts) == 1, f'{source}: invented or ambiguous excerpt')
    start = original[:starts[0]].count('\n') + 1
    return dict(source_id=source, locator=f'L{start}-L{start + excerpt.count(chr(10))}', excerpt=excerpt, sha256=digest(excerpt.encode()))


def parse_note(data, note_id):
    require(re.fullmatch(KB, note_id), f'unsafe note ID: {note_id}')
    value = data.decode('utf-8').replace('\r\n', '\n')
    lines = value.splitlines()
    require(lines and re.fullmatch(r'# .+', lines[0]), f'{note_id}: first line must be a title')
    require('[[' not in lines[0] and '](' not in lines[0], f'{note_id}: title cannot contain links')
    headers = list(re.finditer(r'^## (.*)$', value, re.M))
    require([m[1] for m in headers] == SECTIONS, f'{note_id}: use exactly the four ordered sections')
    require(not value[len(lines[0]):headers[0].start()].strip(), f'{note_id}: content before Claim')
    parts = {m[1]: value[m.end()+1:(headers[i+1].start() if i+1 < len(headers) else len(value))].strip('\n') for i, m in enumerate(headers)}
    require(parts['Claim'].strip() and parts['Limits and conflicts'].strip(), f'{note_id}: empty claim or limits')
    evidence, current, quote = [], None, []
    def finish():
        if current is not None:
            require(quote, f'{note_id}: missing block quote for {current}')
            evidence.append(dict(source_id=current, excerpt=decode_quote('\n'.join(quote))))
    for line in parts['Evidence'].splitlines():
        match = re.fullmatch(r'### \[\[(?:Sources/)?(DN-[0-9]{3})\]\]', line)
        if match:
            finish()
            current, quote = match[1], []
        elif line.startswith('>') and current:
            quote.append(line)
        else:
            require(not line.strip(), f'{note_id}: malformed Evidence line: {line}')
    finish()
    require(evidence, f'{note_id}: no evidence')
    related = []
    for line in parts['Related'].splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r'- \[\[Knowledge/(' + KB + r')(?:\|[^\]\n]+)?\]\]', line)
        require(match, f'{note_id}: Related must use existing Knowledge/KB-NNN links; replace Drafts or ambiguous links')
        related.append(match[1])
    # Links outside the two structural link sections are not navigation.
    require(not any('[[' in parts[k] or '](' in parts[k] for k in ['Claim', 'Limits and conflicts']), f'{note_id}: put links in Evidence or Related')
    require(note_id not in related and len(related) == len(set(related)), f'{note_id}: duplicate/self relationship')
    return evidence, related


def note_receipt(work, path):
    evidence, related = parse_note(raw(path), path.stem)
    for target in related:
        require(safe(work / 'vault/Knowledge' / (target + '.md')).is_file(), f'{path.name}: missing Knowledge/{target}.md')
    return [support(work, e['source_id'], e['excerpt']) for e in evidence]


def review(work, note, decision, reason):
    source_identity(work)
    note, reason = safe(note), safe(reason)
    folder = 'Knowledge' if decision == 'admit' else 'Drafts'
    require(note.parent == work / 'vault' / folder and re.fullmatch(KB + r'\.md', note.name), f'{decision} requires vault/{folder}/KB-NNN.md')
    require(reason.is_relative_to(work / 'vault/Reviews'), 'reason file must be under vault/Reviews')
    reason_bytes = raw(reason)
    require(reason_bytes.decode().strip(), 'write a short review reason first')
    quotes = note_receipt(work, note) if decision == 'admit' else []
    receipt = dict(note_id=note.stem, note_sha256=digest(raw(note)), decision=decision, reason_sha256=digest(reason_bytes), reason_text=reason_bytes.decode(), source_manifest_sha256=digest(raw(work / 'source-manifest.json')), quotes=quotes)
    save(work / 'reviews' / f'{note.stem}-{uuid.uuid4().hex}.json', receipt)


def matching_review(work, path):
    for p in sorted(safe(work / 'reviews').glob(path.stem + '-*.json')):
        receipt = load(p)
        if receipt.get('decision') == 'admit' and receipt.get('note_sha256') == digest(raw(path)):
            verify_review(work, path, receipt)
            return dict(path=p.name, sha256=digest(raw(p)))
    return None


def verify_review(work, path, receipt):
    fields(receipt, {'note_id', 'note_sha256', 'decision', 'reason_sha256', 'reason_text', 'source_manifest_sha256', 'quotes'})
    require(receipt['decision'] == 'admit' and receipt['note_id'] == path.stem and receipt['note_sha256'] == digest(raw(path)), f'{path.name}: admission bytes differ')
    require(receipt['source_manifest_sha256'] == digest(raw(work / 'source-manifest.json')), 'review source identity differs')
    require(receipt['reason_text'].strip() and digest(receipt['reason_text'].encode()) == receipt['reason_sha256'], 'immutable review reason differs')
    evidence, _ = parse_note(raw(path), path.stem)
    require(len(receipt['quotes']) == len(evidence), 'review quote set differs')
    for item, quote in zip(evidence, receipt['quotes']):
        fields(quote, {'source_id', 'locator', 'excerpt', 'sha256'})
        require(quote['source_id'] in DN, f'unknown receipt source: {quote["source_id"]}')
        require(item == {k: quote[k] for k in item} and quote['sha256'] == digest(quote['excerpt'].encode()) and re.fullmatch(r'L[1-9][0-9]*-L[1-9][0-9]*', quote['locator']), 'review quote identity differs')


def navigation(root, files):
    notes = {Path(f['path']).stem for f in files if f['path'].startswith('Knowledge/')}
    require(notes, 'no admitted Knowledge notes')
    links = set()
    for i, line in enumerate(text(root / 'MOC.md').splitlines()):
        if not line.strip() or i == 0 and re.fullmatch(r'# .+', line):
            continue
        match = re.fullmatch(r'- \[\[Knowledge/(' + KB + r')(?:\|[^\]\n]+)?\]\]', line)
        require(match, 'MOC.md accepts only a title and Knowledge links')
        links.add(match[1])
    require(links <= notes, 'MOC.md names missing Knowledge notes')
    graph = {}
    for name in notes:
        _, related = parse_note(raw(root / 'Knowledge' / (name + '.md')), name)
        require(set(related) <= notes, f'{name}: missing Knowledge link')
        graph[name] = related
    reached = set(links)
    while True:
        expanded = reached | {n for p in reached for n in graph[p]}
        if expanded == reached:
            break
        reached = expanded
    require(reached == notes, 'MOC.md does not reach every Knowledge note')


def content_files(root):
    files = inventory(root)
    bad = {f['path'] for f in files if not (f['path'] == 'MOC.md' or re.fullmatch(r'Knowledge/' + KB + r'\.md', f['path']))}
    directories = {p.relative_to(root).as_posix() for p in tree(root) if p.is_dir()}
    bad |= directories ^ {'Knowledge'}
    require(not bad, 'cold content/directory membership differs: ' + ', '.join(str(root / p) for p in sorted(bad)))
    return files


def revision_id(value):
    require(re.fullmatch(r'[a-z][a-z0-9-]*', value), f'unsafe revision: {value}')
    return value


def check(work, revision, seen=None):
    revision_id(revision)
    seen = set() if seen is None else seen
    require(revision not in seen, 'cyclic previous revision')
    seen.add(revision)
    manifest = load(work / 'identities' / (revision + '.json'))
    fields(manifest, {'schema_version', 'files', 'root_fingerprint', 'source_manifest_sha256', 'instruction_sha256', 'reviews', 'previous_manifest_sha256', 'previous', 'focus_note'})
    require(type(manifest['schema_version']) is int and manifest['schema_version'] == 1, 'unsupported manifest schema')
    require(isinstance(manifest['files'], list) and isinstance(manifest['reviews'], dict), 'malformed snapshot files/reviews')
    paths = set()
    for entry in manifest['files']:
        fields(entry, {'path', 'bytes', 'sha256'})
        relative = entry['path']
        require(isinstance(relative, str) and (relative == 'MOC.md' or re.fullmatch(r'Knowledge/' + KB + r'\.md', relative)), f'unsafe snapshot path: {relative}')
        require(relative not in paths, f'duplicate snapshot path: {relative}')
        paths.add(relative)
        require(type(entry['bytes']) is int and entry['bytes'] >= 0 and isinstance(entry['sha256'], str) and re.fullmatch(r'[0-9a-f]{64}', entry['sha256']), f'malformed snapshot identity: {relative}')
    source = source_identity(work, live=False)
    require(manifest['source_manifest_sha256'] == digest(raw(work / 'source-manifest.json')) and manifest['instruction_sha256'] == source['instruction']['sha256'], 'snapshot source/rule identity differs')
    root = work / 'cold' / revision
    actual = content_files(root)
    if actual != manifest['files']:
        expected = {i['path']: i for i in manifest['files']}
        current = {i['path']: i for i in actual}
        bad = [p for p in sorted(expected.keys() | current.keys()) if expected.get(p) != current.get(p)]
        raise ValueError('snapshot changed/added/missing: ' + ', '.join(bad))
    require(manifest['root_fingerprint'] == digest(canonical(actual)), 'snapshot fingerprint differs')
    navigation(root, actual)
    require(set(manifest['reviews']) == {f['path'] for f in actual if f['path'] != 'MOC.md'}, 'snapshot admission set differs')
    for relative, entry in manifest['reviews'].items():
        fields(entry, {'path', 'sha256'})
        require(re.fullmatch(KB + r'-[0-9a-f]+\.json', entry['path']), 'unsafe review receipt path')
        p = work / 'reviews' / entry['path']
        require(digest(raw(p)) == entry['sha256'], f'review receipt changed: {p.name}')
        verify_review(work, root / relative, load(p))
    if manifest['previous'] is not None:
        previous = revision_id(manifest['previous'])
        require(digest(raw(work / 'identities' / (previous + '.json'))) == manifest['previous_manifest_sha256'], 'previous manifest changed')
        old = check(work, previous, seen)
        delta(old, manifest['files'], manifest['focus_note'])
    else:
        require(manifest['previous_manifest_sha256'] is None and manifest['focus_note'] is None, 'initial revision cannot have a focus/previous hash')
    return manifest


def delta(previous, files, focus):
    before = {f['path']: f['sha256'] for f in previous['files'] if f['path'].startswith('Knowledge/')}
    after = {f['path']: f['sha256'] for f in files if f['path'].startswith('Knowledge/')}
    require(before.keys() <= after.keys(), 'revision deleted Knowledge notes')
    changed = {p for p in after if before.get(p) != after[p]}
    require(f'Knowledge/{focus}.md' in changed, 'focus_note must be a changed or new Knowledge note')


def admission_hint(work, path):
    reason = work / 'vault/Reviews' / (path.stem + '.md')
    command = [sys.executable, work / 'scripts/second_brain.py', 'review', '--work', work,
               '--note', path, '--decision', 'admit', '--reason-file', reason]
    shell_quote = lambda value: "'" + str(value).replace("'", "'\"'\"'") + "'"
    ps_quote = lambda value: "'" + str(value).replace("'", "''") + "'"
    return (f'{path}: inspect/remove this note in Obsidian, or complete it and review it.\n'
            f'Create a short-reason file at {reason}, or substitute your actual short-reason file under vault/Reviews in the command.\n'
            'Bash/zsh: ' + ' '.join(shell_quote(part) for part in command) + '\n'
            'PowerShell: & ' + ' '.join(ps_quote(part) for part in command))


def knowledge_issues(root):
    """Collect all unsafe entries without descending through a link or junction."""
    root = safe(root)
    issues = []
    def visit(directory):
        for path in sorted(directory.iterdir()):
            try:
                safe(path)
            except (ValueError, OSError) as exc:
                issues.append(f'{path}: {exc}')
                continue
            if path.parent != root or not re.fullmatch(KB + r'\.md', path.name) or not path.is_file():
                issues.append(str(path))
            if path.is_dir():
                visit(path)
    visit(root)
    return issues


def freeze(work, revision, previous=None, focus=None):
    revision_id(revision)
    destination = absent(work / 'cold' / revision)
    manifest_path = absent(work / 'identities' / (revision + '.json'))
    source = source_identity(work)
    require(digest(raw(work / 'shared/controls/SAVED_INSTRUCTION.md')) == source['instruction']['sha256'], 'saved instruction changed')
    knowledge_root = work / 'vault/Knowledge'
    unsafe = knowledge_issues(knowledge_root)
    # Keep collecting unreviewed direct notes even when another filename is unsafe.
    knowledge = []
    for p in sorted(knowledge_root.iterdir()):
        if re.fullmatch(KB + r'\.md', p.name):
            try:
                data = raw(p)
            except (ValueError, OSError) as exc:
                unsafe.append(f'{p}: {exc}')
                continue
            knowledge.append(dict(path=p.name, bytes=len(data), sha256=digest(data)))
    reviews, missing = {}, []
    for item in knowledge:
        p = work / 'vault/Knowledge' / item['path']
        try:
            receipt = matching_review(work, p)
            if receipt is None:
                missing.append(admission_hint(work, p))
            else:
                note_receipt(work, p)
                reviews['Knowledge/' + p.name] = receipt
        except (ValueError, OSError) as exc:
            missing.append(f'{p}: {exc}')
    issues = (['Unsafe Knowledge entries: ' + '; '.join(unsafe) +
               '. Inspect/remove these files or directories in Obsidian, or give each note a unique KB-NNN.md name, complete it and review it.'] if unsafe else []) + missing
    require(not issues, 'Knowledge needs attention:\n' + '\n'.join(issues))
    files = [dict(path='MOC.md', bytes=len(raw(work / 'vault/MOC.md')), sha256=digest(raw(work / 'vault/MOC.md')))] + [dict(f, path='Knowledge/' + f['path']) for f in knowledge]
    files.sort(key=lambda f: f['path'])
    navigation(work / 'vault', files)
    prior = None
    if previous:
        previous = safe(previous)
        require(previous.parent == work / 'identities' and previous.suffix == '.json', 'previous must be an external identity in this work')
        prior = check(work, previous.stem)
        delta(prior, files, focus)
    else:
        require(focus is None, 'focus-note requires previous')
    manifest = dict(schema_version=1, files=files, root_fingerprint=digest(canonical(files)), source_manifest_sha256=digest(raw(work / 'source-manifest.json')), instruction_sha256=source['instruction']['sha256'], reviews=reviews, previous=previous.stem if previous else None, previous_manifest_sha256=digest(raw(previous)) if previous else None, focus_note=focus)
    # Exclusive sibling lock serializes publishers; existing attempts are never replaced.
    lock = absent(destination.with_name('.' + revision + '.lock'))
    lock.mkdir()
    temporary = Path(tempfile.mkdtemp(prefix='.' + revision + '-', dir=safe(destination.parent)))
    try:
        (temporary / 'Knowledge').mkdir()
        for item in files:
            write_new(temporary / item['path'], raw(work / 'vault' / item['path']))
        require(content_files(temporary) == files, 'content changed while freezing')
        require(source_identity(work) == source, 'source identity changed while freezing')
        require(digest(raw(work / 'shared/controls/SAVED_INSTRUCTION.md')) == manifest['instruction_sha256'], 'saved instruction changed while freezing')
        for entry in reviews.values():
            require(digest(raw(work / 'reviews' / entry['path'])) == entry['sha256'], 'review receipt changed while freezing')
        absent(destination)
        absent(manifest_path)
        publish_directory(temporary, destination)
        save(manifest_path, manifest)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
        lock.rmdir()


def response_json(value):
    value = value.strip()
    if value.startswith('```'):
        match = re.fullmatch(r'```(?:json)?\n(.*)\n```', value, re.S)
        require(match, 'response must be JSON or one outer JSON fence')
        value = match[1]
    return strict(value)


def stage(work, response):
    value = response_json(response)
    fields(value, {'notes'})
    require(isinstance(value['notes'], list), 'notes must be an array')
    ids = [n.get('note_id') for n in value['notes'] if isinstance(n, dict)]
    valid, invalid = [], []
    for index, note in enumerate(value['notes']):
        name = note.get('note_id') if isinstance(note, dict) else None
        try:
            fields(note, {'note_id', 'title', 'claim', 'limits', 'related', 'sources'})
            require(isinstance(name, str) and re.fullmatch(KB, name), 'unsafe note ID')
            require(ids.count(name) == 1, f'duplicate note ID {name}')
            for key in ['title', 'claim', 'limits']:
                require(isinstance(note[key], str) and note[key].strip(), f'empty {key}')
            require('\n' not in note['title'] and '\r' not in note['title'], 'multiline title')
            require(isinstance(note['related'], list) and all(isinstance(n, str) and n in ids and n != name for n in note['related']) and len(set(note['related'])) == len(note['related']), 'invalid related IDs')
            require(isinstance(note['sources'], list) and note['sources'], 'missing sources')
            quotes = []
            for s in note['sources']:
                fields(s, {'source_id', 'excerpt'})
                quotes.append(support(work, s['source_id'], s['excerpt']))
            body = f'# {note["title"]}\n## Claim\n{note["claim"]}\n## Limits and conflicts\n{note["limits"]}\n## Evidence\n'
            for q in quotes:
                body += f'### [[Sources/{q["source_id"]}]]\n' + '\n'.join('> ' + line for line in q['excerpt'].split('\n')) + '\n'
            body += '## Related\n'
            # Validate structural Markdown before adding deliberately non-clickable suggestions.
            parse_note(body.encode(), name)
            body += ''.join(f'- {n} — {next((p.get("title", n) for p in value["notes"] if isinstance(p, dict) and p.get("note_id") == n), n)}\n' for n in note['related'])
            valid.append((name, body))
        except (ValueError, TypeError, KeyError) as exc:
            invalid.append(dict(note_id=name if isinstance(name, str) else f'proposal-{index+1}', reason=str(exc)))
    for name, body in valid:
        write_new(work / 'vault/Drafts' / (name + '.md'), body.encode())
    save(work / 'reviews/ingest-report.json', dict(staged=[n for n, _ in valid], invalid=invalid))
    require(not invalid, 'proposal HOLD: ' + '; '.join(f'{n["note_id"]}: {n["reason"]}' for n in invalid))


def runner_module(path):
    path = safe(path)
    raw(path)
    spec = importlib.util.spec_from_file_location('module02_explicit_runner', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def phase_audit(work, evidence, runtime, phase, manifest=None):
    inventory(evidence)  # Reject selected receipt files or parents that are links.
    errors = runtime.audit_evidence(evidence)
    require(not errors, 'shared runtime audit: ' + '; '.join(errors))
    source = source_identity(work, live=phase == 'ingest')
    root = work / 'vault/Sources' if phase == 'ingest' else work / 'cold' / manifest[0]
    expected = source['files'] if phase == 'ingest' else manifest[1]['files']
    policy, result = load(evidence / 'policy.json'), load(evidence / 'result.json')
    prompt = work / 'shared/controls' / ('INGEST_PROMPT.md' if phase == 'ingest' else 'RETRIEVE_PROMPT.md')
    require(policy['profile'] == 'read' and policy['tools'] == ['course_read'] and policy['work_root'] == str(root), 'phase read policy/root differs')
    require(policy['instruction'] == source['instruction'], 'missing or changed saved-instruction descriptor')
    require(policy['prompt_sha256'] == digest(raw(prompt)), 'phase prompt differs')
    require(result['input_sha256'] == {f['path']: f['sha256'] for f in expected} and result['output_sha256'] == {}, 'phase input/output identity differs')
    require(inventory(root) == expected, 'phase input bytes changed')
    guard = runtime.read_jsonl(evidence / 'guard.jsonl')
    snapshots = load(evidence / 'snapshots.json')
    reads, classifications = set(), []
    events = runtime.read_jsonl(evidence / 'events.jsonl')
    for call, row, event, classification in attempted_calls(guard, events):
        if event:
            require(event['tool'] == 'course_read' and event.get('output_sha256') is None, 'non-read effect')
            target = Path(event['resolved_path'])
            require(target.is_relative_to(root), 'read escaped phase root')
            relative = target.relative_to(root).as_posix()
            if relative in {f['path'] for f in expected}:
                reads.add(relative)
            else:
                require(relative == '.' or snapshots['before']['work'].get(relative, {}).get('type') == 'directory', f'successful read of nonmember: {relative}')
        elif classification == 'ALLOWED_ABSENT':
            target = Path(row.get('resolved_path', ''))
            require(target.is_absolute() and target.is_relative_to(root) and not target.exists(), 'allowed failed call was not an absent in-root path')
        classifications.append(classification)
    if phase == 'ingest':
        require(reads == {n + '.md' for n in DN}, 'ingest must read forty distinct DN files')
    else:
        require('MOC.md' in reads, 'cold run did not read MOC.md')
    return reads, classifications or ['NOT_ATTEMPTED']


def attempted_calls(guard, events):
    """Enumerate actual calls after the shared auditor has verified their receipts."""
    decisions = {row['call_id']: row for row in guard if row['type'] == 'decision'}
    executed = {row['call_id']: row for row in guard if row['type'] == 'executed'}
    for row in events:
        message = row.get('message', {})
        if row['type'] != 'message_end' or message.get('role') != 'assistant':
            continue
        for call in message.get('content', []):
            if call.get('type') != 'toolCall':
                continue
            decision, execution = decisions.get(call['id']), executed.get(call['id'])
            # A missing decision can pass the shared audit only for an
            # undeclared tool rejected by OMP before the extension hook.
            state = 'EXECUTED' if execution else 'ALLOWED_ABSENT' if decision and decision.get('allow') else 'DENIED'
            yield call, decision, execution, state


def raw_access_observations(guard, events):
    """Classify raw-source path references in call arguments, not successful reads."""
    def mentions_raw(value):
        if isinstance(value, str):
            return bool(re.search(r'(?<![\w.-])(?:Sources|Drafts|Reviews|shared|DN-[0-9]{3}\.md)(?![\w.-])', value))
        if isinstance(value, dict):
            return any(mentions_raw(item) for item in value.values())
        if isinstance(value, list):
            return any(mentions_raw(item) for item in value)
        return False

    observations = []
    for call, decision, execution, state in attempted_calls(guard, events):
        if not mentions_raw(call.get('arguments')):
            continue
        observations.append(state)
    return observations or ['NOT_ATTEMPTED']


def answers(work, revision, manifest, reads, response):
    value = response_json(response)
    fields(value, {'answers'})
    require(isinstance(value['answers'], list) and len(value['answers']) == 3, 'exactly three answers required')
    seen, cited = set(), set()
    for answer in value['answers']:
        fields(answer, {'question_id', 'status', 'answer', 'citations'})
        q = answer['question_id']
        require(q in {'Q1', 'Q2', 'Q3'} and q not in seen, 'duplicate/unknown question ID')
        seen.add(q)
        require(answer['status'] in {'supported', 'unsupported'} and isinstance(answer['answer'], str) and answer['answer'].strip() and isinstance(answer['citations'], list), f'{q}: malformed answer')
        require(answer['status'] != 'supported' or answer['citations'], f'{q}: supported answer needs citations')
        for citation in answer['citations']:
            fields(citation, {'note_id', 'source_id', 'excerpt'})
            name = citation['note_id']
            require(isinstance(name, str) and re.fullmatch(KB, name), 'unsafe cited KB ID')
            relative = f'Knowledge/{name}.md'
            require(relative in reads and relative in manifest['reviews'], f'{q}: unread/unfrozen citation {name}')
            quotes, _ = parse_note(raw(work / 'cold' / revision / relative), name)
            excerpt = citation['excerpt']
            require(isinstance(excerpt, str) and excerpt.strip(), 'empty citation excerpt')
            # Try literal first: a source's leading > must never disappear merely
            # because it resembles presentation syntax.
            candidates = [excerpt.replace('\r\n', '\n'), decode_quote(excerpt)]
            require(any(c and c in item['excerpt'] for item in quotes if item['source_id'] == citation['source_id'] for c in candidates), f'{q}: fabricated DN/excerpt citation')
            cited.add(name)
        print(f'{q} ({answer["status"]}): {answer["answer"]}')
        for c in answer['citations']:
            print(f'  Knowledge/{c["note_id"]}.md · {c["source_id"]}: {c["excerpt"]}')
    require(manifest['focus_note'] is None or manifest['focus_note'] in cited, 'revised focus note must be read and cited')


def paid(work, runtime_path, evidence, phase, revision=None):
    rule = safe(work / 'shared/controls/SAVED_INSTRUCTION.md')
    if not rule.is_file():
        print(f'HOLD: missing saved instruction: {rule}', file=sys.stderr)
        return 2
    source = source_identity(work, live=phase == 'ingest')
    require(digest(raw(rule)) == source['instruction']['sha256'], 'saved instruction differs from initial identity')
    evidence = absent(evidence)
    require(not (evidence.is_relative_to(work) or work.is_relative_to(evidence)), 'work and evidence overlap')
    manifest = check(work, revision) if phase == 'retrieve' else None
    root = work / 'cold' / revision if manifest else work / 'vault/Sources'
    prompt = safe(work / 'shared/controls' / ('INGEST_PROMPT.md' if phase == 'ingest' else 'RETRIEVE_PROMPT.md'))
    prompt_hash = digest(raw(prompt))
    runtime = runner_module(runtime_path)
    marker = work / 'reviews/ingest-attempt.json'
    reservation = None
    if phase == 'ingest':
        absent(work / 'reviews/ingest-report.json')
        require(not list(safe(work / 'vault/Drafts').iterdir()), 'staged drafts already exist; use fresh work and evidence')
        reservation = dict(reservation=uuid.uuid4().hex, evidence=str(evidence), source_manifest_sha256=digest(raw(work / 'source-manifest.json')), instruction=source['instruction'], prompt_sha256=prompt_hash)
        save(marker, reservation)
    code = runtime.main(['--workdir', str(root), '--prompt', str(prompt), '--instruction', str(rule), '--evidence', str(evidence)])
    if phase == 'ingest' and code == 2 and not evidence.exists() and not evidence.is_symlink():
        require(load(marker) == reservation, 'ingest reservation changed; preserve it')
        save(work / 'reviews' / ('ingest-preflight-' + uuid.uuid4().hex + '.json'), reservation)
        marker.unlink()
        return 2
    if code != 0:
        return code if code in {1, 2} else 1
    require(digest(raw(prompt)) == prompt_hash, 'phase prompt changed during run')
    reads, classifications = phase_audit(work, evidence, runtime, phase, (revision, manifest) if manifest else None)
    print('Observed calls: ' + ', '.join(classifications))
    if phase == 'ingest':
        stage(work, text(evidence / 'response.md'))
    else:
        print('Raw-source access: ' + ', '.join(raw_access_observations(runtime.read_jsonl(evidence / 'guard.jsonl'), runtime.read_jsonl(evidence / 'events.jsonl'))))
        answers(work, revision, manifest, reads, text(evidence / 'response.md'))
        check(work, revision)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ['initialize', 'ingest', 'review', 'freeze', 'retrieve', 'check']:
        p = sub.add_parser(command)
        p.add_argument('--work', required=True, type=Path)
        if command in {'freeze', 'retrieve', 'check'}:
            p.add_argument('--revision', required=True)
        if command in {'ingest', 'retrieve'}:
            p.add_argument('--runner', required=True, type=Path)
            p.add_argument('--evidence', required=True, type=Path)
        if command == 'review':
            p.add_argument('--note', required=True, type=Path)
            p.add_argument('--decision', required=True, choices=['admit', 'reject'])
            p.add_argument('--reason-file', required=True, type=Path)
        if command == 'freeze':
            p.add_argument('--previous', type=Path)
            p.add_argument('--focus-note')
    args = parser.parse_args(argv)
    try:
        work = safe(args.work)
        require(work.is_dir(), f'missing work directory: {work}')
        if args.command == 'initialize':
            rule = safe(work / 'shared/controls/SAVED_INSTRUCTION.md')
            if not rule.is_file():
                print(f'HOLD: missing saved instruction: {rule}', file=sys.stderr)
                return 2
            initialize(work)
        elif args.command == 'review':
            review(work, args.note, args.decision, args.reason_file)
        elif args.command == 'freeze':
            freeze(work, args.revision, args.previous, args.focus_note)
        elif args.command == 'check':
            check(work, args.revision)
        else:
            return paid(work, args.runner, args.evidence, args.command, getattr(args, 'revision', None))
        print(f'PASS: {args.command}')
        return 0
    except (OSError, ValueError, UnicodeError, TypeError, KeyError, AttributeError, RuntimeError, ImportError) as exc:
        print(f'HOLD: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
