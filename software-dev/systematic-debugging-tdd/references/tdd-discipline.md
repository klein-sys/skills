# Test-Driven Development (TDD) Discipline & Standards

## Principles of Robust Automated Testing

1. **Test Behavior, Not Internal Implementation**:
   - Test against public interfaces and observable outputs.
   - Avoid mocking private methods or verifying internal variables, which makes tests brittle to refactoring.
2. **The FIRST Principles**:
   - **Fast**: Tests execute in milliseconds so developers run them continuously.
   - **Isolated / Independent**: Tests do not depend on execution order or shared mutable global state.
   - **Repeatable**: Tests yield the exact same result in any environment without flakiness.
   - **Self-Validating**: Tests produce a binary Pass/Fail output with no manual log inspection.
   - **Timely**: Tests are written immediately before or alongside the production code.

## Test Pyramid Allocation

- **70% Unit Tests**: Fast, in-memory tests verifying single classes or functions with mocked external I/O.
- **20% Integration Tests**: Verifying contracts between real database adapters, file systems, or API clients.
- **10% End-to-End (E2E) Tests**: Critical journey verification through entrypoint down to data storage.

## Test Naming Standard

Use the pattern: `test_<method_or_unit>_<scenario>_<expected_behavior>()`

```python
# Example
def test_withdraw_insufficient_balance_raises_overdraft_error():
    ...
```
