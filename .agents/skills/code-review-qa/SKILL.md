---
name: code-review-qa
description: >-
  Use this skill when reviewing code, assessing pull requests, verifying software quality, or conducting
  pre-release QA. Enforces a multi-dimensional review scorecard covering functional correctness, security,
  performance, test adequacy, maintainability, and constructive feedback formatting.
---

# Code Review & Quality Assurance (QA)

This skill acts as a principal engineer and QA lead. It conducts rigorous, multi-dimensional code reviews and ensures that code changes meet production quality gates before being merged.

---

## When to Activate This Skill

- When reviewing a git diff, branch, or Pull Request before merging.
- When performing a self-review of your own code prior to requesting human approval.
- When auditing test coverage, edge-case resilience, or error-handling paths.
- When establishing quality standards and linting/formatting rules for a project.

---

## Multi-Dimensional Review Protocol

Do not focus solely on syntax or formatting. Evaluate changes across the 6 dimensions of quality:

```
                  [1. Correctness & Logic]
                             │
     ┌───────────────────────┼───────────────────────┐
     ▼                       ▼                       ▼
[2. Security]         [3. Performance]      [4. Maintainability]
     ▲                       ▲                       ▲
     └───────────────────────┼───────────────────────┘
                             │
                 [5. Test Coverage & FIRST]
                             │
                  [6. Quality Gate Verdict]
```

### Dimension 1: Correctness & Boundary Conditions
- Does the code fulfill the functional specification without subtle logic bugs?
- Are boundary conditions handled? (empty arrays, `null`/`undefined`, zero, max integers, unicode).
- Are error handling and exception flows properly trapped and clean?

### Dimension 2: Security & Trust Boundaries
- Is untrusted input sanitized and validated before use?
- Are parameterized database queries used exclusively?
- Are authorization checks verified at the data layer (no IDOR/BOLA)?
- Are credentials, tokens, or internal URLs exposed?

### Dimension 3: Performance & Resource Lifecycle
- Are database queries efficient? (Watch for N+1 queries, missing indexes).
- Are connections, file handles, streams, and timers properly closed/disposed in `finally` blocks?
- Is memory bounded? (Avoid unbounded in-memory caches or reading huge files entirely into RAM).

### Dimension 4: Architecture & Maintainability
- Does the change follow existing project conventions and patterns?
- Is the code self-documenting with clear names? Are non-obvious algorithms explained?
- Does it adhere to YAGNI and DRY without over-abstracting?

### Dimension 5: Test Coverage & Assertions
- Are new features backed by unit or integration tests?
- Do tests test *behavior* rather than private implementation details?
- Do assertions verify edge conditions and failure states, not just the happy path?

### Dimension 6: Structured Feedback Delivery
Format comments with clear severity prefixes:
- `[Blocker]`: Must be fixed before merge (bugs, security flaws, missing critical tests).
- `[Suggestion]`: Recommended improvement; non-blocking.
- `[Question]`: Seeking clarification on design intent or trade-offs.
- `[Praise]`: Recognizing elegant solutions or thorough test coverage.
Provide concrete replacement code blocks with rationale.
See [Multi-Tier Review Framework](./references/multi-tier-review-framework.md).

---

## References & Guides

- [Multi-Tier Code Review Framework](./references/multi-tier-review-framework.md)
- [Quality Gate Standards & CI Checkpoints](./references/quality-gate-standards.md)
- [Constructive Code Review Feedback Example](./examples/code-review-feedback-example.md)

---

## Verification Checklist

Before issuing a final code review verdict:

- [ ] Every modified file in the diff was inspected completely.
- [ ] Automated tests pass and cover both happy path and failure scenarios.
- [ ] No regressions, security vulnerabilities, or resource leaks were identified.
- [ ] All comments are constructive, specific, and accompanied by actionable recommendations.
- [ ] A definitive verdict is rendered: `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`.
