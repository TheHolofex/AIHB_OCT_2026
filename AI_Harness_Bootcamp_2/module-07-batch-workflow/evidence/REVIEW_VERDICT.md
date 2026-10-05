# Module 07 review verdict

**Historical numbering:** Previously titled "Module 6 verdict" in early records (body, date 2026-08-23, commands, retired Python section, native n8n cutover 2026-10-02, and all outcomes preserved unchanged as historical evidence).

The 2026-08-23 record below describes the retired Python implementation. Its commands and review results are historical, not current verification. See [Native n8n cutover](#native-n8n-cutover--2026-10-02) for the replacement evidence.

**Date:** 2026-08-23
**Standard:** `reference/REFERENCE.md`, SHA-256 recorded in `reference/REFERENCE.sha256`
**Amendments:** none. Reference frozen 2026-08-23.

## Executable evidence

| Evidence | Command | Result file |
|---|---|---|
| Acceptance oracle | `python3 tests/test_module_06.py` | `evidence/oracle-final.txt` |
| Oracle adequacy | `python3 tests/test_adequacy.py` | `evidence/adequacy-final.txt` |
| Restore | `python3 scripts/restore_rule.py` | `RESTORE OK`, baseline receipts |

## Prose panel

Language-model seats. **Class F / human panel is UNMEASURED.**

| File | Seat | Total |
|---|---|---|
| `reviews/round-1-technical.md` | Technical | 32/40 REJECT |
| `reviews/round-1-curriculum.md` | Curriculum | 30/40 REJECT |
| `reviews/round-1-adversarial.md` | Adversarial | 31/40 REJECT |
| `reviews/round-1-voice.md` | Voice | 90/100 human craft, 6/100 AI mannerisms REJECT |

## Decision

**Accepted as a reviewed implementation package, ready for a controlled pilot with a facilitator present.** Not accepted as a measured learner experience.

## Native n8n cutover — 2026-10-02

**Contract:** `reference/REFERENCE.md` revision 3 and its frozen digest. The setup prerequisite is governed by Module 0 reference v5. Historical receipts, reviews and verdicts above are retained; they do not establish native n8n behavior.

**Runtime:** n8n 2.41.5 on Apple Silicon Docker Desktop, using the approved isolated `white-rack-course` project and the full six-service official stack. The editor was bound to `127.0.0.1:5678`; the sandbox API was healthy and the certificate service exited successfully. Local owner access, a blank workflow saved through reload, and persistence after non-destructive down/up were observed. The exact authored macOS `course_n8n` helper subsequently reported the expected services, loopback binding and version.

### Native execution evidence

`native/runtime-proof.json` records controls, hashes, observations and execution IDs. Eight downloaded CSV receipts and 24 independently downloaded checker reports are retained beside it. Staff router exports and frozen deltas live under `reference/native/`. These files are excluded from public publication; they are not secret from repository readers.

| Operation | Native executions | Observed result |
|---|---|---|
| Original export identity | 64, recheck 72 | The unchanged original export retained SHA-256 `3d02aef9cb8da98a61e992609375fd91b0fc5d8b7d9e903e9f681f354ccc67df` |
| Both core baselines | Routers 65–66; checker 67 | Both receipts contain 80 rows and are byte-identical; SHA-256 `ee45d45acb05cd269877ee71d29db07187b2804d6e6fb7fb06bc71956f630027` |
| Predicted policy change | Routers 68–69; checkers 70–71 | Only LW-12, LW-28 and LW-41 change; 77 rows stay unchanged in each wave; rack claimants LW-19 and LW-55 remain held |
| Restore into a new blank workflow | Routers 76–77; checkers 78–79 | Both restored receipts match the corresponding original files byte-for-byte |
| Revised-wave input/policy separation | Routers 80–81; checkers 82–83 | Input-only changes: LW-12/LW-44/LW-60. Policy-only changes: LW-28/LW-41/LW-44/LW-60 |
| Invalid input/policy | 84–94, 99 | Empty/malformed/duplicate/extra-column/control-character inputs and invalid policy fail before a routing receipt |
| Empty routes | 95–98 | Each empty-route case retains the exact expected records and source order, without a fabricated row |
| Checker negatives | 100–112, 114 | Wrong schema/order/count/serialization, invalid UTF-8/CSV, incorrect or omitted delta, unpredicted changes and baseline-export replacement produce HOLD |
| Empty predicted delta | 113 | Header-only delta with identical receipts passes |

Native rehearsal found two validator gaps: a source-supplied `pending_status` could be overwritten before checking, and a lot ID containing an ASCII control character could diverge during serialization. The supplied validator now compares the original `Read CSV` records with the augmented records and rejects those inputs. The final native boundary runs above exercise the corrected control.

### Publication and command evidence

- The learner constructs the 13-node router from a blank canvas; only the independent six-node checker is imported. Module 6 does not use the retired Python router or a paid OMP/provider execution path.
- Forty authentic n8n PNG captures illustrate all 35 numbered construction/operation steps. The public allowlist contains those figures and five browser exercise inputs, not a complete router export, answer deltas, contract, or staff evidence.
- `node --test AI_Harness_Bootcamp_2/module-06-batch-workflow/tests/test_controls.mjs` passed as part of `.venv/bin/python scripts/check_course.py`. The complete redacted transcript is `native/course-gates.txt`: all 27 scoped gates passed.
- `.venv/bin/python scripts/build_course.py` and `--check` passed: 32 instructional pages, 692 raw downloads, 38 UI/generated assets. Both passed again after the final save-link instruction. The raw-download count includes figures, not just exercise inputs.
- All 206 authored Bash/PowerShell blocks across the five setup routes passed 322 parser invocations. All 216 controlled host-shell checks passed for project collision detection, preservation of existing files/symlinks, inspection failure, explicit Compose arguments and refusal of exported overrides, including empty values. Per-case results are in `native/runtime-proof.json`; Docker was stubbed for these boundary checks.
- Chromium exercised Overview/Lab navigation, Guided/Full modes, Dark/Sand, the mobile course menu, image-dialog focus/Escape, no-JavaScript full-size links, print-state restoration and `/course-preview/` publication. All five setup pages had no document-width overflow at 1440 or 390 CSS pixels. Each of the five served inputs matched its source bytes; sampled staff and retired Python URLs returned 404.

### Limits and decision

Direct course-page screenshot capture timed out in the browser tooling. Real Chromium screen-media PDF renders at wide/narrow sizes and a print-media PDF succeeded, were rasterized and visually inspected, and remain outside the checkout with the capture-failure record. They are PDF renders, not screenshots. This does not replace the 40 genuine n8n captures shipped with the lab.

PowerShell parsing used PowerShell 7 on macOS, not Windows PowerShell 5.1. The host-shell matrix is not native Windows, WSL, Ubuntu or Arch execution. Native n8n behavior was observed only on Apple Silicon Docker Desktop. Human completion time, independent nondeveloper performance and assistive-technology behavior remain unmeasured. No hosted deployment or paid readiness check is asserted here.

The cutover is implemented and the native routing, evidence-control and publication paths above passed their exercised checks. Retain the isolated runtime and original evidence; do not describe this as five-platform native verification or measured learner mastery.
