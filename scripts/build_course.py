#!/usr/bin/env python3
"""Publish the allowlisted Reformation course; --check never writes."""
from __future__ import annotations

import argparse
import html
import json
import os
import posixpath
import re
import sys
from dataclasses import dataclass, field
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote, urlsplit, urlunsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
BLOCKED_PARTS = {"staff", "facilitator", "reference", "reviews", "review", "history", "evidence", "tests", "work", "__pycache__", ".git", "graded", "answer-keys", "answers"}
SAFE_TAGS = set("a p h1 h2 h3 h4 h5 h6 ul ol li em strong code pre blockquote table caption thead tbody tr th td details summary img hr br div span dl dt dd sup sub del input".split())
VOID_TAGS = {"img", "hr", "br", "input", "meta", "link"}
COMMAND_LANGUAGES = {"bash", "sh", "zsh", "powershell"}
PAGE_KINDS = {"home", "overview", "lab", "setup", "reference"}
UI_SUFFIXES = {".css", ".js", ".woff2", ".txt", ".svg", ".webp"}
SEARCH_PATH = PurePosixPath("assets/search-index.json")


@dataclass
class Node:
    tag: str
    attrs: dict[str, str] = field(default_factory=dict)
    children: list[Node | str] = field(default_factory=list)

    def text(self) -> str:
        return "".join(child.text() if isinstance(child, Node) else child for child in self.children)

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.walk()

    def render(self) -> str:
        if not self.tag:
            return "".join(child.render() if isinstance(child, Node) else html.escape(child, quote=False) for child in self.children)
        attrs = "".join(f' {key}="{html.escape(value, quote=True)}"' for key, value in self.attrs.items())
        if self.tag in VOID_TAGS:
            return f"<{self.tag}{attrs}>"
        inner = "".join(child.render() if isinstance(child, Node) else html.escape(child, quote=False) for child in self.children)
        return f"<{self.tag}{attrs}>{inner}</{self.tag}>"


class TreeParser(HTMLParser):
    def __init__(self, safe_fragment: bool = False):
        super().__init__(convert_charrefs=True)
        self.root = Node("")
        self.stack = [self.root]
        self.safe_fragment = safe_fragment

    def handle_starttag(self, tag, attrs):
        if self.safe_fragment and tag not in SAFE_TAGS:
            raise ValueError(f"active or unsupported HTML element: {tag}")
        attributes = dict((key, value or "") for key, value in attrs)
        if len(attributes) != len(attrs):
            raise ValueError("duplicate HTML attribute")
        for key, value in attributes.items():
            if key.lower().startswith("on") or key in {"srcdoc", "formaction", "style"}:
                raise ValueError(f"active HTML attribute: {key}")
            if key in {"href", "src"} and urlsplit(value).scheme.lower() not in {"", "https", "http", "mailto"}:
                raise ValueError(f"unsafe link scheme: {value}")
        node = Node(tag, attributes)
        self.stack[-1].children.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        if len(self.stack) == 1 or self.stack[-1].tag != tag:
            raise ValueError(f"unbalanced HTML closing tag: {tag}")
        self.stack.pop()

    def handle_data(self, data):
        self.stack[-1].children.append(data)

    def finish(self) -> Node:
        self.close()
        if len(self.stack) != 1:
            raise ValueError(f"unclosed HTML element: {self.stack[-1].tag}")
        return self.root


def parse_html(text: str, safe_fragment=False) -> Node:
    parser = TreeParser(safe_fragment)
    parser.feed(text)
    return parser.finish()


