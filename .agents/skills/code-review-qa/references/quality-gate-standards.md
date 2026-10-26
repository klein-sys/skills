# Quality Gate Standards & CI Checkpoints

A production quality gate represents the non-negotiable minimum criteria that any code change must satisfy before entering the main branch.

---

## 1. Automated CI Quality Gates

Every pull request build must pass:

1. **Clean Compilation / Build**:
   - Zero syntax errors or unresolved imports.
2. **Static Type Checking**:
   - `mypy --strict`, `tsc --noEmit`, or equivalent language type checker passes with zero errors.
3. **Linter & Formatter**:
   - ESLint, Ruff, or Black pass with zero warnings and correct formatting.
4. **Automated Test Execution**:
   - 100% of existing and new automated tests must pass.
   - Zero skipped or flaky tests without an open issue ticket.
5. **Secret Scanner**:
   - GitGuardian, Gitleaks, or Trufflehog confirms zero exposed credentials or high-entropy tokens.
6. **Dependency Security Scan**:
   - `npm audit` / `pip-audit` / `govulncheck` shows zero High or Critical vulnerabilities.

---

## 2. Human / Agent Review Quality Gates

Before merging:
- At least one thorough code review approval is recorded.
- Every `[Blocker]` comment has been addressed, retested, and resolved.
- Definition of Done (DoD) from the engineering plan is completely satisfied.
- Changelog and documentation reflect all public API changes.
