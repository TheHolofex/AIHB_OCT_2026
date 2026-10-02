#!/usr/bin/env python3
"""Behavioral oracle. Sealed receipts below are synthetic, never provider evidence."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1]
REPO = MODULE.parents[1]
sys.path.insert(0, str(REPO))
from shared import run_omp as runtime

spec = importlib.util.spec_from_file_location('second_brain_oracle', MODULE / 'scripts/second_brain.py')
brain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(brain)


def holds(action):
    try:
        action()
    except (ValueError, OSError) as exc:
        return str(exc)
    raise AssertionError('invalid operation was accepted')


def prepare(base):
    work = base / 'work'
    work.mkdir()
    shutil.copytree(MODULE / 'shared/case', work / 'shared/case')
    shutil.copytree(MODULE / 'shared/controls', work / 'shared/controls')
    brain.initialize(work)
    return work


def proposal(work, name='KB-001'):
    # Include literal Markdown and multiple lines exactly as present in the packet.
    excerpt = brain.text(work / 'vault/Sources/DN-003.md')
    return dict(note_id=name, title='Paper receipt', claim='Paper receipt is recorded.', limits='Other authority remains separate.', related=[], sources=[dict(source_id='DN-003', excerpt=excerpt)])


def author(work, name='KB-001', extra=''):
    p = proposal(work, name)
    body = f'# {p["title"]}\n## Claim\n{p["claim"]}{extra}\n## Limits and conflicts\n{p["limits"]}\n## Evidence\n### [[Sources/DN-003]]\n'
    body += '\n'.join('> ' + line for line in p['sources'][0]['excerpt'].split('\n'))
    body += '\n## Related\n'
    note = work / 'vault/Knowledge' / (name + '.md')
    note.write_text(body)
    reason = work / 'vault/Reviews' / (name + '.md')
    reason.write_text('Admit: source quote checked; authority remains a limit.\n')
    return note, reason


def admit(work, name='KB-001', extra=''):
    note, reason = author(work, name, extra)
    brain.review(work, note, 'admit', reason)
    (work / 'vault/MOC.md').write_text('# Index\n' + ''.join(f'- [[Knowledge/{p.stem}|{p.stem}]]\n' for p in sorted((work / 'vault/Knowledge').glob('*.md'))))
    return note, reason


def cold_answers(work, status='supported'):
    excerpt = proposal(work)['sources'][0]['excerpt']
    return dict(answers=[dict(question_id=f'Q{i}', status=status, answer='Synthetic source-bounded answer.' if status == 'supported' else 'Missing evidence for the remaining authority.', citations=[dict(note_id='KB-001', source_id='DN-003', excerpt='\n'.join('> ' + line for line in excerpt.split('\n')))] if status == 'supported' else []) for i in range(1, 4)])


class Sealed:
    """Module 08's locally sealed synthetic pattern, using the real shared auditor."""
    def __init__(self, work, evidence, root, prompt, actions=(), response='{}'):
        self.work, self.evidence, self.root = work, evidence, root
        evidence.mkdir()
        overlay = {'retry': {'enabled': False, 'modelFallback': False}, 'providers': {'cacheWarming': 'off'}, 'tools': {'approval': {'course_read': 'allow'}}}
        (evidence / 'runtime-config.yml').write_bytes(runtime.json_bytes(overlay))
        rule = work / 'shared/controls/SAVED_INSTRUCTION.md'
        self.policy = dict.fromkeys(runtime.POLICY_KEYS)
        self.policy.update(schema_version=1, run_id='synthetic-module02', work_root=str(root), profile='read', tools=['course_read'], write_files=[], write_root=None, provider=runtime.PROVIDER, model=runtime.MODEL, omp_version=runtime.OMP_VERSION, prompt_sha256=runtime.file_hash(prompt), instruction={'path': str(rule), 'sha256': runtime.file_hash(rule)}, declaration=None, python=sys.executable, guard_source_sha256=runtime.file_hash(runtime.GUARD), runtime_config_sha256=runtime.file_hash(evidence / 'runtime-config.yml'), guard_log=str(evidence / 'guard.jsonl'), watch_paths=[])
        self.snapshots = {'before': runtime.snapshot(root, []), 'after': runtime.snapshot(root, [])}
        common = dict(run_id=self.policy['run_id'])
        self.guard = [dict(type='guard_ready', provider=runtime.PROVIDER, model=runtime.MODEL, active_tools=['course_read'], **common), dict(type='instruction_loaded', file_sha256=runtime.file_hash(rule), loaded_text_sha256=runtime.sha256(rule.read_bytes().decode().strip().encode()), **common), dict(type='provider_request', provider=runtime.PROVIDER, model=runtime.MODEL, **common)]
        self.events = [{'type': 'agent_start'}]
        for i, (kind, relative) in enumerate(actions):
            target = (root / relative).resolve()
            identifier = f'call-{i}'
            args = {'path': relative}
            pre_hook = kind in {'unknown-read', 'unknown-write', 'unknown-bash'}
            tool = {'unknown-read': 'read', 'unknown-write': 'course_write', 'unknown-bash': 'bash'}.get(kind, 'course_read')
            if kind == 'unknown-write':
                args['content'] = 'Attempted write that must never reach disk.'
            elif kind == 'unknown-bash':
                args = {'command': f'cat {relative}'}
            error = pre_hook or kind in {'deny', 'absent'}
            content = [{'type': 'text', 'text': f'Tool {tool} not found' if pre_hook else 'HOLD: synthetic denial' if kind == 'deny' else 'ENOENT: synthetic absent path' if kind == 'absent' else '\n'.join(p.name for p in target.iterdir()) if target.is_dir() else target.read_text()}]
            call = dict(type='toolCall', id=identifier, name=tool, arguments=args)
            assistant = dict(role='assistant', provider=runtime.PROVIDER, model=runtime.MODEL, stopReason='toolUse', content=[call])
            self.events.extend([dict(type='message_end', message=assistant), dict(type='tool_execution_start', toolCallId=identifier, toolName=tool, args=args), dict(type='tool_execution_end', toolCallId=identifier, toolName=tool, result={'content': content}, isError=error), dict(type='message_end', message=dict(role='toolResult', toolCallId=identifier, toolName=tool, content=content, isError=error))])
            if pre_hook:
                continue
            decision = dict(type='decision', call_id=identifier, tool='course_read', arguments=args, allow=kind != 'deny', resolved_path=None if kind == 'deny' else str(target), **common)
            self.guard.append(decision)
            if kind != 'deny':
                self.guard.append(dict(decision, type='execution_check'))
            if not error:
                self.guard.append(dict(type='executed', call_id=identifier, tool='course_read', resolved_path=str(target), output_sha256=None, **common))
        self.response = response
        final = dict(role='assistant', provider=runtime.PROVIDER, model=runtime.MODEL, stopReason='stop', content=[dict(type='text', text=response)])
        self.events += [dict(type='message_end', message=final), dict(type='agent_end', isTerminal=True, messages=[final])]
        self.guard.append(dict(type='guard_end', ready=True, failed=False, provider_requests=1, **common))
        self.seal()

    def seal(self):
        e, p = self.evidence, self.policy
        (e / 'policy.json').write_bytes(runtime.json_bytes(p))
        for row in self.guard:
            if row['type'] in {'guard_ready', 'guard_end', 'instruction_loaded'}:
                row['policy_sha256'] = runtime.file_hash(e / 'policy.json')
        for name in ['events', 'guard']:
            (e / (name + '.jsonl')).write_text(''.join(json.dumps(row) + '\n' for row in getattr(self, name)))
        (e / 'snapshots.json').write_bytes(runtime.json_bytes(self.snapshots))
        (e / 'response.md').write_text(self.response)
        result = dict(run_id=p['run_id'], provider=runtime.PROVIDER, model=runtime.MODEL, omp_version=runtime.OMP_VERSION, exit_code=0, policy_sha256=runtime.file_hash(e / 'policy.json'), guard_sha256=runtime.file_hash(e / 'guard.jsonl'), declared_policy_sha256=None, instruction_sha256=p['instruction']['sha256'] if p['instruction'] else None, input_sha256={k: v['sha256'] for k, v in self.snapshots['before']['work'].items() if v['type'] == 'file'}, output_sha256={}, status='PASS', reason='Explicitly synthetic sealed receipt; no provider contact.')
        (e / 'result.json').write_bytes(runtime.json_bytes(result))


