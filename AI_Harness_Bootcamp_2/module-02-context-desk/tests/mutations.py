#!/usr/bin/env python3
"""Applied behavioral defects in disposable module copies only."""
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class Mutation:
    cid: str
    what: str
    apply: Callable[[Path], None]


def replace(old, new, relative='scripts/second_brain.py'):
    def apply(root):
        path = root / relative
        value = path.read_text()
        if value.count(old) != 1:
            raise AssertionError(f'mutation target must occur once: {old!r}')
        path.write_text(value.replace(old, new))
    return apply


MUTATIONS = [
    Mutation('M2-GUARD', 'accept hostile screened input', replace('return 0 if ok else 1', 'return 0', 'shared/case/guard.py')),
    Mutation('M2-SOURCE', 'trust changed source copy', replace("require(not changed, 'source identity changed/added/missing: ' + ', '.join(str(root / p) for p in changed) + '\\n' + '\\n'.join(originals))", "require(True, 'source identity changed/added/missing: ' + ', '.join(str(root / p) for p in changed) + '\\n' + '\\n'.join(originals))")),
    Mutation('M2-REVIEW', 'accept substituted immutable reason', replace("require(receipt['reason_text'].strip() and digest(receipt['reason_text'].encode()) == receipt['reason_sha256'], 'immutable review reason differs')", "require(True, 'immutable review reason differs')")),
    Mutation('M2-LINKS', 'admit dangling Knowledge relationship', replace("require(safe(work / 'vault/Knowledge' / (target + '.md')).is_file(), f'{path.name}: missing Knowledge/{target}.md')", "require(True, f'{path.name}: missing Knowledge/{target}.md')")),
    Mutation('M2-FREEZE', 'return success on snapshot mismatch', replace("raise ValueError('snapshot changed/added/missing: ' + ', '.join(bad))", 'return manifest')),
    Mutation('M2-REVISION', 'allow unchanged focal content', replace("require(f'Knowledge/{focus}.md' in changed, 'focus_note must be a changed or new Knowledge note')", "require(True, 'focus_note must be a changed or new Knowledge note')")),
    Mutation('M2-PRESERVE', 'consume recoverable no-provider preflight reservation', replace('        marker.unlink()', '        pass  # defective reservation retention')),
    Mutation('M2-RECEIPT', 'count duplicate reads as packet coverage', replace("require(reads == {n + '.md' for n in DN}, 'ingest must read forty distinct DN files')", "require(True, 'ingest must read forty distinct DN files')")),
]
