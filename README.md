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
│   ├── scripts/                       # Validator for software-dev
│   ├── README.md                      # Category guide & installation manual
│   ├── ATTRIBUTION.md                 # Open-source research & license attribution
│   ├── COMPATIBILITY_REPORT.md        # Technical agent compatibility report
│   └── VALIDATION_CHECKLIST.md        # Structural validation matrix
│
├── flashdock/                         # FlashDock Workstation & Android Device Tools
│   ├── flashdock-workstation/         # Zero-brick protocols, QThread async & design tokens
│   ├── android-cli/                   # Android CLI, ADB, Fastboot & AVD emulator tools
│   ├── scripts/                       # Validator for flashdock
│   └── README.md                      # FlashDock category guide
│
├── agent-productivity/                # Agent Workflow Loops & Engineering Lifecycles
│   ├── productivity/                  # grill-me, grilling, handoff, teach, wait-what
│   ├── engineering/                   # to-spec, to-tickets, triage, implement, code-review
│   ├── in-progress/                   # loop-me, chief-of-staff, claude-handoff, writing
│   ├── misc/                          # git-guardrails, setup-pre-commit, scaffold
│   ├── scripts/                       # Validator for agent-productivity
│   ├── ATTRIBUTION.md                 # Matt Pocock (mattpocock/skills) attribution
│   └── README.md                      # Agent productivity guide
│
├── README.md                          # Repository hub index
└── LICENSE                            # MIT License
```

---

## Active Skill Packs

### 1. [`software-dev/`](./software-dev/) — Software Engineering & Design Systems
Comprehensive standards for full-stack engineering, test-driven development, application security reviews (STRIDE / OWASP Top 10), ethical web security testing (WSTG v4.2), design systems, accessibility (WCAG 2.1 AA), and multi-tier code reviews.
- *See [software-dev README](./software-dev/README.md).*

### 2. [`flashdock/`](./flashdock/) — FlashDock & Android Workstation Standards
Architectural rules, zero-brick safety guarantees, radio calibration backups (`efs`, `nvram`, `persist`), AVB/ARP anti-rollback guards, `QThread` async worker lifecycles, and Android device CLI tools (`adb`, `fastboot`, `android`).
- *See [flashdock README](./flashdock/README.md).*

### 3. [`agent-productivity/`](./agent-productivity/) — Agent Workflows & Interaction Loops
Originated from **Matt Pocock's Agent Skills** ([mattpocock/skills](https://github.com/mattpocock/skills)). Powers interactive `/grill-me` requirement interviews, context handoffs, issue triage, technical specs (`to-spec`, `to-tickets`), and task execution loops.
- *See [agent-productivity README](./agent-productivity/README.md).*

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

## Installation & Enabling Skills in Your Agent

### Method 1: Project Workspace (.agents/skills)
Copy any category's skills into your project workspace:
```powershell
$project = "C:\Path\To\YourProject"
New-Item -ItemType Directory -Force -Path "$project\.agents\skills"

# Example: Copy software-dev or flashdock skills:
Copy-Item -Recurse -Force "software-dev\*" "$project\.agents\skills\"
```

### Method 2: Global Configuration (~/.gemini/config/skills)
To make skills available globally across all conversations:
```powershell
$global = "$env:USERPROFILE\.gemini\config\skills"
New-Item -ItemType Directory -Force -Path $global
Copy-Item -Recurse -Force "software-dev\*" "$global\"
```

---

## License

Released under the [MIT License](./LICENSE) by **klein-sys**.
