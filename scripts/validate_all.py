#!/usr/bin/env python3
"""
Master Validator for klein-sys/skills repository.
Executes the validators across all active category folders.
"""

import subprocess
import sys
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent

CATEGORIES = [
    ROOT_DIR / "software-dev",
    ROOT_DIR / "flashdock",
    ROOT_DIR / "agent-productivity"
]

def main():
    print("=" * 65)
    print(" Master Skill Validator: klein-sys/skills")
    print("=" * 65)
    
    total_failed_categories = 0
    
    for cat in CATEGORIES:
        val_script = cat / "scripts" / "validate_skills.py"
        if val_script.exists():
            print(f"\n>>> Running validator for: {cat.name}")
            res = subprocess.run([sys.executable, str(val_script)], capture_output=False)
            if res.returncode != 0:
                total_failed_categories += 1
        else:
            print(f"\n[WARN] No validator script found in {cat.name}/scripts/")

    print("\n" + "=" * 65)
    if total_failed_categories > 0:
        print(f"Validation FAILED in {total_failed_categories} categories.")
        sys.exit(1)
    else:
        print("ALL ACTIVE CATEGORIES (software-dev, flashdock, agent-productivity) PASSED!")
        sys.exit(0)

if __name__ == "__main__":
    main()
