# AI Agent Skills Library (`klein-sys/skills`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Platform: Antigravity & Gemini](https://img.shields.io/badge/Platform-Antigravity%20%7C%20Gemini-green.svg)](#compatibility)
[![Architecture: Progressive Disclosure](https://img.shields.io/badge/Architecture-Progressive%20Disclosure-purple.svg)](#progressive-disclosure)

A modular, extensible personal skill library designed for AI coding agents operating in **Google Antigravity**, **Gemini**, and multi-agent harnesses.

Organized into domain categories to support continuous expansion across software engineering, application security, design systems, mobile development, and emerging agent workflows.

---

## Repository Category Architecture

This repository is structured into domain categories, allowing specialized skill packs to be added and maintained independently:

```
klein-sys/skills/
├── software-dev/                      # Core Software Engineering & Quality Pack
│   ├── software-engineering-planning/
│   ├── systematic-debugging-tdd/
│   ├── git-github-workflows/
│   ├── secure-coding-review/
│   ├── authorized-web-security-testing/
│   ├── ui-ux-design-systems/
│   ├── accessibility-responsive-design/
│   ├── code-review-qa/
│   └── README.md
├── .agents/
│   └── skills/                        # Flat native mirror for instant Antigravity discovery
├── scripts/
│   └── validate_skills.py             # Recursive skill structure & link validator
├── README.md                          # Repository overview and installation manual
├── ATTRIBUTION.md                     # Open-source source & license attribution
├── COMPATIBILITY_REPORT.md            # Agent harness compatibility analysis
└── LICENSE                            # MIT License
```

*Future categories (e.g., `android-dev/`, `cloud-infra/`, `ai-ml/`) will be introduced in parallel category directories.*

---

## 1. Software Development Category (`software-dev/`)

The foundational pack for software engineers, application security engineers, and UI/UX designers:

| Skill | Domain / Focus | Key Workflow Highlights |
| :--- | :--- | :--- |
| **[`software-engineering-planning`](./software-dev/software-engineering-planning/SKILL.md)** | Architecture & Planning | Discovery -> Tech Spec -> Risk & Dependency Mapping -> Atomic Task Breakdown with DoD -> ADRs. |
| **[`systematic-debugging-tdd`](./software-dev/systematic-debugging-tdd/SKILL.md)** | Debugging & TDD | 4-Phase Diagnosis (Reproduce -> Trace Invariants -> Failing Regression Test -> Minimal Fix & Refactor). |
| **[`git-github-workflows`](./software-dev/git-github-workflows/SKILL.md)** | Git & GitHub Hygiene | Conventional Commits, branch hygiene, safe rebasing, `git worktree` isolation, PR readiness reviews. |
| **[`secure-coding-review`](./software-dev/secure-coding-review/SKILL.md)** | Application Security | Component trust boundaries, STRIDE threat modeling, OWASP Top 10 code defenses, zero secret leakage. |
| **[`authorized-web-security-testing`](./software-dev/authorized-web-security-testing/SKILL.md)** | Ethical Security Testing | Strict scope authorization verification, non-destructive OWASP WSTG v4.2 test procedures, CVSS scoring. |
| **[`ui-ux-design-systems`](./software-dev/ui-ux-design-systems/SKILL.md)** | UI/UX & Design Systems | Distinct aesthetic themes, 3-tier CSS design tokens, typography pairings, bento layouts, anti-generic rules. |
| **[`accessibility-responsive-design`](./software-dev/accessibility-responsive-design/SKILL.md)** | Responsive & Accessibility | Mobile-first CSS Grid/flexbox, fluid clamp typography, WCAG 2.1 Level AA compliance, keyboard focus traps. |
| **[`code-review-qa`](./software-dev/code-review-qa/SKILL.md)** | Code Review & QA Gates | 6-dimension review scorecard (Correctness, Security, Reliability, Tests, Maintainability, Scale), CI gates. |

---

## Progressive Disclosure

Each skill adheres strictly to Antigravity's **Progressive Disclosure** specification:
1. **Lightweight Metadata**: The agent only ingests the `name` and `description` frontmatter upon launch, preserving conversation context tokens.
2. **Autonomous Activation**: When a matching user request or task is detected, the agent reads the full `SKILL.md` runbook.
3. **Deep References on Demand**: Bulky templates, threat modeling matrices, and code examples reside in `references/` and `examples/` subdirectories, read only when required.

---

## Installation & Setup

### Method 1: Drop into an Active Project Workspace
To enable all skills in an existing Antigravity project:

```powershell
# In PowerShell:
$projectRoot = "C:\Path\To\YourProject"
New-Item -ItemType Directory -Force -Path "$projectRoot\.agents\skills"
Copy-Item -Recurse -Force "software-dev\*" "$projectRoot\.agents\skills\"
```

### Method 2: Global Machine-Wide Installation
To make all skills available across every project and conversation:

```powershell
$globalSkills = "$env:USERPROFILE\.gemini\config\skills"
New-Item -ItemType Directory -Force -Path $globalSkills
Copy-Item -Recurse -Force "software-dev\*" "$globalSkills\"
```

### Method 3: Antigravity CLI Plugin
Install directly from this repository:
```bash
agy plugin install https://github.com/klein-sys/skills
```

---

## Adding New Skills & Categories

To contribute a new skill category:
1. Create a category directory: `mkdir <category-name>`.
2. Add a skill package: `<category-name>/<skill-name>/SKILL.md` with standard YAML frontmatter:
   ```markdown
   ---
   name: my-new-skill
   description: >-
     Use this skill when... (state concrete situational triggers in third-person).
   ---
   ```
3. Add `references/` and `examples/` subdirectories.
4. Run the validation suite to ensure zero broken links and strict frontmatter compliance:
   ```bash
   python scripts/validate_skills.py
   ```

---

## Attribution & Licenses

This project synthesizes research and architectural methodologies from renowned open-source repositories:
- `obra/superpowers` (MIT License)
- `nextlevelbuilder/ui-ux-pro-max-skill` (MIT License)
- `OWASP/wstg` (CC-BY-SA-4.0)
- `anthropics/skills`
- `addyosmani/agent-skills` (MIT License)

See [`ATTRIBUTION.md`](./ATTRIBUTION.md) for complete details.

---

## License

Released under the [MIT License](./LICENSE) by **klein-sys**.
