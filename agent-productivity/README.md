# Agent Productivity & Workflow Skills (`agent-productivity/`)

This directory houses the comprehensive collection of agent workflow, interaction loop, and real-world engineering skills originated by **Matt Pocock** ([mattpocock/skills](https://github.com/mattpocock/skills)) and curated for coding agents.

Organized across distinct namespaces to support interactive interview workflows, specification drafting, bug triage, and autonomous task execution.

---

## Namespaces & Skill Catalog

### 1. `productivity/` — Interaction Loops & Clarification
Core skills that govern the interview, clarification, and handoff lifecycle:

| Skill | Description |
| :--- | :--- |
| **`grill-me`** | Interactive interview protocol that walks down decision trees one question at a time before coding begins. |
| **`grilling`** | Deep-dive questioning framework for resolving ambiguous product requirements. |
| **`handoff`** | Serializes session context and outstanding tasks for seamless handoff across turns or subagents. |
| **`teach`** | Interactive instructional skill explaining concepts, tradeoffs, and system architecture step-by-step. |
| **`to-questionnaire`** | Converts underspecified tasks into structured multiple-choice questionnaires. |
| **`wait-what`** | Pauses execution when assumptions break or conflicting instructions are detected. |
| **`writing-for-agents`** | Guidelines for writing concise, token-efficient markdown documentation optimized for AI agents. |

---

### 2. `engineering/` — Specification & Implementation Lifecycles
Methodical engineering workflows for architecture, research, implementation, and code reviews:

| Sub-Domain | Skills Included |
| :--- | :--- |
| **Requirements & Specs** | `to-spec`, `to-tickets`, `triage`, `grill-with-docs`, `domain-modeling` |
| **Implementation & TDD** | `implement`, `implement-spec`, `prototype`, `tdd`, `wizard`, `wayfinder` |
| **Review & Quality** | `code-review`, `improve-codebase-architecture`, `diagnosing-bugs`, `pr`, `retro` |
| **Knowledge & Setup** | `ask-matt`, `research`, `setup-matt-pocock-skills` |

---

### 3. `in-progress/` & `misc/` — Advanced Workflows & Guardrails
- **`in-progress/`**: Emerging workflows including `loop-me`, `chief-of-staff`, `claude-handoff`, `setup-ts-deep-modules`, and structured writing skills (`writing-beats`, `writing-fragments`, `writing-shape`).
- **`misc/`**: Version control guardrails and dev tooling (`git-guardrails-claude-code`, `setup-pre-commit`, `scaffold-exercises`, `migrate-to-shoehorn`).
- **Core Utilities**: `Readme-gen`, `find-skills`, `permissioned-github`, `agy-customizations`, `antigravity_guide`.

---

## Attribution & License

- Original Author: **Matt Pocock** ([@mattpocock](https://github.com/mattpocock))
- Source: [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)
- License: **MIT License** (See [`ATTRIBUTION.md`](./ATTRIBUTION.md))

---

## How to Install in Your Agent

```powershell
# Copy productivity skills to your project workspace:
$project = "C:\Path\To\YourProject"
New-Item -ItemType Directory -Force -Path "$project\.agents\skills"
Copy-Item -Recurse -Force "agent-productivity\*" "$project\.agents\skills\"
```
