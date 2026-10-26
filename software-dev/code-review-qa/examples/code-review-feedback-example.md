# Real-World Code Review Feedback Example

### Pull Request Under Review: `feat(export): Add CSV download for telemetry data`

---

### Review Summary
**Verdict: REQUEST_CHANGES**

> Thank you for implementing the CSV export feature! The file formatting and column selection are clean and well-structured. However, there is one critical security issue (CSV injection) and one performance issue with unbounded in-memory streaming that need to be addressed before this can be merged.

---

### Detailed Review Findings

#### 1. [Blocker] CSV Injection Vulnerability
- **File**: `src/exporters/csv_exporter.py:L34`
- **Why**: Cells that begin with formula characters (`=`, `+`, `-`, `@`) are written raw to the CSV. If an attacker inputs `=CMD|' /C calc'!A0` as a project name, spreadsheet applications (Excel, LibreOffice) will execute the command when the CSV is opened by an administrator.
- **Recommendation**: Sanitize leading formula characters by prefixing with a single quote:
  ```python
  def sanitize_cell(value: str) -> str:
      if value and value[0] in ("=", "+", "-", "@", "\t", "\r"):
          return f"'{value}"
      return value
  ```

#### 2. [Blocker] Unbounded Memory Consumption on Large Datasets
- **File**: `src/api/routes/export.py:L58`
- **Why**: The route executes `records = db.query(Telemetry).all()` and buffers all rows into a single in-memory `StringIO` object before returning. For tenants with 500,000+ telemetry rows, this will exhaust server memory (OOM crash).
- **Recommendation**: Use a streaming response with database cursor pagination (`yield_per`):
  ```python
  from fastapi.responses import StreamingResponse

  def generate_csv_chunks():
      yield "timestamp,metric,value\n"
      for record in db.query(Telemetry).yield_per(1000):
          yield f"{record.timestamp},{record.metric},{record.value}\n"

  return StreamingResponse(generate_csv_chunks(), media_type="text/csv")
  ```

#### 3. [Suggestion] Add automated regression test for sanitization
- **File**: `tests/test_csv_exporter.py`
- **Recommendation**: Add a test case verifying that a string starting with `=SUM(A1:A10)` is sanitized to `'=SUM(A1:A10)`.

#### 4. [Praise] Great job on Clean Headers
- **File**: `src/exporters/csv_exporter.py:L12`
- **Note**: The use of explicit metadata headers and RFC 4180 compliant quotation is very clean and readable!
