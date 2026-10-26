# Software Development Skills Pack (`software-dev/`)

This directory houses the foundational software engineering, quality assurance, application security, and user experience skills for AI coding agents.

---

## Included Skills

| Skill | Focus | Key Workflow |
| :--- | :--- | :--- |
| **[`software-engineering-planning`](./software-engineering-planning/SKILL.md)** | Architecture & Planning | Discovery -> Tech Spec -> Risk & Dependency Mapping -> Atomic Task Breakdown with DoD -> ADRs. |
| **[`systematic-debugging-tdd`](./systematic-debugging-tdd/SKILL.md)** | Debugging & TDD | 4-Phase Diagnosis (Reproduce -> Trace Invariants -> Failing Regression Test -> Minimal Fix & Refactor). |
| **[`git-github-workflows`](./git-github-workflows/SKILL.md)** | Git & GitHub | Conventional Commits, branch hygiene, safe rebasing, `git worktree` isolation, PR readiness reviews. |
| **[`secure-coding-review`](./secure-coding-review/SKILL.md)** | Application Security | Component trust boundaries, STRIDE threat modeling, OWASP Top 10 code defenses, zero secret leakage. |
| **[`authorized-web-security-testing`](./authorized-web-security-testing/SKILL.md)** | Ethical Web Security | Strict scope authorization verification, non-destructive OWASP WSTG v4.2 test procedures, CVSS scoring. |
| **[`ui-ux-design-systems`](./ui-ux-design-systems/SKILL.md)** | UI/UX & Design Systems | Distinct aesthetic themes, 3-tier CSS design tokens, typography pairings, bento layouts, anti-generic rules. |
| **[`accessibility-responsive-design`](./accessibility-responsive-design/SKILL.md)** | Responsive & Accessibility | Mobile-first CSS Grid/flexbox, fluid clamp typography, WCAG 2.1 Level AA compliance, keyboard focus traps. |
| **[`code-review-qa`](./code-review-qa/SKILL.md)** | Code Review & QA Gates | 6-dimension review scorecard (Correctness, Security, Reliability, Tests, Maintainability, Scale), CI gates. |

---

## Progressive Disclosure Structure

Each skill folder follows the Antigravity specification:
- `SKILL.md`: Main instructions with YAML frontmatter (`name`, `description`).
- `references/`: In-depth templates, threat models, and design standards loaded on demand.
- `examples/`: Realistic walkthroughs, sample audits, and reference implementations.