def guard_group(work, base):
    for name, code in [('DN-003', 0), ('DN-014', 1), ('DN-015', 1), ('DN-016', 1), ('DN-999', 1)]:
        result = subprocess.run([sys.executable, str(MODULE / 'shared/case/guard.py'), str(work / 'shared/case' / (name + '.md'))], capture_output=True, text=True)
        assert result.returncode == code, f'file screen {name}'


def source_group(work, base):
    p = proposal(work)
    brain.support(work, 'DN-003', p['sources'][0]['excerpt'])
    holds(lambda: brain.support(work, 'DN-014', p['sources'][0]['excerpt']))
    holds(lambda: brain.support(work, 'DN-003', 'invented evidence'))
    holds(lambda: brain.response_json('{"notes":[],"notes":[]}'))
    holds(lambda: brain.response_json('prose {"notes":[]}'))
    bad = dict(p, note_id='KB-002', sources=[dict(source_id='DN-999', excerpt='invented')])
    holds(lambda: brain.stage(work, json.dumps({'notes': [p, bad]})))
    assert (work / 'vault/Drafts/KB-001.md').is_file()
    assert not (work / 'vault/Drafts/KB-002.md').exists()
    assert brain.load(work / 'reviews/ingest-report.json')['invalid'][0]['note_id'] == 'KB-002'
    for label, proposals in [('duplicate', [p, p]), ('unknown-field', [dict(p, authority='invented')]), ('empty-claim', [dict(p, claim='')]), ('malformed-source', [dict(p, sources=[dict(source_id='DN-003', excerpt='x', locator='L1')])])]:
        parent = base / ('proposal-' + label)
        parent.mkdir()
        other = prepare(parent)
        holds(lambda: brain.stage(other, json.dumps({'notes': proposals})))
        assert not list((other / 'vault/Drafts').iterdir())
    parent = base / 'malformed-top'
    parent.mkdir()
    other = prepare(parent)
    holds(lambda: brain.stage(other, '{"notes": [], "extra": true}'))
    assert not list((other / 'vault/Drafts').iterdir())
    assert not (other / 'reviews/ingest-report.json').exists()
    source = work / 'vault/Sources/DN-001.md'
    source.write_text(source.read_text() + '\nChanged\n')
    missing = work / 'vault/Sources/DN-002.md'
    missing.unlink()
    extra = work / 'vault/Sources/Untitled.md'
    extra.touch()
    extra_dir = work / 'vault/Sources/extra'
    extra_dir.mkdir()
    error = holds(lambda: brain.source_identity(work))
    assert all(str(path) in error for path in [source, missing, extra, extra_dir]), error
    for defect in ['missing', 'duplicate']:
        target = base / defect
        shutil.copytree(work / 'shared', target / 'shared')
        if defect == 'missing':
            (target / 'shared/case/DN-040.md').unlink()
        else:
            (target / 'shared/case/nested').mkdir()
            shutil.copyfile(target / 'shared/case/DN-001.md', target / 'shared/case/nested/DN-001.md')
        error = holds(lambda: brain.initialize(target))
        expected = target / ('shared/case/DN-040.md' if defect == 'missing' else 'shared/case/nested/DN-001.md')
        assert str(expected) in error, error