def safe_relative(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value or "\0" in value or ":" in value:
        raise ValueError(f"invalid manifest path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"..", "."} for part in value.split("/")):
        raise ValueError(f"escaping manifest path: {value}")
    return path


def source_path(base: Path, rel: str) -> Path:
    path = base / safe_relative(rel)
    if any(part.lower() in BLOCKED_PARTS or part.startswith(".") for part in Path(rel).parts):
        raise ValueError(f"staff or hidden source cannot be published: {rel}")
    if path.name in {"CUSTODY_CONTRACT.md", "spec.json"} or path.name.lower().startswith(("answer-key", "graded-")):
        raise ValueError(f"staff source cannot be published: {rel}")
    current = path
    while current != base:
        if current.is_symlink():
            raise ValueError(f"symlink source cannot be published: {path}")
        current = current.parent
    if not path.is_file():
        raise ValueError(f"missing publication source: {path}")
    return path


def inventory(root: Path) -> tuple[dict, dict[PurePosixPath, Path], dict[Path, PurePosixPath], set[Path]]:
    course = json.loads((root / "course.json").read_text(encoding="utf-8"))
    modules = course.get("modules", [])
    if [module.get("id") for module in modules] != [f"{i:02d}" for i in range(10)]:
        raise ValueError("manifest must enumerate exactly ten modules in order, 00–09")
    if course.get("schema_version") != 1 or course.get("site_dir") != "site" or course.get("course_id") != "AI_Harness_Bootcamp_2":
        raise ValueError("unsupported course manifest identity")
    boot = root / safe_relative(course["source_root"])
    if boot.resolve() != root.resolve() / "AI_Harness_Bootcamp_2" or boot.is_symlink():
        raise ValueError("source_root must be the Reformation module tree")
    destinations: dict[PurePosixPath, Path] = {}
    sources: dict[Path, PurePosixPath] = {}
    pages: set[Path] = set()

    def add(base: Path, src: str, dest: str, page: bool = False):
        source = source_path(base, src)
        target = safe_relative(dest)
        if any(part.lower() in BLOCKED_PARTS for part in target.parts):
            raise ValueError(f"staff destination: {target}")
        if target == SEARCH_PATH:
            raise ValueError("search index is a reserved generated destination")
        if target in destinations:
            raise ValueError(f"duplicate publication destination: {target}")
        if source in sources:
            raise ValueError(f"duplicate publication source: {source}")
        if not page and source.suffix.lower() in {".html", ".htm", ".pyc"}:
            raise ValueError(f"untrusted or generated raw artifact cannot be published: {source}")
        destinations[target] = source
        sources[source] = target
        if page:
            if source.suffix != ".md" or target.suffix != ".html":
                raise ValueError(f"instructional page must map Markdown to HTML: {source}")
            pages.add(source)

    if course["index"].get("kind") != "home":
        raise ValueError("index must be the home page")
    if "guide" in course["index"]:
        raise ValueError("home cannot define a guide")
    add(boot, course["index"]["source"], course["index"]["dest"], True)
    for module in modules:
        directory = module["directory"]
        if any(not isinstance(module.get(key), str) or not module[key].strip() for key in ("title", "case_name", "summary", "nav_summary")):
            raise ValueError("module display fields must be nonempty strings")
        kinds = [page.get("kind") for page in module["pages"]]
        if any(kind not in PAGE_KINDS - {"home"} for kind in kinds):
            raise ValueError("unrecognized instructional page kind")
        if any(kinds.count(kind) != 1 for kind in ("overview", "lab")):
            raise ValueError("each module needs one overview and lab page")
        safe_relative(directory)
        if not re.fullmatch(rf"module-{module['id']}-[a-z0-9-]+", directory):
            raise ValueError(f"module ID/directory mismatch: {directory}")
        base = boot / directory
        prefix = PurePosixPath(course["course_id"]) / directory
        for page in module["pages"]:
            guide = page.get("guide")
            if page["kind"] == "lab":
                if not isinstance(guide, dict) or set(guide) != {"context_sections", "optional_sections"}:
                    raise ValueError("lab guide must declare context_sections and optional_sections")
                anchors = []
                for values in guide.values():
                    if not isinstance(values, list) or any(not isinstance(value, str) or not value for value in values):
                        raise ValueError("guide sections must be lists of nonempty anchors")
                    anchors.extend(values)
                if len(anchors) != len(set(anchors)):
                    raise ValueError("guide anchors must be unique and disjoint")
            elif page["kind"] == "setup":
                if guide != {}:
                    raise ValueError("setup requires an empty guide object")
            elif "guide" in page:
                raise ValueError("only lab and setup pages may define a guide")
            add(base, page["source"], str(prefix / page["dest"]), True)
        for kind in ("figures", "scripts"):
            for entry in module.get(kind, []):
                add(base, entry["source"], str(prefix / entry["dest"]))
        for relative in module.get("raw_downloads", []):
            add(base, relative, str(prefix / relative))
        for relative in module.get("download_dirs", []):
            folder = base / safe_relative(relative)
            if not folder.is_dir() or folder.is_symlink():
                raise ValueError(f"missing or linked exercise directory: {folder}")
            for source in sorted(folder.rglob("*")):
                if source.is_symlink():
                    raise ValueError(f"linked exercise source: {source}")
                if source.is_file():
                    rel = source.relative_to(base).as_posix()
                    if any(part == "__pycache__" for part in source.parts) or source.suffix == ".pyc":
                        continue
                    add(base, rel, str(prefix / rel))
        verifier = module.get("verifier_download")
        if verifier and (base / verifier) not in sources:
            add(base, verifier, str(prefix / verifier))
    for entry in course.get("shared_downloads", []):
        add(root, entry["source"], entry["dest"])
    ui_assets = course.get("ui_assets", [])
    for entry in ui_assets:
        if PurePosixPath(entry["source"]).suffix not in UI_SUFFIXES or PurePosixPath(entry["dest"]).suffix not in UI_SUFFIXES:
            raise ValueError("unsupported UI asset type")
        add(root, entry["source"], entry["dest"])
    if not {"assets/course.css", "assets/course.js", "assets/theme-init.js"}.issubset(entry["dest"] for entry in ui_assets):
        raise ValueError("course.css, course.js and theme-init.js must be declared")
    return course, destinations, sources, pages


def rewrite_link(value: str, source: Path, dest: PurePosixPath, mapping: dict[Path, PurePosixPath], course: dict, root: Path) -> str:
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return value
    if parsed.path.startswith("/"):
        raise ValueError(f"source link must be relative: {source}: {value}")
    target = Path(os.path.normpath(source.parent / unquote(parsed.path)))
    if target not in mapping:
        raise ValueError(f"unlisted local link: {source.relative_to(root)} -> {value}")
    path = posixpath.relpath(str(mapping[target]), str(dest.parent))
    return urlunsplit(("", "", quote(path, safe="/-._~"), parsed.query, parsed.fragment))


def procedure_errors(tree: Node, label: str) -> list[str]:
    errors = []
    nodes = list(tree.walk())
    if sum(node.tag == "h1" for node in nodes) != 1:
        errors.append(f"{label}: expected one h1")
    blocks = [node for node in nodes if node.tag in {"h1", "h2", "h3", "h4", "p", "pre", "summary"}]
    for index, node in enumerate(blocks):
        if node.tag != "pre":
            continue
        codes = [child for child in node.children if isinstance(child, Node) and child.tag == "code"]
        language = codes[0].attrs.get("class", "").removeprefix("language-") if len(codes) == 1 else ""
        if not language or not codes[0].attrs.get("class", "").startswith("language-"):
            errors.append(f"{label}: every fenced block needs an explicit language")
            continue
        if language not in COMMAND_LANGUAGES:
            continue
        previous = index - 1
        while previous >= 0 and blocks[previous].tag not in {"h1", "h2", "h3", "h4", "pre"}:
            previous -= 1
        before = " ".join(block.text() for block in blocks[previous + 1:index])
        end = index + 1
        while end < len(blocks) and blocks[end].tag not in {"h1", "h2", "h3", "h4"}:
            end += 1
        after = " ".join(block.text() for block in blocks[index + 1:end] if block.tag != "pre")
        if not re.search(r"\bTerminal\s*:", before, re.I) or not re.search(r"\b(user|administrator|admin|root|elevat\w*|privilege)\b", before, re.I):
            errors.append(f"{label}: {language} command lacks its terminal/privilege label")
        if not re.search(r"\b(Expected|Expect|You should see|You.ll see|Observation)\b", after, re.I):
            errors.append(f"{label}: {language} command lacks an associated expected observation")
        if not re.search(r"\b(Stop|HOLD)\b", after, re.I):
            errors.append(f"{label}: {language} command lacks an associated stop condition")
        if not re.search(r"\b(Recover\w*|Retry|Rerun|Restore|Ask|Choose|Correct|Return|Contact)\b", after, re.I):
            errors.append(f"{label}: {language} command lacks an associated recovery")
        if re.search(r"^(?:PASS|HOLD|FAIL|READY|READINESS CHECK (?:PASS|HOLD))(?::|$)", codes[0].text(), re.M):
            errors.append(f"{label}: observed output must be separate from command text")
        node.attrs["data-command"] = language
    return errors


def _page_records(course: dict) -> list[dict]:
    records = [{**course["index"], "path": course["index"]["dest"], "moduleId": None}]
    for module in course["modules"]:
        prefix = PurePosixPath(course["course_id"]) / module["directory"]
        records.extend({**page, "path": str(prefix / page["dest"]), "moduleId": module["id"]} for page in module["pages"])
    return records


def _guide_tree(tree: Node, guide: dict, label: str) -> tuple[list[dict], list[dict]]:
    """Group only top-level boundaries; retain the original nodes and their order."""
    contexts = set(guide.get("context_sections", []))
    optional = set(guide.get("optional_sections", []))
    headings = [node.attrs.get("id") for node in tree.children if isinstance(node, Node) and node.tag == "h2"]
    if any(headings.count(anchor) != 1 for anchor in contexts | optional):
        raise ValueError(f"{label}: missing or duplicate configured guide anchor")
    original_text = tree.text()
    original_ids = [node.attrs["id"] for node in tree.walk() if "id" in node.attrs]
    original_commands = [node.text() for node in tree.walk() if "data-command" in node.attrs]
    children, result, steps, outline = tree.children, [], [], []

    def stretch(node):
        return isinstance(node, Node) and node.tag == "details" and "rf-stretch" in node.attrs.get("class", "").split()

    def validate_group(nodes: list[Node | str]):
        errors = procedure_errors(Node("", {}, [Node("h1", {}, [label]), *nodes]), label)
        if errors:
            raise ValueError("\n".join(errors))

    def identify_stretch(node):
        node.attrs.setdefault("id", "rf-stretch")
        summaries = [child for child in node.children if isinstance(child, Node) and child.tag == "summary"]
        if len(summaries) != 1:
            raise ValueError(f"{label}: optional stretch requires one summary")
        outline.append({"id": node.attrs["id"], "title": "Optional stretch"})

    index = 0
    while index < len(children):
        node = children[index]
        if isinstance(node, Node) and node.tag == "h2":
            anchor = node.attrs["id"]
            end = index + 1
            while end < len(children) and not (isinstance(children[end], Node) and children[end].tag == "h2") and not stretch(children[end]):
                end += 1
            if anchor in optional:
                if end == len(children) or not stretch(children[end]):
                    raise ValueError(f"{label}: optional heading must precede its stretch disclosure")
                identify_stretch(children[end])
                group = children[index:end + 1]
                validate_group(group)
                result.append(Node("section", {"class": "rf-optional"}, group))
                index = end + 1
                continue
            group = children[index:end]
            validate_group(group)
            context = anchor in contexts
            name = "context" if context else "step"
            body = Node("div", {"class": f"rf-{name}-body", "id": f"rf-body-{anchor}"}, group[1:])
            result.append(Node("section", {"class": f"rf-{name}", f"data-{name}-id": anchor}, [node, body]))
            item = {"id": anchor, "title": node.text()}
            outline.append(item)
            if not context:
                steps.append(item)
            index = end
        elif stretch(node):
            identify_stretch(node)
            validate_group([node])
            result.append(node)
            index += 1
        else:
            if isinstance(node, Node) and any("data-command" in descendant.attrs for descendant in node.walk()):
                raise ValueError(f"{label}: command outside a procedure section")
            result.append(node)
            index += 1
    if not steps:
        raise ValueError(f"{label}: guide needs at least one core section")
    tree.children = result
    if tree.text() != original_text or [node.text() for node in tree.walk() if "data-command" in node.attrs] != original_commands:
        raise ValueError(f"{label}: procedure transformation changed authored text")
    final_ids = [node.attrs["id"] for node in tree.walk() if "id" in node.attrs]
    if any(anchor not in final_ids for anchor in original_ids) or len(final_ids) != len(set(final_ids)):
        raise ValueError(f"{label}: procedure transformation changed or duplicated an anchor")
    return steps, outline


def _section_records(tree: Node, title: str) -> list[dict]:
    """Attribute prose once, to its nearest heading; never index fenced bytes."""
    sections = []

    def new_section(anchor: str, text: str, optional: bool):
        record = {"id": anchor, "title": text, "text": [], "optional": optional}
        sections.append(record)
        return record

    current = new_section("", title, False)

    def visit(node: Node | str, optional: bool = False):
        nonlocal current
        if isinstance(node, str):
            current["text"].append(node)
            return
        if node.tag in {"pre", "h1"} or "data-course-map" in node.attrs:
            return
        classes = node.attrs.get("class", "").split()
        if "rf-optional" in classes or "rf-stretch" in classes:
            previous = current
            if "rf-stretch" in classes:
                summary = next(child for child in node.children if isinstance(child, Node) and child.tag == "summary")
                current = new_section(node.attrs["id"], summary.text(), True)
            for child in node.children:
                if not isinstance(child, Node) or child.tag != "summary":
                    visit(child, True)
            current = previous
            return
        if node.tag in {"h2", "h3"}:
            current = new_section(node.attrs["id"], node.text(), optional)
            return
        for child in node.children:
            visit(child, optional)
        if node.tag in {"p", "li", "td", "th", "summary", "blockquote"}:
            current["text"].append(" ")

    visit(tree)
    for section in sections:
        section["text"] = " ".join("".join(section["text"]).split())
    return sections


def _prepare_page(source: Path, dest: PurePosixPath, mapping: dict[Path, PurePosixPath], course: dict, root: Path, record: dict) -> dict:
    fragment = markdown.markdown(source.read_text(encoding="utf-8"), extensions=["fenced_code", "tables", "toc", "md_in_html"], extension_configs={"tables": {"use_align_attribute": True}}, output_format="html")
    try:
        tree = parse_html(fragment, True)
    except ValueError as error:
        raise ValueError(f"{source.relative_to(root)}: {error}") from error
    errors = procedure_errors(tree, source.relative_to(root).as_posix())
    if errors:
        raise ValueError("\n".join(errors))
    placeholders = [node for node in tree.walk() if "data-course-map" in node.attrs]
    if len(placeholders) != (1 if record["kind"] == "home" else 0):
        raise ValueError("exactly one course map placeholder is required, on home only")
    if any(node.attrs.get("id", "").startswith("rf-") for node in tree.walk()):
        raise ValueError("rf- anchors are reserved for the publisher")
    title = next(node.text() for node in tree.walk() if node.tag == "h1")
    steps = []
    outline = [{"id": node.attrs["id"], "title": node.text()} for node in tree.children if isinstance(node, Node) and node.tag == "h2"]
    if record["kind"] in {"lab", "setup"}:
        steps, outline = _guide_tree(tree, record["guide"], source.relative_to(root).as_posix())
    sections = _section_records(tree, title)
    heading = "Course data"
    for node in list(tree.walk()):
        if node.tag.startswith("h") and node.tag[1:].isdigit():
            heading = node.text()
        if node.tag == "table":
            node.children.insert(0, Node("caption", {}, [heading]))
        if node.tag == "th":
            node.attrs["scope"] = "col"
        if node.tag == "img" and not node.attrs.get("alt", "").strip():
            raise ValueError(f"{source}: image needs alternative text")
        for attr in ("href", "src"):
            if attr in node.attrs:
                node.attrs[attr] = rewrite_link(node.attrs[attr], source, dest, mapping, course, root)
    def wrap_tables(parent: Node):
        for i, child in enumerate(parent.children):
            if isinstance(child, Node):
                wrap_tables(child)
                if child.tag == "table":
                    parent.children[i] = Node("div", {"class": "table-scroll", "tabindex": "0", "role": "region", "aria-label": child.children[0].text()}, [child])
    wrap_tables(tree)
    return {"tree": tree, "title": title, "record": record, "sections": sections, "outline": outline, "steps": steps}


def _relative(dest: PurePosixPath, target: str) -> str:
    return quote(posixpath.relpath(target, str(dest.parent)), safe="/-._~")


def _course_map(course: dict, dest: PurePosixPath) -> Node:
    rows = []
    for module in course["modules"]:
        overview = next(page for page in module["pages"] if page["kind"] == "overview")
        path = str(PurePosixPath(course["course_id"]) / module["directory"] / overview["dest"])
        rows.append(Node("li", {}, [Node("a", {"href": _relative(dest, path)}, [
            Node("span", {"class": "rf-map-number"}, [module["id"]]),
            Node("span", {"class": "rf-map-name"}, [module["case_name"]]),
            Node("span", {"class": "rf-map-summary"}, [module["summary"]]),
        ])]))
    return Node("ol", {"class": "rf-course-map"}, rows)


def _module_routes(course: dict, module: dict) -> dict[str, str]:
    prefix = PurePosixPath(course["course_id"]) / module["directory"]
    return {page["kind"]: str(prefix / page["dest"]) for page in module["pages"] if page["kind"] in {"overview", "lab"}}


def _asset_context(course: dict, outputs: dict[PurePosixPath, bytes]) -> dict:
    declared = [PurePosixPath(entry["dest"]) for entry in course["ui_assets"]]
    fonts = []
    for path in declared:
        if path.suffix != ".css":
            continue
        for face in re.findall(r"@font-face\s*\{([^}]+)\}", outputs[path].decode(), re.S):
            if "U+0000-00FF" not in face or not re.search(r"font-family:\s*['\"](?:Inter|Space Grotesk)['\"]", face):
                continue
            source = re.search(r"""url\(['"]([^'"]+)['"]\)""", face)
            if source:
                fonts.append(posixpath.normpath(str(path.parent / source[1])))
    dimensions = {}
    for path, data in outputs.items():
        if path.suffix == ".svg" and "figures" in path.parts:
            image = ET.fromstring(data)
            viewbox = image.get("viewBox", "").split()
            width, height = image.get("width", ""), image.get("height", "")
            if not width.isdigit() or not height.isdigit():
                if len(viewbox) != 4:
                    raise ValueError(f"figure lacks intrinsic dimensions: {path}")
                width, height = viewbox[2:]
            dimensions[str(path)] = (width, height)
    return {"styles": [str(path) for path in declared if path.suffix == ".css"],
            "fonts": fonts, "hero": next((str(path) for path in declared if path.suffix == ".webp"), None),
            "dimensions": dimensions}


def _appearance(extra_class: str = "") -> str:
    return f'''<label class="rf-appearance {extra_class}" hidden>Appearance
<select class="sc-select" data-theme><option value="system">System</option><option value="dark">Dark</option><option value="sand">Sand</option></select></label>'''


def _reset_place() -> str:
    return '<button type="button" class="sc-btn rf-btn sc-btn--secondary rf-reset" data-reset-place hidden>Reset saved place</button>'


def _course_navigation(modules: list[dict], dest: PurePosixPath, current_module: str | None, rail: bool = False) -> str:
    links = []
    for module in modules:
        attrs = ' aria-current="page"' if module["overview"] == str(dest) else ""
        if module["id"] == current_module:
            attrs += f' data-current-module="{module["id"]}"'
        label = html.escape(f'{module["id"]} · {module["caseName"]}')
        summary = html.escape(module["navSummary"])
        css = ' class="sc-rail__item"' if rail else ""
        links.append(f'<a{css} href="{_relative(dest, module["overview"])}"{attrs}><span class="sc-rail__label"><span class="rf-nav-name">{label}</span><span class="rf-nav-summary">{summary}</span></span></a>')
    return f'<nav class="rf-nav{" sc-rail" if rail else ""}" aria-label="Course assignments">{"".join(links)}</nav>'


def _outline(items: list[dict], *, inline: bool = False) -> str:
    links = "".join(f'<a href="#{html.escape(item["id"], quote=True)}">{html.escape(item["title"])}</a>' for item in items)
    if inline:
        return f'<details class="rf-inline-outline"><summary>On this page</summary><nav aria-label="Page sections">{links}</nav></details>'
    return f'<nav id="rf-outline" aria-label="Page sections"><h2 class="sc-label">On this page</h2>{links}</nav>'


def _decorate_reading(tree: Node, dest: PurePosixPath, assets: dict, kind: str):
    entry = False
    for child in tree.children:
        if not isinstance(child, Node):
            continue
        if child.tag == "h2":
            entry = child.attrs.get("id") == "start-here"
        if entry and child.tag in {"ol", "ul"} and kind == "overview":
            child.attrs["class"] = "rf-entry-sequence"
            first = next((node for node in child.walk() if node.tag == "a"), None)
            if first:
                first.attrs["class"] = "sc-btn rf-btn sc-btn--primary"

    def decorate(parent: Node):
        for index, child in enumerate(parent.children):
            if not isinstance(child, Node):
                continue
            decorate(child)
            if child.tag == "pre":
                language = child.attrs.get("data-command", "Source")
                child.attrs.update({"tabindex": "0", "role": "region", "aria-label": f"{language} code"})
            if child.tag == "table" and kind == "overview" and any("/platforms/" in n.attrs.get("href", "") or n.attrs.get("href", "").startswith("platforms/") for n in child.walk()):
                child.attrs["class"] = "rf-platform-table"
            if child.tag == "img":
                target = posixpath.normpath(str(dest.parent / unquote(urlsplit(child.attrs["src"]).path)))
                if target in assets["dimensions"]:
                    width, height = assets["dimensions"][target]
                    child.attrs.update({"width": width, "height": height, "loading": "lazy", "class": "rf-figure-image"})
                    link = Node("a", {"href": child.attrs["src"], "class": "rf-figure-link", "data-figure-open": ""}, ["Open full-size figure"])
                    parent.children[index] = Node("span", {"class": "rf-figure"}, [child, link])
    decorate(tree)


def _dialogs(navigation: str, home: str) -> str:
    close = '<button type="button" class="sc-btn rf-btn sc-btn--secondary" data-dialog-close>Close</button>'
    return f'''<dialog id="rf-course-dialog" class="sc-drawer rf-dialog" aria-labelledby="rf-course-title" hidden>
<div class="rf-dialog-head"><h2 id="rf-course-title">Course</h2>{close}</div>{navigation}
<div class="rf-menu-tools">{_appearance()}{_reset_place()}</div></dialog>
<dialog id="rf-search-dialog" class="sc-palette rf-dialog" aria-labelledby="rf-search-title" hidden>
<div class="rf-dialog-head"><h2 id="rf-search-title">Search course</h2>{close}</div>
<label for="rf-search-input">Search the lessons</label><input id="rf-search-input" class="sc-input" type="search" autocomplete="off">
<p id="rf-search-status" role="status"></p><ol id="rf-search-results" class="rf-search-results"></ol>
<div class="rf-search-recovery" hidden><button type="button" class="sc-btn rf-btn sc-btn--secondary" data-search-retry>Retry</button>
<a class="sc-btn rf-btn sc-btn--secondary" href="{home}#choose-your-assignment">Course map</a></div></dialog>
<dialog id="rf-figure-dialog" class="sc-drawer rf-dialog" aria-labelledby="rf-figure-title" hidden>
<div class="rf-dialog-head"><h2 id="rf-figure-title">Full-size figure</h2>{close}</div>
<div class="rf-figure-scroll" tabindex="0" role="region" aria-label="Full-size figure"></div></dialog>'''


def render_page(source: Path, dest: PurePosixPath, mapping: dict[Path, PurePosixPath], course: dict, root: Path, prepared: dict) -> bytes:
    tree, title, record, common = prepared["tree"], prepared["title"], prepared["record"], prepared["common"]
    kind, module_id = record["kind"], record["moduleId"]
    home = _relative(dest, course["index"]["dest"])
    assets = common["assets"]
    module = next((item for item in course["modules"] if item["id"] == module_id), None)
    routes = _module_routes(course, module) if module else {}
    navigation = _course_navigation(common["modules"], dest, module_id)
    _decorate_reading(tree, dest, assets, kind)
    for node in list(tree.walk()):
        if "data-course-map" in node.attrs:
            node.children = [_course_map(course, dest)]
    h1 = next(node for node in tree.children if isinstance(node, Node) and node.tag == "h1")
    tree.children.remove(h1)
    page_data = {"version": 1, "page": str(dest), "kind": kind, "moduleId": module_id,
                 "root": posixpath.relpath(".", str(dest.parent)).rstrip("/") + "/",
                 "modules": common["modules"], "pages": common["pages"], "steps": prepared["steps"], "resume": common["resume"]}
    if kind == "home":
        lead = next(node for node in tree.children if isinstance(node, Node) and node.tag == "p")
        tree.children.remove(lead)
        lead.attrs["class"] = "rf-lead"
        setup = _relative(dest, common["modules"][0]["overview"])
        image = f'<img class="rf-hero-image" src="{_relative(dest, assets["hero"])}" width="1672" height="941" alt="" fetchpriority="high">' if assets["hero"] else ""
        main = f'''<main id="main" class="rf-home-main" tabindex="-1"><section class="rf-hero sc-photo" data-sc-theme="dark">{image}
<div class="rf-hero-content">{h1.render()}{lead.render()}
<div class="rf-hero-actions"><a id="rf-home-primary" class="sc-btn rf-btn sc-btn--primary" href="{setup}">Start with setup</a>
<a class="sc-btn rf-btn sc-btn--secondary" href="#choose-your-assignment">Explore the course</a></div>
<p id="rf-resume-note" hidden></p><a id="rf-home-setup" href="{setup}" hidden>Start with setup</a></div></section>
<div class="rf-home-content">{tree.render()}</div></main>'''
    else:
        role = {"overview": "Overview", "lab": "Lab", "setup": "Setup", "reference": "Reference"}[kind]
        breadcrumb = f'<nav class="rf-breadcrumb" aria-label="Breadcrumb"><a href="{home}">Course</a><span aria-hidden="true"> / </span><a href="{_relative(dest, routes["overview"])}">{module_id} · {html.escape(module["case_name"])}</a><span aria-hidden="true"> / </span><span>{role}</span></nav>'
        links = []
        for page_kind, label in (("overview", "Overview"), ("lab", "Lab")):
            current = ' aria-current="page"' if str(dest) == routes[page_kind] else ""
            links.append(f'<a href="{_relative(dest, routes[page_kind])}"{current}>{label}</a>')
        local = f'<nav class="rf-local-links" aria-label="Assignment documents">{"".join(links)}</nav>'
        intro = []
        while tree.children:
            node = tree.children[0]
            if isinstance(node, Node) and (node.tag in {"h2", "section"} or "rf-stretch" in node.attrs.get("class", "").split()):
                break
            intro.append(tree.children.pop(0))
        controls = ""
        if kind in {"lab", "setup"}:
            controls = '''<fieldset id="rf-reader-controls" hidden><legend>Reading mode</legend>
<button type="button" class="sc-btn rf-btn sc-btn--secondary" data-view-choice="guided">Guided</button>
<button type="button" class="sc-btn rf-btn sc-btn--secondary" data-view-choice="read">Read full page</button>
<p class="rf-reader-hint">Use Read full page to find text across every section.</p></fieldset>'''
        inline_outline = "" if kind in {"lab", "setup"} else _outline(prepared["outline"], inline=True)
        if prepared["steps"]:
            last = next(node for node in tree.walk() if node.attrs.get("data-step-id") == prepared["steps"][-1]["id"])
            actions = []
            stretch = next((node for node in tree.walk() if "rf-stretch" in node.attrs.get("class", "").split()), None)
            if stretch:
                actions.append(Node("a", {"href": "#" + stretch.attrs["id"], "class": "sc-btn rf-btn sc-btn--secondary"}, ["Optional stretch"]))
            if kind == "setup":
                next_href, next_label = _relative(dest, routes["lab"]), "Open the lab"
            elif module_id == "09":
                next_href, next_label = home + "#choose-your-assignment", "Course map"
            else:
                next_href, next_label = _relative(dest, common["modules"][int(module_id) + 1]["overview"]), "Next assignment"
            actions.append(Node("a", {"href": next_href, "class": "sc-btn rf-btn sc-btn--secondary"}, [next_label]))
            last.children[-1].children.append(Node("nav", {"class": "rf-end-actions", "aria-label": "Continue reading"}, actions))
        back = f'<p class="rf-back-to-lab"><a class="sc-btn rf-btn sc-btn--secondary" href="{_relative(dest, routes["lab"])}">Back to lab</a></p>' if kind == "reference" else ""
        main = f'''<div class="rf-layout"><aside class="rf-course-rail">{_course_navigation(common["modules"], dest, module_id, True)}</aside>
<main id="main" class="rf-reading" tabindex="-1"><header class="rf-page-header sc-grid">{breadcrumb}{h1.render()}</header>{local}
<div class="rf-intro">{Node("", {}, intro).render()}</div><div class="rf-reader-mobile-slot">{controls}</div>{inline_outline}{tree.render()}{back}</main>
<aside class="rf-section-rail"><div class="rf-reader-desktop-slot"></div>{_outline(prepared["outline"])}</aside></div>'''
    styles = "".join(f'<link rel="stylesheet" href="{_relative(dest, path)}">' for path in assets["styles"])
    preloads = "".join(f'<link rel="preload" href="{_relative(dest, path)}" as="font" type="font/woff2" crossorigin>' for path in assets["fonts"])
    data = json.dumps(page_data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    document = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><script src="{_relative(dest, "assets/theme-init.js")}"></script>{preloads}{styles}
<script src="{_relative(dest, "assets/course.js")}" defer></script></head>
<body class="{"rf-home" if kind == "home" else "rf-interior"}" data-page-kind="{kind}">
<a class="sc-skip-link" href="#main">Skip to content</a>
<header class="rf-masthead sc-grain"><div class="rf-masthead-inner">
<a class="sc-brand rf-brand" href="{home}" aria-label="Starzl Enterprises AI Harness Bootcamp — home"><span class="sc-brand__dot" aria-hidden="true"></span>
<span class="sc-brand__name">Starzl Enterprises</span><span class="sc-brand__divider" aria-hidden="true"></span><span class="sc-brand__product">AI Harness Bootcamp</span></a>
<div class="rf-header-actions"><button type="button" class="sc-btn rf-btn sc-btn--secondary" data-search-open hidden>Search course</button>
<button type="button" class="sc-btn rf-btn sc-btn--secondary rf-course-trigger" data-course-open hidden>Course</button>{_appearance("rf-desktop-appearance")}</div></div>
<details class="rf-course-fallback"><summary>Course</summary>{navigation}</details></header>{main}
<div class="rf-status"><p id="copy-status" role="status" aria-live="polite"></p><p id="rf-state-status" role="status"></p></div>
<footer class="rf-footer"><p class="rf-caveat">Fictional, class-only work. A passing check does not authorize a real movement.</p>
<div class="rf-footer-tools">{_appearance()}{_reset_place()}</div>
<p class="rf-print-note">Expand optional work and figure-text disclosures before printing if your browser does not expand them automatically.</p></footer>
{_dialogs(navigation, home)}<script type="application/json" id="rf-page-data">{data}</script></body></html>
'''
    return document.encode("utf-8")


def validate_links(outputs: dict[PurePosixPath, bytes]) -> None:
    parsed = {path: parse_html(data.decode("utf-8")) for path, data in outputs.items() if path.suffix == ".html"}
    anchors = {}
    for path, tree in parsed.items():
        ids = [node.attrs["id"] for node in tree.walk() if "id" in node.attrs]
        if len(ids) != len(set(ids)):
            raise ValueError(f"duplicate HTML anchor: {path}")
        anchors[path] = set(ids)
    for path, tree in parsed.items():
        for node in tree.walk():
            for attr in ("href", "src"):
                value = node.attrs.get(attr)
                if value is None:
                    continue
                url = urlsplit(value)
                if url.scheme or url.netloc:
                    continue
                target = PurePosixPath(posixpath.normpath(str(path.parent / unquote(url.path)))) if url.path else path
                if target not in outputs:
                    raise ValueError(f"broken published link: {path} -> {value}")
                if url.fragment and target in anchors and unquote(url.fragment) not in anchors[target]:
                    raise ValueError(f"missing published anchor: {path} -> {value}")
    for path, data in outputs.items():
        if path.suffix != ".css":
            continue
        css = re.sub(r"/\*.*?\*/", "", data.decode("utf-8"), flags=re.S)
        references = [next(value for value in match if value) for match in re.findall(r"""url\(\s*(?:'([^']*)'|"([^"]*)"|([^)\s]+))\s*\)""", css, re.I)]
        references.extend(re.findall(r"""@import\s+['"]([^'"]+)['"]""", css, re.I))
        for value in references:
            url = urlsplit(value)
            if url.scheme == "data":
                continue
            if url.scheme or url.netloc or url.path.startswith("/") or "\\" in value:
                raise ValueError(f"nonlocal CSS dependency: {path} -> {value}")
            target = PurePosixPath(posixpath.normpath(str(path.parent / unquote(url.path)))) if url.path else path
            if target not in outputs:
                raise ValueError(f"missing CSS dependency: {path} -> {value}")
    if SEARCH_PATH in outputs:
        search = json.loads(outputs[SEARCH_PATH])
        if {page["path"] for page in search["pages"]} != {str(path) for path in parsed}:
            raise ValueError("search must contain exactly the instructional destinations")
        targets = [(page["path"], section["id"]) for page in search["pages"] for section in page["sections"]]
        for tree in parsed.values():
            for node in tree.walk():
                if node.attrs.get("id") == "rf-page-data":
                    page_data = json.loads(node.text())
                    targets.extend((path, section["id"]) for path, sections in page_data.get("resume", {}).items() for section in sections)
        for path, anchor in targets:
            if PurePosixPath(path) not in anchors or (anchor and anchor not in anchors[PurePosixPath(path)]):
                raise ValueError(f"dangling search/resume target: {path}#{anchor}")


def build(root: Path = ROOT, check: bool = False) -> int:
    course, destinations, mapping, pages = inventory(root)
    records = {PurePosixPath(record["path"]): record for record in _page_records(course)}
    prepared = {dest: _prepare_page(source, dest, mapping, course, root, records[dest]) for dest, source in destinations.items() if source in pages}
    outputs = {dest: source.read_bytes() for dest, source in destinations.items() if source not in pages}
    common = {
        "assets": _asset_context(course, outputs),
        "modules": [{"id": module["id"], "caseName": module["case_name"], "navSummary": module["nav_summary"], "overview": _module_routes(course, module)["overview"]} for module in course["modules"]],
        "pages": [{"path": str(dest), "title": page["title"], "kind": page["record"]["kind"], "moduleId": page["record"]["moduleId"]} for dest, page in prepared.items()],
        "resume": {str(dest): [{**step, "optional": False} for step in page["steps"]] + [
            {key: section[key] for key in ("id", "title", "optional")} for section in page["sections"] if section["optional"]
        ] for dest, page in prepared.items() if page["record"]["kind"] in {"lab", "setup"}},
    }
    for dest, page in prepared.items():
        page["common"] = common
        outputs[dest] = render_page(destinations[dest], dest, mapping, course, root, page)
    outputs[SEARCH_PATH] = (json.dumps({"version": 1, "pages": [
        {"path": str(dest), "moduleId": page["record"]["moduleId"], "kind": page["record"]["kind"], "title": page["title"], "sections": page["sections"]}
        for dest, page in prepared.items()
    ]}, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
    validate_links(outputs)
    site = root / "site"
    if site.is_symlink():
        raise ValueError("site must not be a symlink")
    existing = set()
    if site.exists():
        for path in site.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"linked public output: {path}")
            if path.is_file():
                existing.add(PurePosixPath(path.relative_to(site).as_posix()))
    extras = existing - outputs.keys()
    if extras:
        raise ValueError("unlisted public output (preserved): " + ", ".join(map(str, sorted(extras))))
    if check:
        mismatches = [str(dest) for dest, data in outputs.items() if dest not in existing or (site / dest).read_bytes() != data]
        if mismatches:
            raise ValueError("missing or stale published bytes: " + ", ".join(mismatches))
        # Read the actual published documents, not only regenerated fragments.
        validate_links({dest: (site / dest).read_bytes() for dest in outputs})
    else:
        for dest, data in outputs.items():
            target = site / dest
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    ui_count = len(course["ui_assets"]) + 1
    print(f"PASS: {len(pages)} instructional pages, {len(outputs) - len(pages) - ui_count} raw downloads, {ui_count} UI/generated assets {'checked byte-for-byte' if check else 'published'}; public links and procedure structure checked")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        return build(check=args.check)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"HOLD: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
