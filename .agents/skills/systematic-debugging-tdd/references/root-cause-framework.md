# Root-Cause Analysis Framework

Speculative debugging leads to code churn, hidden regressions, and wasted hours. This framework provides a rigorous method for isolating the true root cause.

---

## The "5 Whys" for Software Defects

When a defect occurs, drill down past the immediate symptom:

1. **Symptom**: "The application crashed with a `TypeError: Cannot read properties of undefined`."
   - *Why?* The `user.preferences.theme` lookup failed because `preferences` was undefined.
2. **Immediate Cause**: *Why was `preferences` undefined?*
   - The user record was loaded from the migration pipeline without executing default profile initialization.
3. **Upstream Mechanism**: *Why did the migration pipeline skip initialization?*
   - The bulk insert path bypassed ORM model lifecycle hooks (`before_insert`).
4. **Design Flaw**: *Why does bulk insert bypass lifecycle hooks?*
   - Bulk insertion directly executed raw SQL statements to maximize throughput without applying the schema defaults.
5. **Root Cause**: The database schema lacked a `DEFAULT` constraint or default fallback at the database/repository boundary, allowing orphaned null states.

**Fix**: Do not just add `user?.preferences?.theme ?? 'dark'` in the frontend! Fix the database schema constraint and repository ingestion logic so invalid data cannot exist.

---

## Defect Classification Matrix

| Defect Class | Hallmarks | Diagnostic Technique |
| :--- | :--- | :--- |
| **Logic / Boundary** | Fails on specific inputs (0, empty string, max integer). | Add unit tests testing boundary conditions. |
| **State / Mutability** | Works on step 1, fails on step 5 or after page refresh. | Inspect state mutations and object sharing. |
| **Concurrency / Race** | Intermittent failures, happens only under load. | Trace lock ordering, async/await timing, thread safety. |
| **Environment / Config** | Works locally, fails in CI or production. | Compare environment variables, runtime versions, file paths. |
| **Resource Leak** | Slow degradation, out-of-memory after long uptime. | Inspect open handles, listeners, unclosed DB connections. |
