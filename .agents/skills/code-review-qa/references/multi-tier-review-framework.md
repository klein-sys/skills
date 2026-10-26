# Multi-Tier Code Review Framework

## The 6 Quality Dimensions Scorecard

Use this scorecard when evaluating any pull request or substantial commit:

| Quality Dimension | Weight | Primary Questions | Red Flags |
| :--- | :--- | :--- | :--- |
| **1. Functional Correctness** | Critical | Does the change solve the problem? Are edge cases handled? | Off-by-one errors, unhandled nulls, swallowing exceptions silently. |
| **2. Security & Safety** | Critical | Are trust boundaries respected? Are secrets protected? | SQL string concatenation, unescaped HTML, missing auth checks. |
| **3. Reliability & Leaks** | High | Are resources properly released? Is concurrency safe? | Missing `finally` blocks, unbounded memory arrays, race conditions. |
| **4. Test Quality** | High | Are new behaviors verified? Are assertions meaningful? | Tests without assertions, tests mocking the unit under test. |
| **5. Maintainability** | Medium | Is the code readable? Are names descriptive? | Functions > 50 lines, deeply nested conditionals (> 3 levels), dead code. |
| **6. Performance & Scale** | Medium | Will this scale under production load? | N+1 database queries, synchronous blocking I/O on async loops. |

---

## Actionable Review Comment Syntax

Avoid vague criticism like *"This looks messy."* or *"Fix this."* Always follow the format:

```
[Severity] Location: What the problem is.
Why: Explanation of risk, bug, or impact.
Recommendation: Concrete fix with code block.
```

### Example:
> **[Blocker]** `src/services/billing.py:L45`: The `db_session` is not closed if an exception occurs during charge processing.
> **Why**: Under heavy traffic or network timeouts from the payment gateway, unclosed database sessions will exhaust the connection pool, crashing the service.
> **Recommendation**: Wrap in a context manager:
> ```python
> with get_db_session() as session:
>     session.execute(...)
> ```
