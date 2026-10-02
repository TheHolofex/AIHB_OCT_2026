#!/usr/bin/env python3
"""Public-site boundary regressions using isolated authored test courses."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("course_build", ROOT / "scripts/build_course.py")
builder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = builder
SPEC.loader.exec_module(builder)

PROCEDURE = """# Example

## Read a file

Read the supplied source before deciding what it supports.

**Terminal: Bash or zsh, ordinary user.**

```bash
printf '%s\\n' 'a < b & c'
```

**Expected:** You see the literal comparison text.

```text
a < b & c
```

**Stop:** If the command fails, keep the error. **Recovery:** Correct the path and rerun.

[Input file](shared/case/SOURCE.md)

| Field | Meaning |
|:---|---:|
| state | An observed state. |
"""

GUIDED_PROCEDURE = PROCEDURE + """

<details class="rf-stretch" markdown="1">
<summary>Optional stretch: inspect a second source</summary>

## Compare the second source

This is optional authored lesson prose, not raw case data.

<details><summary>Figure text</summary><p>The source and claim stay separate.</p></details>

</details>

The continuation remains outside the optional disclosure.

## Preserve the decision

Keep the unsupported claim unresolved.
"""


class PublicationBehavior(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="course-publish-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        boot = self.root / "AI_Harness_Bootcamp_2"
        boot.mkdir()
        self.course = {"schema_version": 1, "course_id": "AI_Harness_Bootcamp_2", "source_root": "AI_Harness_Bootcamp_2", "site_dir": "site", "index": {"source": "README.md", "dest": "index.html", "kind": "home"}, "modules": [], "shared_downloads": []}
        (self.root / "ui").mkdir()
        self.course["ui_assets"] = []
        for name, content in {
            "course.css": "body { background-image: url('texture.svg'); }\n",
            "course.js": "'use strict';\n",
            "theme-init.js": "'use strict';\n",
            "texture.svg": '<svg xmlns="http://www.w3.org/2000/svg" width="1" height="1"></svg>\n',
        }.items():
            (self.root / "ui" / name).write_text(content, encoding="utf-8")
            self.course["ui_assets"].append({"source": f"ui/{name}", "dest": f"assets/{name}"})
        links = []
        for i in range(10):
            directory = f"module-{i:02d}-example"
            module = boot / directory
            (module / "shared/case").mkdir(parents=True)
            (module / "shared/case/SOURCE.md").write_text("# Authored test input\nRAW_CASE_SENTINEL_8f341\n", encoding="utf-8")
            (module / "README.md").write_text(PROCEDURE, encoding="utf-8")
            links.append(f"[Assignment {i}]({directory}/README.md)")
            pages = [{"source": "README.md", "dest": "README.html", "kind": "overview"}]
            (module / "lab.md").write_text(GUIDED_PROCEDURE, encoding="utf-8")
            pages.append({"source": "lab.md", "dest": "lab.html", "kind": "lab", "guide": {"context_sections": [], "optional_sections": []}})
            self.course["modules"].append({"id": f"{i:02d}", "directory": directory, "title": "Example", "case_name": f"Example {i}", "summary": "Inspect the supplied evidence.", "nav_summary": "Terminal · Source inspection", "pages": pages, "download_dirs": ["shared/case"]})
        (boot / "README.md").write_text("# Synthetic publication test\n\nInspect the supplied course.\n\n## Choose your assignment\n\n<div data-course-map></div>\n\n" + "\n\n".join(links), encoding="utf-8")
        self.save_manifest()
        self.page = boot / "module-00-example/README.md"
        self.published = self.root / "site/AI_Harness_Bootcamp_2/module-00-example/README.html"

    def save_manifest(self):
        (self.root / "course.json").write_text(json.dumps(self.course), encoding="utf-8")

    def build(self, check=False):
        with contextlib.redirect_stdout(io.StringIO()):
            return builder.build(self.root, check)

    def test_rendered_links_raw_inputs_commands_and_accessible_tables(self):
        self.build()
        document = self.published.read_text(encoding="utf-8")
        tree = builder.parse_html(document)
        commands = [node for node in tree.walk() if "data-command" in node.attrs]
        self.assertEqual([node.text() for node in commands], ["printf '%s\\n' 'a < b & c'\n"])
        self.assertIn('href="shared/case/SOURCE.md"', document)
        self.assertIn('href="AI_Harness_Bootcamp_2/module-00-example/README.html"', (self.root / "site/index.html").read_text())
        self.assertEqual(len([node for node in tree.walk() if node.tag == "caption"]), 1)
        self.assertTrue(all(node.attrs.get("scope") == "col" for node in tree.walk() if node.tag == "th"))
        self.assertEqual(self.build(check=True), 0)

    def test_check_missing_site_and_raw_tampering_fail_without_writing(self):
        with self.assertRaises(ValueError):
            self.build(check=True)
        self.assertFalse((self.root / "site").exists())
        self.build()
        raw = self.published.parent / "shared/case/SOURCE.md"
        raw.write_text("tampered", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.build(check=True)
        self.assertEqual(raw.read_text(), "tampered")

    def test_duplicate_destinations_and_escaping_paths_fail(self):
        self.course["modules"][0]["pages"].append({"source": "README.md", "dest": "README.html", "kind": "reference"})
        self.save_manifest()
        with self.assertRaises(ValueError):
            self.build()
        self.assertFalse((self.root / "site").exists())
        for path in ("../outside", "/outside", "C:thing", "a\\b"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                builder.safe_relative(path)

    def test_unlisted_staff_links_and_active_html_fail_before_publication(self):
        for addition in ("\n[Staff](reference/REFERENCE.md)\n", "\n<script>alert('unsafe')</script>\n", '\n<img src="shared/case/SOURCE.md" onerror="alert(1)">\n'):
            with self.subTest(addition=addition):
                self.page.write_text(PROCEDURE + addition, encoding="utf-8")
                with self.assertRaises(ValueError):
                    self.build()
                self.assertFalse((self.root / "site").exists())

    def test_each_command_needs_its_own_terminal_and_later_observation(self):
        variants = [PROCEDURE.replace("```bash", "```", 1), PROCEDURE.replace("**Terminal: Bash or zsh, ordinary user.**", "**Bash**"), PROCEDURE + "\n## Another action\n\n**Terminal: Bash, ordinary user.**\n\n```bash\nprintf forgotten\n```\n"]
        for text in variants:
            with self.subTest(text=text):
                self.page.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    self.build()

    def test_broken_anchor_and_unlisted_output_are_rejected(self):
        self.page.write_text(PROCEDURE + "\n[Missing](#missing)\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.build()
        self.page.write_text(PROCEDURE, encoding="utf-8")
        self.build()
        stray = self.root / "site/private.txt"
        stray.write_text("preserve me", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.build()
        self.assertEqual(stray.read_text(), "preserve me")

    def test_symlinked_data_cannot_escape_the_public_allowlist(self):
        outside = self.root / "outside-secret.txt"
        outside.write_text("secret", encoding="utf-8")
        (self.page.parent / "shared/case/link.txt").symlink_to(outside)
        with self.assertRaises(ValueError):
            self.build()
        self.assertFalse((self.root / "site").exists())

    def test_ui_dependencies_resolve_at_root_and_prefix_mounts(self):
        from urllib.parse import urljoin
        self.build()
        for path in ("index.html", "AI_Harness_Bootcamp_2/module-00-example/lab.html"):
            tree = builder.parse_html((self.root / "site" / path).read_text())
            data = json.loads(next(node.text() for node in tree.walk() if node.attrs.get("id") == "rf-page-data"))
            assets = [node.attrs.get("href", node.attrs.get("src")) for node in tree.walk() if node.tag in {"link", "script"} and ("src" in node.attrs or "href" in node.attrs)]
            for prefix in ("/", "/reformation/site/"):
                base = "https://example.test" + prefix
                for value in assets:
                    self.assertTrue(urljoin(base + path, value).startswith(base + "assets/"))
                self.assertEqual(urljoin(base + path, data["root"] + "assets/search-index.json"), base + "assets/search-index.json")
                self.assertTrue(all(urljoin(base, item["overview"]).startswith(base) for item in data["modules"]))

    def test_invalid_ui_sources_fail_before_writing(self):
        entry = self.course["ui_assets"][0]
        original = entry["source"]
        for source in ("ui/missing.css", "../outside.css", "staff/private.css"):
            with self.subTest(source=source):
                entry["source"] = source
                self.save_manifest()
                with self.assertRaises(ValueError):
                    self.build()
                self.assertFalse((self.root / "site").exists())
        entry["source"] = original
        (self.root / original).unlink()
        (self.root / original).symlink_to(self.root / "ui/theme-init.js")
        self.save_manifest()
        with self.assertRaises(ValueError):
            self.build()
        self.assertFalse((self.root / "site").exists())

    def test_missing_or_network_css_dependencies_are_rejected(self):
        for value in ("missing.svg", "../../outside.svg", "https://example.test/texture.svg", "//example.test/font.woff2"):
            with self.subTest(value=value):
                (self.root / "ui/course.css").write_text(f"body {{ background: url('{value}'); }}")
                with self.assertRaises(ValueError):
                    self.build()
                self.assertFalse((self.root / "site").exists())

    def test_guided_groups_keep_commands_context_fragments_and_optional_boundaries(self):
        self.build()
        original = builder.parse_html(builder.markdown.markdown(
            GUIDED_PROCEDURE, extensions=["fenced_code", "tables", "toc", "md_in_html"],
            extension_configs={"tables": {"use_align_attribute": True}},
        ))
        original_ids = {node.attrs["id"] for node in original.walk() if "id" in node.attrs}
        tree = builder.parse_html((self.published.parent / "lab.html").read_text())
        nodes = list(tree.walk())
        self.assertTrue(original_ids.issubset({node.attrs["id"] for node in nodes if "id" in node.attrs}))
        steps = [node for node in nodes if "data-step-id" in node.attrs]
        self.assertEqual([node.attrs["data-step-id"] for node in steps], ["read-a-file", "preserve-the-decision"])
        first = list(steps[0].walk())
        self.assertEqual([node.text() for node in first if "data-command" in node.attrs], ["printf '%s\\n' 'a < b & c'\n"])
        self.assertEqual([node.text() for node in first if node.tag == "p" and node.text().startswith(("Terminal:", "Expected:", "Stop:"))], [
            "Terminal: Bash or zsh, ordinary user.",
            "Expected: You see the literal comparison text.",
            "Stop: If the command fails, keep the error. Recovery: Correct the path and rerun.",
        ])
        stretch = next(node for node in nodes if "rf-stretch" in node.attrs.get("class", "").split())
        self.assertFalse(any("data-step-id" in node.attrs for node in stretch.walk()))
        self.assertNotIn("The continuation remains", stretch.text())
        self.assertTrue(all("hidden" not in node.attrs for step in steps for node in step.walk()))
        data = json.loads(next(node.text() for node in nodes if node.attrs.get("id") == "rf-page-data"))
        self.assertEqual([step["id"] for step in data["steps"]], ["read-a-file", "preserve-the-decision"])

    def test_orphaned_commands_and_invalid_guide_anchors_are_rejected(self):
        lab = self.page.parent / "lab.md"
        lab.write_text(GUIDED_PROCEDURE.replace("## Read a file", "Read a file", 1))
        with self.assertRaises(ValueError):
            self.build()
        lab.write_text(GUIDED_PROCEDURE)
        guide = self.course["modules"][0]["pages"][1]["guide"]
        for anchors in (["missing"], ["read-a-file", "read-a-file"]):
            guide["context_sections"] = anchors
            self.save_manifest()
            with self.assertRaises(ValueError):
                self.build()
        self.assertFalse((self.root / "site").exists())

    def test_search_contains_lesson_prose_not_raw_private_or_fenced_bytes(self):
        (self.root / "staff").mkdir()
        (self.root / "staff/private.md").write_text("PRIVATE_SENTINEL_d839c")
        self.build()
        text = (self.root / "site/assets/search-index.json").read_text()
        index = json.loads(text)
        self.assertIn("Read the supplied source before deciding what it supports.", text)
        self.assertNotIn("RAW_CASE_SENTINEL_8f341", text)
        self.assertNotIn("PRIVATE_SENTINEL_d839c", text)
        self.assertNotIn("printf", text)
        self.assertNotIn("a < b & c", text)
        page = next(page for page in index["pages"] if page["path"].endswith("module-00-example/lab.html"))
        optional = next(section for section in page["sections"] if section["id"] == "compare-the-second-source")
        self.assertTrue(optional["optional"])
        self.assertEqual(sum(section["text"].count("This is optional authored lesson prose") for section in page["sections"]), 1)
        self.assertEqual({page["path"] for page in index["pages"]}, {p.relative_to(self.root / "site").as_posix() for p in (self.root / "site").rglob("*.html")})

    def test_generated_search_and_style_tampering_fail_without_writing(self):
        self.build()
        for relative in ("assets/search-index.json", "assets/course.css"):
            path = self.root / "site" / relative
            original = path.read_bytes()
            path.write_bytes(b"tampered generated asset")
            with self.assertRaises(ValueError):
                self.build(check=True)
            self.assertEqual(path.read_bytes(), b"tampered generated asset")
            path.write_bytes(original)

    def test_page_metadata_contract_rejects_missing_roles_and_home_placeholders(self):
        self.course["modules"][0]["case_name"] = ""
        self.save_manifest()
        with self.assertRaises(ValueError):
            self.build()
        self.course["modules"][0]["case_name"] = "Example"
        self.course["modules"][0]["pages"][1]["kind"] = "reference"
        self.save_manifest()
        with self.assertRaises(ValueError):
            self.build()
        self.course["modules"][0]["pages"][1]["kind"] = "lab"
        self.save_manifest()
        home = self.root / "AI_Harness_Bootcamp_2/README.md"
        original = home.read_text()
        for text in (original.replace("<div data-course-map></div>", ""), original + "\n<div data-course-map></div>\n"):
            home.write_text(text)
            with self.assertRaises(ValueError):
                self.build()
        self.assertFalse((self.root / "site").exists())


if __name__ == "__main__":
    unittest.main()
