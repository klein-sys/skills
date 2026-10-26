# AI Agent Skills Repository (`klein-sys/skills`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Platform: Antigravity & Gemini](https://img.shields.io/badge/Platform-Antigravity%20%7C%20Gemini-green.svg)](#compatibility)
[![Architecture: Modular Categories](https://img.shields.io/badge/Architecture-Modular%20Categories-purple.svg)](#repository-structure)

A modular, multi-category AI coding agent skill repository for **Google Antigravity**, **Gemini**, and multi-agent harnesses.

Every domain is packaged in its own dedicated, self-contained category folder, allowing you to add new skills and skill categories in the future without cluttering the repository.

---

## Repository Structure

```
klein-sys/skills/
├── software-dev/                      # All software development skills & docs
│   ├── accessibility-responsive-design/
│   ├── authorized-web-security-testing/
│   ├── code-review-qa/
│   ├── git-github-workflows/
│   ├── secure-coding-review/
│   ├── software-engineering-planning/
│   ├── systematic-debugging-tdd/
│   ├── ui-ux-design-systems/
│   ├── scripts/                       # Validator for software-dev skills
│   ├── README.md                      # Category guide & instructions
│   ├── ATTRIBUTION.md                 # Open-source research & license attribution
│   ├── COMPATIBILITY_REPORT.md        # Technical agent compatibility report
│   └── VALIDATION_CHECKLIST.md        # Structural validation matrix
│
├── <future-category>/                 # Future skill categories (e.g., android-dev, cloud-infra)
├── README.md                          # Repository hub index & guide
└── LICENSE                            # MIT License
```

---

## Active Skill Categories

### 1. [`software-dev/`](./software-dev/) — Software Development & Quality Pack
A complete, production-grade skill suite for senior software engineering, quality assurance, application security, and UI/UX design:

- **[`software-engineering-planning`](./software-dev/software-engineering-planning/SKILL.md)**: Architectural specs, risk sequencing, ADRs, and phased task breakdowns with Definition of Done.
- **[`systematic-debugging-tdd`](./software-dev/systematic-debugging-tdd/SKILL.md)**: 4-phase root cause diagnosis protocol and Red-Green-Refactor test discipline.
- **[`git-github-workflows`](./software-dev/git-github-workflows/SKILL.md)**: Conventional Commits, branch hygiene, safe rebasing, and `git worktree` context switching.
- **[`secure-coding-review`](./software-dev/secure-coding-review/SKILL.md)**: Trust boundary identification, STRIDE threat modeling, and OWASP Top 10 code defenses.
- **[`authorized-web-security-testing`](./software-dev/authorized-web-security-testing/SKILL.md)**: Ethical penetration testing simulation and non-destructive OWASP WSTG v4.2 verification.
- **[`ui-ux-design-systems`](./software-dev/ui-ux-design-systems/SKILL.md)**: CSS design tokens, typography pairings, bento layouts, and anti-generic design rules.
- **[`accessibility-responsive-design`](./software-dev/accessibility-responsive-design/SKILL.md)**: Mobile-first fluid layouts and WCAG 2.1 Level AA compliance.
- **[`code-review-qa`](./software-dev/code-review-qa/SKILL.md)**: 6-dimension review scorecard (Correctness, Security, Reliability, Tests, Maintainability, Scale).

*See the [software-dev README](./software-dev/README.md) for detailed workflows, templates, and references.*

---

## Adding New Skill Categories in the Future

Because this repository is organized by category folders, you can easily add new skill packs:

1. **Create your new category folder**:
   ```bash
   mkdir android-dev
   ```
2. **Add skills in standard Antigravity format**:
   ```text
   android-dev/
   ├── my-new-skill/
   │   ├── SKILL.md
   │   ├── references/
   │   └── examples/
   └── README.md
   ```
3. **Commit and push**:
   ```bash
   git add android-dev/
   git commit -m "feat(skills): add android-dev category pack"
   git push
   ```

---

## Installation & Enabling Skills in Your Agent

### Method 1: Project Workspace (.agents/skills)
Copy any skill category into your project's `.agents/skills` directory:
```powershell
# Copy software-dev skills into your project workspace:
$project = "C:\Path\To\YourProject"
New-Item -ItemType Directory -Force -Path "$project\.agents\skills"
Copy-Item -Recurse -Force "software-dev\*" "$project\.agents\skills\"
```

### Method 2: Global Configuration (~/.gemini/config/skills)
To make a category's skills available across all projects on your system:
```powershell
$global = "$env:USERPROFILE\.gemini\config\skills"
New-Item -ItemType Directory -Force -Path $global
Copy-Item -Recurse -Force "software-dev\*" "$global\"
```

---

## License

Released under the [MIT License](./LICENSE) by **klein-sys**.
