#!/usr/bin/env python3
"""
Skill Validator for klein-sys/skills repository.
Recursively validates:
1. Category directories (e.g. software-dev/) and .agents/skills/.
2. YAML frontmatter parsing (name, description).
3. Name matches folder naming conventions.
4. Internal markdown links point to existing files.
"""

import os
import re
import sys
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent

def parse_frontmatter(content: str):
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", content, re.DOTALL)
    if not match:
        return None, content
    raw_frontmatter = match.group(1)
    body = match.group(2)
    metadata = {}
    
    lines = raw_frontmatter.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("#"):
            i += 1
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val in (">-", ">", "|"):
                multiline = []
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                    multiline.append(lines[i].strip())
                    i += 1
                metadata[key] = " ".join(multiline).strip()
                continue
            else:
                metadata[key] = val.strip("\"'")
        i += 1
    return metadata, body

def validate_skill(skill_path: pathlib.Path):
    errors = []
    warnings = []
    
    skill_name = skill_path.name
    skill_md = skill_path / "SKILL.md"
    
    if not skill_md.exists():
        return False, [f"Missing SKILL.md in {skill_name}"], []

    content = skill_md.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)
    
    if meta is None:
        errors.append(f"Invalid or missing YAML frontmatter in {skill_name}/SKILL.md")
        return False, errors, warnings
        
    if "name" not in meta:
        errors.append(f"Missing 'name' field in frontmatter of {skill_name}")
    elif meta["name"] != skill_name:
        errors.append(f"Frontmatter name '{meta['name']}' does not match directory name '{skill_name}'")
        
    if "description" not in meta or not meta["description"].strip():
        errors.append(f"Missing or empty 'description' in {skill_name}")
    elif len(meta["description"]) < 30:
        warnings.append(f"Description for {skill_name} is brief ({len(meta['description'])} chars).")

    # Check internal markdown links
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', body)
    for link_text, link_target in links:
        if link_target.startswith("http://") or link_target.startswith("https://") or link_target.startswith("#"):
            continue
        clean_target = link_target.split("#")[0].split("?")[0]
        if not clean_target:
            continue
        target_path = (skill_path / clean_target).resolve()
        if not target_path.exists():
            errors.append(f"Broken internal link in {skill_name}/SKILL.md: '{link_target}' -> File not found at {target_path}")

    return len(errors) == 0, errors, warnings

def validate_directory(target_dir: pathlib.Path):
    print(f"\nScanning: {target_dir.relative_to(ROOT_DIR)}")
    passed = 0
    failed = 0
    all_errors = []
    
    for item in sorted(target_dir.iterdir()):
        if item.is_dir() and (item / "SKILL.md").exists():
            is_valid, errs, warns = validate_skill(item)
            if is_valid:
                print(f"  [PASS] {item.name}")
                passed += 1
            else:
                print(f"  [FAIL] {item.name}")
                for e in errs:
                    print(f"         ERROR: {e}")
                all_errors.extend(errs)
                failed += 1
            for w in warns:
                print(f"         WARN:  {w}")
    return passed, failed, all_errors

def main():
    print("=" * 60)
    print(" Validating klein-sys/skills Repository")
    print("=" * 60)
    
    total_passed = 0
    total_failed = 0
    total_errors = []
    
    categories = [ROOT_DIR / "software-dev", ROOT_DIR / ".agents" / "skills"]
    for cat in categories:
        if cat.exists():
            p, f, errs = validate_directory(cat)
            total_passed += p
            total_failed += f
            total_errors.extend(errs)
            
    print("\n" + "-" * 60)
    print(f"Validation Summary: {total_passed} passed, {total_failed} failed.")
    if total_errors:
        print(f"Errors encountered: {len(total_errors)}")
        sys.exit(1)
    else:
        print("All skills across all categories verified successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
