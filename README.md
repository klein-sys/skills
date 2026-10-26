# AI Agent Skills Repository (`klein-sys/skills`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Platform: Antigravity & Gemini](https://img.shields.io/badge/Platform-Antigravity%20%7C%20Gemini-green.svg)](#compatibility)
[![Architecture: Modular Categories](https://img.shields.io/badge/Architecture-Modular%20Categories-purple.svg)](#repository-categories)

A modular, multi-category AI coding agent skill repository for **Google Antigravity**, **Gemini**, and multi-agent harnesses.

Every domain is packaged in its own dedicated, self-contained category folder, allowing you to add new skills and skill categories in the future without cluttering the repository.

---

## Repository Structure & Categories

```
klein-sys/skills/
├── software-dev/                      # Core Software Engineering, AppSec & UI/UX Pack
│   ├── accessibility-responsive-design/
│   ├── authorized-web-security-testing/
│   ├── code-review-qa/
│   ├── git-github-workflows/
│   ├── secure-coding-review/
│   ├── software-engineering-planning/
│   ├── systematic-debugging-tdd/
│   ├── ui-ux-design-systems/
│   ├── scripts/validate_skills.py
│   ├── README.md                      # Category guide & installation manual
│   ├── ATTRIBUTION.md                 # Open-source research & license attribution
│   ├── COMPATIBILITY_REPORT.md        # Technical agent compatibility report
│   └── VALIDATION_CHECKLIST.md        # Structural validation matrix
│
├── flashdock-skills/                  # All 50 skills from FlashDock/.agents/skills
│   ├── flashdock-workstation/         # Zero-brick protocols, QThread async & design tokens
│   ├── android-cli/                   # Android CLI, ADB, Fastboot & AVD emulator tools
│   ├── engineering/                   # to-spec, to-tickets, triage, implement, code-review
│   ├── productivity/                  # grill-me, grilling, handoff, teach, wait-what
│   ├── in-progress/                   # loop-me, chief-of-staff, claude-handoff, writing
│   ├── misc/                          # git-guardrails, setup-pre-commit, scaffold
│   └── README.md                      # FlashDock skills guide
│
├── skills-from-github/                # Full upstream repo from FlashDock/.agents/skills-from github
│   ├── skills/                        # All skills organized by namespace
│   ├── docs/                          # Guides and reference documentation
│   ├── scripts/                       # Upstream helper scripts
│   ├── package.json                   # Package configuration
│   └── README.md                      # Matt Pocock (mattpocock/skills) original documentation
│
├── scripts/
│   └── validate_all.py                # Master validator testing category packages
├── README.md                          # Repository hub index
└── LICENSE                            # MIT License
```

---

## Active Skill Packs

### 1. [`software-dev/`](./software-dev/) — Software Engineering & Design Systems
Comprehensive standards for full-stack engineering, test-driven development, application security reviews (STRIDE / OWASP Top 10), ethical web security testing (WSTG v4.2), design systems, accessibility (WCAG 2.1 AA), and multi-tier code reviews.
- *See [software-dev README](./software-dev/README.md).*

### 2. [`flashdock-skills/`](./flashdock-skills/) — FlashDock Workstation & Device Tools
All 50 skills installed and created for FlashDock development, including `flashdock-workstation` (zero-brick guarantees, radio calibration backups, `QThread` async workers), `android-cli` (ADB/Fastboot and Android SDK CLI tooling), and productivity/engineering workflows.
- *See [flashdock-skills README](./flashdock-skills/README.md).*

### 3. [`skills-from-github/`](./skills-from-github/) — Upstream Agent Skills Package
The complete upstream repository package from `FlashDock\.agents\skills-from github` originated from **Matt Pocock's Agent Skills** ([mattpocock/skills](https://github.com/mattpocock/skills)), including all documentation, docs, scripts, and skills.
- *See [skills-from-github README](./skills-from-github/README.md).*

---

## Adding New Categories in the Future

To add a new category (e.g., `cloud-infra/`, `ai-ml/`, `devops/`):
1. **Create your new category folder**:
   ```bash
   mkdir cloud-infra
   ```
2. **Add skills in Antigravity format**:
   ```text
   cloud-infra/
   ├── terraform-deploy/
   │   ├── SKILL.md
   │   ├── references/
   │   └── examples/
   └── README.md
   ```
3. **Commit and push**:
   ```bash
   git add cloud-infra/
   git commit -m "feat(skills): add cloud-infra category pack"
   git push
   ```

---

## License

Released under the [MIT License](./LICENSE) by **klein-sys**.
