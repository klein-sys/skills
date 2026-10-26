# Conventional Commits Reference Guide

## Commit Format

```
<type>(<scope>): <short imperative description>

[Optional longer body explaining why the change was made and the context]

[Optional footer(s)]
```

### Commit Types

| Type | Purpose | SemVer Impact | Example |
| :--- | :--- | :--- | :--- |
| **`feat`** | Introduces a new feature or user capability | MINOR (0.x.0) | `feat(auth): add OAuth2 refresh token rotation` |
| **`fix`** | Patches a bug or regression | PATCH (0.0.x) | `fix(cart): prevent negative quantity on item decrement` |
| **`refactor`** | Code change that neither fixes a bug nor adds a feature | None | `refactor(db): extract connection pool into singleton` |
| **`test`** | Adding missing tests or correcting existing tests | None | `test(order): add edge-case tests for zero-tax orders` |
| **`perf`** | Code change that improves performance | PATCH | `perf(search): add composite index on tenant_id and created_at` |
| **`docs`** | Documentation changes only | None | `docs(readme): update quickstart with Docker instructions` |
| **`style`** | Code formatting, missing semicolons, whitespace | None | `style: format imports according to PEP 8` |
| **`chore`** | Build tasks, package updates, repository maintenance | None | `chore(deps): bump pydantic from 2.5.0 to 2.6.0` |
| **`ci`** | CI/CD configuration files and scripts | None | `ci(github): add matrix testing for Python 3.11 and 3.12` |

### Breaking Changes

Indicate a breaking change by appending `!` after the type/scope or adding `BREAKING CHANGE:` in the footer:

```
feat(api)!: drop support for v1 XML payload schema

BREAKING CHANGE: The /api/v1/orders endpoint now accepts JSON only. XML support has been completely removed.
```
