#!/usr/bin/env python3
"""Read-only structure checks for this instruction-only distribution.

This checks the simple scalar metadata and inline Markdown links used here;
it is not a full YAML/Markdown parser or an exhaustive secret scanner.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def check(root: Path) -> list[str]:
    root = root.resolve()
    issues: list[str] = []
    skill = root / "skills" / "web-design-workflow"
    refs = (
        "content-and-consistency.md",
        "media-and-evidence.md",
        "local-delivery.md",
    )
    required = (
        root / "README.md", root / "LICENSE", root / "VERSION",
        root / "THIRD_PARTY.md", skill / "SKILL.md", skill / "LICENSE",
        skill / "agents" / "openai.yaml",
        *(skill / "references" / name for name in refs),
    )
    for path in required:
        if not path.is_file():
            issues.append(f"Missing required file: {path.relative_to(root)}")

    texts: dict[Path, str] = {}
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(part in {".git", "__pycache__"} for part in rel.parts):
            continue
        if not path.resolve().is_relative_to(root):
            issues.append(f"Path escapes repository: {rel}")
            continue
        if not path.is_file():
            continue
        if any(part in {"node_modules", ".venv"} for part in rel.parts) or path.suffix == ".zip":
            issues.append(f"Unexpected distribution artifact: {rel}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError) as exc:
            issues.append(f"Unreadable UTF-8 source: {rel} ({exc})")
            continue
        texts[path] = text
        private_path = r"(?i)(?:[a-z]:[\\/]Users[\\/][^\s/\\]+|/(?:Users|home)/[A-Za-z0-9_.-]+/)"
        credential = r"(?:ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)"
        if re.search(private_path, text):
            issues.append(f"Personal absolute path: {rel}")
        if re.search(credential, text):
            issues.append(f"Potential credential: {rel}")
        if path.suffix != ".md":
            continue
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", prose):
            target = target.strip().strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            destination = (path.parent / unquote(target.split("#")[0])).resolve()
            if not destination.is_relative_to(root):
                issues.append(f"External filesystem link in {rel}: {target}")
            elif not destination.exists():
                issues.append(f"Broken local link in {rel}: {target}")

    entry = texts.get(skill / "SKILL.md", "")
    if texts.get(root / "LICENSE") != texts.get(skill / "LICENSE"):
        issues.append("Installable skill must carry the same license as the repository")
    header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", entry, re.S)
    if not header:
        issues.append("SKILL.md must begin with YAML frontmatter")
    else:
        values = dict(re.findall(r"^([a-z_-]+):[ \t]*(.+)$", header.group(1), re.M))
        if values.get("name") != skill.name:
            issues.append("Skill name must match its install directory")
        if not 1 <= len(values.get("description", "")) <= 1024:
            issues.append("Skill description missing or too long")
    for name in refs:
        if f"references/{name}" not in entry:
            issues.append(f"Reference not routed from SKILL.md: {name}")

    ui = texts.get(skill / "agents" / "openai.yaml", "")
    if re.search(r"allow_implicit_invocation:\s*false", ui):
        issues.append("Automatic discovery was unexpectedly disabled")
    if "$web-design-workflow" not in ui:
        issues.append("Default prompt must identify the skill")
    short = re.search(r'^\s*short_description: "(.*)"$', ui, re.M)
    if not short or not 25 <= len(short.group(1)) <= 64:
        issues.append("UI short description must contain 25–64 characters")
    version = texts.get(root / "VERSION", "").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        issues.append("VERSION must contain a numeric major.minor.patch version")
    return issues


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    if not root.is_dir():
        print(f"FAIL: Repository directory not found: {root}")
        return 1
    issues = check(root)
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        return 1
    print("PASS: Package structure, metadata, local file links, and portability checks.")
    print("Not covered: remote URLs, anchors, browser behavior, or agent outcomes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
