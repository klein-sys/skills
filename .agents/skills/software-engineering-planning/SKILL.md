---
name: software-engineering-planning
description: >-
  Use this skill when starting a new feature, refactoring a subsystem, or designing software architecture.
  Guides the agent through requirements elicitation, technical specification, modular design, phased task
  breakdown with verification criteria, and Architecture Decision Records (ADRs).
---

# Software Engineering & Project Planning

This skill guides you through methodical software engineering and project planning. Rather than jumping directly into writing code, it enforces deliberate architecture, risk-first sequencing, YAGNI, and verifiable task breakdowns.

---

## When to Activate This Skill

- When starting a new project, microservice, library, or feature module.
- When an existing feature requires architectural redesign, refactoring, or database migration.
- When a task description is open-ended or ambiguous and requires discovery before implementation.
- When preparing an implementation roadmap or technical specification for review.

---

## Core Planning Workflow

Follow this phased approach sequentially:

```
[Phase 1: Discover & Clarify]
          │
          ▼
[Phase 2: Architectural Specification]
          │
          ▼
[Phase 3: Risk & Dependency Mapping]
          │
          ▼
[Phase 4: Phased Task Breakdown with DoD]
          │
          ▼
[Phase 5: User Alignment & Sign-off]
```

### Phase 1: Discover & Clarify
1. **Identify the Core Problem**: Formulate a 1-2 sentence problem statement. What user need or business pain does this solve?
2. **Determine Non-Goals**: Explicitly define what is *out of scope* to prevent scope creep.
3. **Analyze Existing Codebase & Constraints**:
   - Inspect active frameworks, versions, database schemas, and conventions.
   - Respect existing architectural patterns unless the brief explicitly calls for a change.
4. **Clarify Ambiguities**: If requirements conflict or are underspecified, formulate precise questions with recommended defaults.

### Phase 2: Architectural Specification
1. **Design System Boundaries & Interfaces**:
   - Define contracts (APIs, function signatures, data models) before internal implementations.
   - Adhere to SOLID and Clean Architecture principles.
2. **Apply Design Heuristics**:
   - **YAGNI (You Aren't Gonna Need It)**: Implement what is required now; avoid speculative abstractions.
   - **DRY (Don't Repeat Yourself)**: Eliminate duplicate domain logic, but favor duplication over the wrong abstraction.
   - **Separation of Concerns**: Decouple domain logic from I/O, UI, and external third-party SDKs.
3. **Capture Trade-offs with ADRs**:
   - If choosing between technologies, data structures, or patterns, draft an Architecture Decision Record using [ADR Template](./references/adr-template.md).

### Phase 3: Risk & Dependency Mapping
1. **Identify Technical Unknowns**: Flag third-party API limits, concurrency bottlenecks, or migration risks.
2. **Front-load Risk**: Order tasks so high-risk spikes and core interface contracts are completed first.
3. **Security & Privacy Baseline**: Check authentication, data classification, and regulatory requirements early.

### Phase 4: Phased Task Breakdown
1. Break the project into small, logical phases (e.g., Foundations -> Core Engine -> Integration -> UI/CLI -> Polish).
2. Each task must be:
   - **Atomic**: Capable of being implemented and tested independently.
   - **Measurable**: Associated with a definitive automated or manual test.
   - **Scoped**: Sized for incremental verification (typically 1-3 files modified per step).
3. Specify the **Definition of Done (DoD)** for each task:
   - Unit tests written and passing.
   - Static analysis / linter clean.
   - Documentation or changelog updated.

---

## References & Templates

- [Architecture Specification Template](./references/architecture-spec-template.md)
- [Architecture Decision Record (ADR) Template](./references/adr-template.md)
- [Real-world Task Breakdown Example](./examples/task-breakdown-example.md)

---

## Verification & Sign-off Checklist

Before presenting the plan to the user or proceeding to code execution, verify:

- [ ] Problem statement and non-goals are clearly stated.
- [ ] Technical design specifies concrete contracts (types, schemas, interfaces).
- [ ] Every task in the breakdown has an explicit verification command or test.
- [ ] High-risk components are scheduled ahead of cosmetic or dependent features.
- [ ] The user has reviewed and explicitly approved the plan.
