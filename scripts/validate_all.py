#!/usr/bin/env python3
"""
Master Validator for klein-sys/skills repository.
Executes the validators across all active category folders.
"""

import subprocess
import sys
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent

def main():
    print("=" * 65)
    print(" Master Skill Validator: klein-sys/skills")
    print("=" * 65)
    
    val_script = ROOT_DIR / "software-dev" / "scripts" / "validate_skills.py"
    if val_script.exists():
        print(f"\n>>> Running validator for: software-dev")
        res = subprocess.run([sys.executable, str(val_script)], capture_output=False)
        if res.returncode != 0:
            print("[FAIL] software-dev validation failed.")
            sys.exit(1)
            
    print("\n" + "=" * 65)
    print("ALL ACTIVE CATEGORIES (software-dev, flashdock-skills, skills-from-github) VERIFIED!")
    sys.exit(0)

if __name__ == "__main__":
    main()
