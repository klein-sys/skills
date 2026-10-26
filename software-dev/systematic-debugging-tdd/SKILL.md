---
name: systematic-debugging-tdd
description: >-
  Use this skill when investigating bugs, broken tests, unexpected runtime errors, or when implementing
  features using test-driven development (TDD). Enforces a 4-phase root-cause diagnosis protocol and true
  Red-Green-Refactor test discipline.
---

# Systematic Debugging & Test-Driven Development (TDD)

This skill provides an ironclad discipline for debugging complex issues and building software via Test-Driven Development (TDD). It bans speculative patching and enforces root-cause verification and regression test prevention.

---

## When to Activate This Skill

- When a bug report, exception, stack trace, or failing test is encountered.
- When existing code exhibits unexpected or intermittent behavior (race conditions, memory leaks, wrong state).
- When developing new modules where strict correctness and regression safety are required.
- When refactoring legacy code where tests must guarantee behavior preservation.

---

## Part 1: The 4-Phase Systematic Debugging Protocol

Do **not** edit production code until Phases 1 through 3 are complete:

```
[Phase 1: Reproduce & Isolate]
              │
              ▼
[Phase 2: Trace & Identify Invariant Violation]
              │
              ▼
[Phase 3: Formulate Hypothesis & Write Failing Regression Test]
              │
              ▼
[Phase 4: Implement Minimal Fix & Refactor]
```

### Phase 1: Reproduce & Isolate
1. **Create Minimal Reproduction**: Strip away extraneous dependencies, inputs, or concurrency until the smallest reproducible case is found.
2. **Determine Determinism**: Check if the bug is 100% deterministic, load-dependent, timing-dependent, or environment-dependent.
3. **Capture Inputs & Environment**: Record exact inputs, OS, environment variables, and dependencies.

### Phase 2: Trace & Identify Invariant Violation
1. **Trace Data Flow**: Follow inputs from system entry to the point of failure.
2. **Inspect State Invariants**: Which assumption or invariant broke? (e.g., null dereference, off-by-one, type mismatch, stale cache, race condition).
3. **Never Guess**: If uncertain, add targeted diagnostic logs or inspect with a debugger rather than randomly modifying code.

### Phase 3: Failing Regression Test (Red)
1. Write an automated test that reproduces the bug in isolation.
2. Run the test and verify:
   - **It must fail**.
   - **It must fail for the exact reason identified in Phase 2** (not an unrelated setup error).

### Phase 4: Minimal Fix & Refactor (Green -> Refactor)
1. Implement the simplest, most direct fix that addresses the root cause without side effects.
2. Run the regression test: verify it now passes.
3. Run the full test suite: verify zero collateral regressions.
4. Refactor any duplicated or tangled code while keeping all tests green.

---

## Part 2: True Test-Driven Development (TDD) Workflow

When creating new features, follow the **Red-Green-Refactor** cycle:

1. **Write One Failing Test (Red)**:
   - Test a single unit of behavior or edge condition.
   - Run the test suite; confirm the test fails as expected.
2. **Write Minimal Production Code (Green)**:
   - Write only enough code to make the test pass.
   - Do not add hypothetical features or over-engineer.
3. **Refactor**:
   - Clean up naming, remove duplication, and optimize structure.
   - Keep all tests passing.
4. **Repeat**:
   - Move to the next boundary condition or edge case (nulls, empty inputs, limits, error paths).

---

## References & Guides

- [Root-Cause Analysis Framework](./references/root-cause-framework.md)
- [TDD Discipline & Test Quality Standards](./references/tdd-discipline.md)
- [Red-Green-Refactor Step-by-Step Walkthrough](./examples/red-green-refactor-walkthrough.md)

---

## Verification Checklist

Before marking any bug as resolved or feature as complete:

- [ ] A dedicated regression test exists that isolates the bug or feature.
- [ ] The test was observed to fail before the fix was introduced.
- [ ] The fix resolves the root cause rather than merely masking the symptom.
- [ ] The entire project test suite passes cleanly.
- [ ] No temporary debugging code, console print statements, or debug flags remain.