def review_group(work, base):
    note, reason = author(work)
    (work / 'vault/MOC.md').write_text('# Index\n- [[Knowledge/KB-001]]\n')
    holds(lambda: brain.freeze(work, 'unreviewed'))
    brain.review(work, note, 'admit', reason)
    receipt = next((work / 'reviews').glob('KB-001-*.json'))
    saved = receipt.read_bytes()
    content = brain.load(receipt)
    assert content['quotes'][0]['locator'].startswith('L1-')
    assert content['reason_text'] == reason.read_text()
    receipt.write_text(json.dumps(dict(content, reason_text='substituted')))
    holds(lambda: brain.freeze(work, 'changed-receipt'))
    receipt.write_bytes(saved)
    brain.freeze(work, 'v1')
    draft = work / 'vault/Drafts/KB-002.md'
    draft.write_text('malformed proposal with no source')
    brain.review(work, draft, 'reject', reason)
    note.write_text(note.read_text() + '\n')
    holds(lambda: brain.freeze(work, 'changed-note'))
    empty = work / 'vault/Knowledge/KB-003.md'
    empty.touch()
    untitled = empty.with_name('Untitled.md')
    duplicate = empty.with_name('KB-001 1.md')
    nested = empty.parent / 'nested'
    nested.mkdir()
    nested_note = nested / 'KB-004.md'
    for path in [untitled, duplicate, nested_note]:
        path.touch()
    error = holds(lambda: brain.freeze(work, 'empty-note'))
    assert all(str(path) in error for path in [note, empty, untitled, duplicate, nested, nested_note]), error
    assert empty.exists()
    # Exercise emitted commands with spaces, apostrophes and shell metacharacters.
    parent = base / "learner's $vault `local`"
    parent.mkdir()
    other = prepare(parent)
    (other / 'scripts').mkdir()
    shutil.copyfile(MODULE / 'scripts/second_brain.py', other / 'scripts/second_brain.py')
    for name in ['KB-001', 'KB-002']:
        p, r = author(other, name)
        r.unlink()  # The suggested reason path does not already exist.
    error = holds(lambda: brain.freeze(other, 'unreviewed'))
    bash = [line.removeprefix('Bash/zsh: ') for line in error.splitlines() if line.startswith('Bash/zsh: ')]
    powershell = [line.removeprefix('PowerShell: ') for line in error.splitlines() if line.startswith('PowerShell: ')]
    assert len(bash) == len(powershell) == 2
    for index, command in enumerate(bash, 1):
        argv = shlex.split(command)
        assert argv[:3] == [sys.executable, str(other / 'scripts/second_brain.py'), 'review']
        assert Path(argv[argv.index('--note') + 1]) == other / f'vault/Knowledge/KB-{index:03}.md'
        reason_path = Path(argv[argv.index('--reason-file') + 1])
        assert not reason_path.exists() and str(reason_path) in error
        reason_path.write_text('Admit: checked source support; authority remains a limit.\n')
        result = subprocess.run(command, shell=True, executable='/bin/bash', capture_output=True, text=True) if os.name != 'nt' else subprocess.run(argv, capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
    if shutil.which('pwsh'):
        for command in powershell:
            result = subprocess.run(['pwsh', '-NoProfile', '-NonInteractive', '-Command', command], capture_output=True, text=True)
            assert result.returncode == 0, result.stderr
    assert all(brain.matching_review(other, other / f'vault/Knowledge/KB-{i:03}.md') for i in [1, 2])


def links_group(work, base):
    note, reason = admit(work)
    original = note.read_text()
    note.write_text(original + '- [[Drafts/KB-002]]\n')
    holds(lambda: brain.review(work, note, 'admit', reason))
    note.write_text(original + '- [[Knowledge/KB-002]]\n')
    holds(lambda: brain.review(work, note, 'admit', reason))
    note.write_text(original)
    (work / 'vault/MOC.md').write_text('# Index\nAn unsourced answer.\n')
    holds(lambda: brain.freeze(work, 'bad-moc'))
    link = work / 'vault/Knowledge/KB-002.md'
    link.symlink_to(note)
    holds(lambda: brain.freeze(work, 'linked'))
    link.unlink()
    parent = work / 'linked-parent'
    parent.symlink_to(work / 'vault/Knowledge', target_is_directory=True)
    holds(lambda: brain.raw(parent / note.name))
    holds(lambda: brain.safe(note.with_name('kb-001.md')))
    dangling = work / 'cold/dangling'
    dangling.symlink_to(base / 'missing-directory', target_is_directory=True)
    holds(lambda: brain.freeze(work, 'dangling'))
    holds(lambda: brain.freeze(work, '../escape'))
    holds(lambda: brain.parse_note(original.replace('## Claim', '## Claim\n## Claim').encode(), 'KB-001'))


def freeze_group(work, base):
    admit(work)
    (work / 'vault/.obsidian').mkdir()
    (work / 'vault/.obsidian/workspace.json').write_text('{}')
    brain.freeze(work, 'v1')
    manifest = brain.check(work, 'v1')
    assert {f['path'] for f in manifest['files']} == {'MOC.md', 'Knowledge/KB-001.md'}
    path = work / 'cold/v1/Knowledge/KB-001.md'
    saved = path.read_bytes()
    path.write_bytes(saved + b'changed')
    holds(lambda: brain.check(work, 'v1'))
    path.write_bytes(saved)
    path.unlink()
    holds(lambda: brain.check(work, 'v1'))
    path.write_bytes(saved)
    extra = work / 'cold/v1/Knowledge/KB-002.md'
    extra.write_bytes(saved)
    holds(lambda: brain.check(work, 'v1'))
    extra.unlink()
    hidden = work / 'cold/v1/.obsidian'
    hidden.mkdir()
    secret = hidden / 'secret'
    secret.write_text('must not enter cold content')
    empty_dir = work / 'cold/v1/extra-empty'
    empty_dir.mkdir()
    error = holds(lambda: brain.check(work, 'v1'))
    assert all(str(path) in error for path in [hidden, secret, empty_dir]), error
    secret.unlink()
    hidden.rmdir()
    empty_dir.rmdir()
    brain.check(work, 'v1')


def revision_group(work, base):
    note, reason = admit(work)
    brain.freeze(work, 'v1')
    original = {p.relative_to(work).as_posix(): p.read_bytes() for p in (work / 'cold/v1').rglob('*') if p.is_file()}
    previous = work / 'identities/v1.json'
    holds(lambda: brain.freeze(work, 'unchanged', previous, 'KB-001'))
    admit(work, extra=' Qualification clarified.')
    holds(lambda: brain.freeze(work, 'wrong-focus', previous, 'KB-999'))
    brain.freeze(work, 'v2', previous, 'KB-001')
    reason.write_text('Mutable later audit text.')
    note.write_text('Mutable later work in progress.')
    (work / 'vault/.obsidian').mkdir()
    (work / 'vault/.obsidian/workspace.json').write_text('{}')
    brain.check(work, 'v1')
    brain.check(work, 'v2')
    assert all((work / p).read_bytes() == value for p, value in original.items())
    admit(work, extra=' Restored current reviewed content.')
    admit(work, 'KB-002')
    brain.freeze(work, 'v3', work / 'identities/v2.json', 'KB-002')
    brain.check(work, 'v3')
    note.unlink()
    admit(work, 'KB-002')
    holds(lambda: brain.freeze(work, 'deleted', previous, 'KB-002'))


def preserve_group(work, base):
    admit(work)
    brain.freeze(work, 'v1')
    saved = (work / 'identities/v1.json').read_bytes()
    holds(lambda: brain.freeze(work, 'v1'))
    holds(lambda: brain.initialize(work))
    assert (work / 'identities/v1.json').read_bytes() == saved
    # Real shared runner preflight, explicitly no provider key; no status echo mock.
    old_key = os.environ.pop('OPENROUTER_API_KEY', None)
    try:
        for i in range(2):
            evidence = base / f'preflight-{i}'
            code = brain.paid(work, REPO / 'shared/run_omp.py', evidence, 'ingest')
            assert code == 2 and not evidence.exists()
            assert not (work / 'reviews/ingest-attempt.json').exists()
        assert len(list((work / 'reviews').glob('ingest-preflight-*.json'))) == 2
        rule = work / 'shared/controls/SAVED_INSTRUCTION.md'
        rule.rename(rule.with_suffix('.saved'))
        evidence = base / 'missing-rule'
        assert brain.paid(work, base / 'nonexistent-runner.py', evidence, 'retrieve', 'v1') == 2
        assert not evidence.exists()
        rule.with_suffix('.saved').rename(rule)
    finally:
        if old_key is not None:
            os.environ['OPENROUTER_API_KEY'] = old_key
    # Local fault injection models an interrupted launcher, not a provider result.
    for mode in ['created', 'exception']:
        other = base / mode
        other.mkdir()
        w = prepare(other)
        runner = other / 'fault_runner.py'
        if mode == 'created':
            runner.write_text('from pathlib import Path\ndef main(argv):\n    Path(argv[argv.index("--evidence")+1]).mkdir()\n    return 2\n')
        else:
            runner.write_text('def main(argv):\n    raise RuntimeError("injected interruption")\n')
        try:
            brain.paid(w, runner, other / 'evidence', 'ingest')
        except RuntimeError:
            pass
        assert (w / 'reviews/ingest-attempt.json').is_file()
        holds(lambda: brain.paid(w, runner, other / 'retry', 'ingest'))
        assert not (other / 'retry').exists()
    # Atomic publication refuses an existing empty destination, too.
    src, dst = base / 'publish-src', base / 'publish-dst'
    src.mkdir()
    dst.mkdir()
    holds(lambda: brain.publish_directory(src, dst))
    assert src.is_dir() and dst.is_dir()


def receipt_group(work, base):
    prompt = work / 'shared/controls/INGEST_PROMPT.md'
    reads = [('read', f'DN-{i:03}.md') for i in range(1, 41)]
    good = Sealed(work, base / 'ingest', work / 'vault/Sources', prompt, reads)
    assert runtime.audit_evidence(good.evidence) == []
    brain.phase_audit(work, good.evidence, runtime, 'ingest')
    short = Sealed(work, base / 'short', work / 'vault/Sources', prompt, reads[:-1] + [reads[0]])
    assert runtime.audit_evidence(short.evidence) == []
    holds(lambda: brain.phase_audit(work, short.evidence, runtime, 'ingest'))
    original = copy.deepcopy(good.policy)
    for key, value in [('instruction', None), ('work_root', str(base)), ('prompt_sha256', '0'*64), ('profile', 'declared')]:
        good.policy = dict(original, **{key: value})
        good.seal()
        holds(lambda: brain.phase_audit(work, good.evidence, runtime, 'ingest'))
    good.policy = original
    good.seal()
    admit(work)
    brain.freeze(work, 'v1')
    manifest = brain.check(work, 'v1')
    response = cold_answers(work)
    prompt = work / 'shared/controls/RETRIEVE_PROMPT.md'
    cold = Sealed(work, base / 'cold', work / 'cold/v1', prompt, [('read', 'MOC.md'), ('read', 'Knowledge/KB-001.md'), ('absent', 'Sources/DN-014.md'), ('deny', '../../forbidden')], json.dumps(response))
    assert runtime.audit_evidence(cold.evidence) == []
    actual, states = brain.phase_audit(work, cold.evidence, runtime, 'retrieve', ('v1', manifest))
    assert states == ['EXECUTED', 'EXECUTED', 'ALLOWED_ABSENT', 'DENIED']
    assert brain.raw_access_observations(cold.guard, cold.events) == ['ALLOWED_ABSENT']
    rejected = Sealed(work, base / 'pre-hook', work / 'cold/v1', prompt,
                      [('read', 'MOC.md'), ('read', 'Knowledge/KB-001.md'),
                       ('unknown-read', '../../vault/Sources/DN-014.md'),
                       ('unknown-write', 'attempted-output.md')], json.dumps(response))
    assert runtime.audit_evidence(rejected.evidence) == []
    rejected_reads, rejected_states = brain.phase_audit(work, rejected.evidence, runtime, 'retrieve', ('v1', manifest))
    assert rejected_reads == {'MOC.md', 'Knowledge/KB-001.md'}
    assert rejected_states == ['EXECUTED', 'EXECUTED', 'DENIED', 'DENIED'], rejected_states
    assert brain.raw_access_observations(rejected.guard, rejected.events) == ['DENIED']
    calls = list(brain.attempted_calls(rejected.guard, rejected.events))
    assert calls[-2][0]['arguments'] == {'path': '../../vault/Sources/DN-014.md'}
    assert calls[-1][0]['name'] == 'course_write' and calls[-1][3] == 'DENIED'
    assert calls[-1][1] is None and calls[-2][1] is None
    assert not (work / 'cold/v1/attempted-output.md').exists()
    command_rejected = Sealed(work, base / 'pre-hook-command', work / 'cold/v1', prompt,
                              [('read', 'MOC.md'), ('read', 'Knowledge/KB-001.md'),
                               ('unknown-bash', '../../vault/Sources/DN-014.md')], json.dumps(response))
    arguments = list(brain.attempted_calls(command_rejected.guard, command_rejected.events))[-1][0]['arguments']
    for request, expected in [
        ({'command': 'cat ../../vault/Sources/DN-014.md'}, ['DENIED']),
        ({'request': {'argv': ['cat', 'Sources/DN-014.md']}, 'timeout': 3, 'stdin': None}, ['DENIED']),
        ({'command': 'cat Knowledge/KB-001.md'}, ['NOT_ATTEMPTED']),
    ]:
        arguments.clear()
        arguments.update(request)
        command_rejected.seal()
        assert runtime.audit_evidence(command_rejected.evidence) == []
        _, command_states = brain.phase_audit(work, command_rejected.evidence, runtime, 'retrieve', ('v1', manifest))
        assert command_states == ['EXECUTED', 'EXECUTED', 'DENIED']
        observed = brain.raw_access_observations(command_rejected.guard, command_rejected.events)
        assert observed == expected, (request, expected, observed)
    # Missing decision is not a license to relabel an invalid receipt as denial.
    broken = copy.deepcopy(rejected.events)
    for row in rejected.events:
        if row['type'] == 'tool_execution_end' and row['toolCallId'] == 'call-2':
            row['isError'] = False
    rejected.seal()
    errors = runtime.audit_evidence(rejected.evidence)
    assert errors
    error = holds(lambda: brain.phase_audit(work, rejected.evidence, runtime, 'retrieve', ('v1', manifest)))
    assert all(item in error for item in errors), error
    rejected.events = broken
    rejected.seal()
    cold_original = copy.deepcopy(cold.policy)
    for key, value in [('instruction', None), ('work_root', str(work / 'vault')), ('prompt_sha256', '0'*64), ('tools', ['course_read', 'course_write'])]:
        cold.policy = dict(cold_original, **{key: value})
        cold.seal()
        holds(lambda: brain.phase_audit(work, cold.evidence, runtime, 'retrieve', ('v1', manifest)))
    cold.policy = cold_original
    cold.seal()
    brain.answers(work, 'v1', manifest, actual, json.dumps(response))
    brain.answers(work, 'v1', manifest, actual, json.dumps(cold_answers(work, 'unsupported')))
    for change in ['unread', 'dn', 'excerpt', 'uncited', 'duplicate']:
        wrong = copy.deepcopy(response)
        citation = wrong['answers'][0]['citations'][0]
        if change == 'unread': citation['note_id'] = 'KB-002'
        if change == 'dn': citation['source_id'] = 'DN-014'
        if change == 'excerpt': citation['excerpt'] = 'invented quote'
        if change == 'uncited': wrong['answers'][0]['citations'] = []
        if change == 'duplicate': wrong['answers'][1]['question_id'] = 'Q1'
        holds(lambda: brain.answers(work, 'v1', manifest, actual, json.dumps(wrong)))
    for name, actions in [('no-moc', [('read', 'Knowledge/KB-001.md')]), ('none', [])]:
        attempt = Sealed(work, base / name, work / 'cold/v1', prompt, actions)
        assert runtime.audit_evidence(attempt.evidence) == []
        holds(lambda: brain.phase_audit(work, attempt.evidence, runtime, 'retrieve', ('v1', manifest)))
    # Test the no-call classification independently of the required MOC condition:
    # an ingest audit cannot succeed without reads, so no successful phase claims denial.
    assert not any(r['type'] == 'decision' for r in attempt.guard)
    assert brain.raw_access_observations(attempt.guard, attempt.events) == ['NOT_ATTEMPTED']
    for label, actions, expected in [
        ('raw-denied', [('deny', '../../vault/Sources/DN-014.md')], ['DENIED']),
        ('raw-executed', [('read', 'DN-014.md')], ['EXECUTED']),
    ]:
        root = work / 'vault/Sources' if label == 'raw-executed' else work / 'cold/v1'
        observed = Sealed(work, base / label, root, prompt, actions)
        assert runtime.audit_evidence(observed.evidence) == []
        assert brain.raw_access_observations(observed.guard, observed.events) == expected
    admit(work, extra=' Revised qualification.')
    brain.freeze(work, 'v2', work / 'identities/v1.json', 'KB-001')
    second = brain.check(work, 'v2')
    holds(lambda: brain.answers(work, 'v2', second, actual, json.dumps(cold_answers(work, 'unsupported'))))
    brain.answers(work, 'v2', second, actual, json.dumps(response))
    (cold.evidence / 'response.md').write_text('substituted capture')
    holds(lambda: brain.phase_audit(work, cold.evidence, runtime, 'retrieve', ('v1', manifest)))


GROUPS = {'M2-GUARD': guard_group, 'M2-SOURCE': source_group, 'M2-REVIEW': review_group, 'M2-LINKS': links_group, 'M2-FREEZE': freeze_group, 'M2-REVISION': revision_group, 'M2-PRESERVE': preserve_group, 'M2-RECEIPT': receipt_group}


def main():
    failed = 0
    for cid, action in GROUPS.items():
        with tempfile.TemporaryDirectory(prefix='module02-oracle-') as directory:
            base = Path(directory).resolve()
            try:
                work = prepare(base)
            except Exception as error:
                print(f'ERROR {cid}: setup failed: {error!r}')
                return 2
            try:
                action(work, base)
                print(f'  PASS {cid}: behavioral boundaries')
            except AssertionError as error:
                failed += 1
                print(f'  FAIL {cid}: {error}')
            except Exception as error:
                # Setup/import/runtime crashes do not count as killed mutations.
                print(f'ERROR {cid}: unexpected exception: {error!r}')
                return 2
    print(f'FAIL {failed}')
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
