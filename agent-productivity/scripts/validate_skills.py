#!/usr/bin/env python3
"""
Validator for Agent Productivity skills pack in klein-sys/skills.
Recursively scans productivity/, engineering/, in-progress/, misc/, and standalone skills.
"""

import os
import re
import sys
import pathlib

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
CATEGORY_DIR = SCRIPT_DIR.parent

def parse_frontmatter(content: str):
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", content, re.DOTALL)
    if not match:
        return None, content
    raw = match.group(1)
    body = match.group(2)
    meta = {}
    lines = raw.splitlines()
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
                meta[key] = " ".join(multiline).strip()
                continue
            else:
                meta[key] = val.strip("\"'")
        i += 1
    return meta, body

def validate_skill(skill_path: pathlib.Path):
    errors = []
    warnings = []
    
    skill_name = skill_path.name
    skill_md = skill_path / "SKILL.md"
    
    if not skill_md.exists():
        return False, [f"Missing SKILL.md in {skill_name}"], []

    content = skill_md.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_frontmatter(content)
    
    if meta is None:
        errors.append(f"Invalid or missing YAML frontmatter in {skill_path.relative_to(CATEGORY_DIR)}")
        return False, errors, warnings
        
    if "name" not in meta:
        errors.append(f"Missing 'name' field in {skill_path.relative_to(CATEGORY_DIR)}")
    if "description" not in meta or not meta["description"].strip():
        errors.append(f"Missing or empty 'description' in {skill_path.relative_to(CATEGORY_DIR)}")

    return len(errors) == 0, errors, warnings

def main():
    print("=" * 60)
    print(" Validating Agent Productivity Skills")
    print("=" * 60)
    print(f"Scanning category folder: {CATEGORY_DIR}\n")
    
    passed = 0
    failed = 0
    all_errors = []
    
    for root, dirs, files in os.walk(CATEGORY_DIR):
        if "scripts" in root:
            continue
        if "SKILL.md" in files:
            skill_dir = pathlib.Path(root)
            rel_name = str(skill_dir.relative_to(CATEGORY_DIR))
            is_valid, errs, warns = validate_skill(skill_dir)
            if is_valid:
                print(f"  [PASS] {rel_name}")
                passed += 1
            else:
                print(f"  [FAIL] {rel_name}")
                for e in errs:
                    print(f"         ERROR: {e}")
                all_errors.extend(errs)
                failed += 1
            for w in warns:
                print(f"         WARN:  {w}")

    print("\n" + "-" * 60)
    print(f"Validation Summary: {passed} passed, {failed} failed.")
    if all_errors:
        print(f"Total Errors: {len(all_errors)}")
        sys.exit(1)
    else:
        print("All Agent Productivity skills verified successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
