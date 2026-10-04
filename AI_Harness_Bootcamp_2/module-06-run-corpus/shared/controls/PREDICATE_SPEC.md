# Predicate spec

You configure this check. You don't write a second checker.

The input is one run file. The config is a JSON object with one key, `all_present`. That value is a list of exactly two different strings, and neither string may be empty. Any other shape is a hold: an empty list, a repeated string, an extra key, or a file that isn't JSON. The check prints `HOLD: malformed config` and does not decide the run.

A literal is one of those two strings, matched as written. Capitals and lowercase are different. The check doesn't use pattern rules, and it doesn't treat the strings as formulas. It only asks whether each string occurs somewhere in the file. A string inside a longer word still counts.

If both strings are present, the process exits 1 and prints `MATCH: both literals present`. If either string is missing, the process exits 0 and prints `PASS: at least one literal absent`. A missing run file exits 1 and prints `HOLD: missing input`. That missing-input line is only for the run file. A bad config uses the malformed-config line instead.

This is a text check, not a release decision. The characters `RELEASED` occur inside `UNRELEASED`, so a config that uses `RELEASED` also matches a hold stamp written as `UNRELEASED`. Measure that limit. Don't treat a match as proof that quality released a cylinder.
