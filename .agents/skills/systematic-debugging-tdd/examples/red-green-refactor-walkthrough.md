# Walkthrough: Red-Green-Refactor in Action

This scenario demonstrates resolving a currency rounding bug using pure TDD.

---

### Step 1: The Failing Test (RED)
A user reports that splitting $10.00 among 3 participants yields $3.33 each, losing 1 cent ($9.99 total).

```python
# tests/test_billing.py
from billing import split_amount

def test_split_amount_distributes_remainder_cents_equally():
    # 1000 cents split 3 ways -> [334, 333, 333]
    result = split_amount(total_cents=1000, parts=3)
    assert sum(result) == 1000
    assert result == [334, 333, 333]
```

Run test:
```bash
pytest tests/test_billing.py
# Output: FAILED - assert [333, 333, 333] == [334, 333, 333] (sum 999 != 1000)
```
*Verification: Test failed for the exact expected reason.*

---

### Step 2: Minimal Implementation (GREEN)

```python
# billing.py
def split_amount(total_cents: int, parts: int) -> list[int]:
    base, remainder = divmod(total_cents, parts)
    return [base + (1 if i < remainder else 0) for i in range(parts)]
```

Run test:
```bash
pytest tests/test_billing.py
# Output: PASSED
```

---

### Step 3: Refactor & Boundary Testing

Now test edge cases:
- `parts == 0` (raises `ValueError`)
- `total_cents == 0` (returns all zeros)
- Negative amounts

Add tests:
```python
import pytest

def test_split_amount_zero_parts_raises():
    with pytest.raises(ValueError, match="parts must be > 0"):
        split_amount(1000, 0)
```

Update implementation to validate inputs:
```python
def split_amount(total_cents: int, parts: int) -> list[int]:
    if parts <= 0:
        raise ValueError("parts must be > 0")
    base, remainder = divmod(total_cents, parts)
    return [base + (1 if i < remainder else 0) for i in range(parts)]
```

Run entire test suite:
```bash
pytest
# Output: All 12 tests passed.
```
