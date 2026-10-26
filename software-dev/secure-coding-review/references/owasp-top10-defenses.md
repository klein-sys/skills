# OWASP Top 10 Secure Coding Patterns

## 1. A01: Broken Access Control
- **Defect**: Direct object references without verifying ownership (`SELECT * FROM orders WHERE id = :id`).
- **Defense**: Scope every query to the authenticated tenant/user:
  ```python
  # Safe
  query = db.query(Order).filter(Order.id == order_id, Order.user_id == current_user.id)
  ```

## 2. A02: Cryptographic Failures
- **Defect**: Using MD5/SHA-1 for passwords or storing plain secrets.
- **Defense**:
  ```python
  from argon2 import PasswordHasher
  ph = PasswordHasher()
  hashed = ph.hash(plain_password)
  # Verification:
  ph.verify(hashed, candidate_password)
  ```

## 3. A03: Injection
- **Defect**: String formatting in SQL or shell:
  ```python
  # Vulnerable!
  cursor.execute(f"SELECT * FROM users WHERE email = '{user_input}'")
  ```
- **Defense**:
  ```python
  # Safe Parameterization
  cursor.execute("SELECT * FROM users WHERE email = %s", (user_input,))
  ```

## 4. A05: Security Misconfiguration
- **Defect**: Debug mode enabled in production, default credentials, verbose stack traces exposed to clients.
- **Defense**: Centralized environment configuration with strict validation. Catch unhandled exceptions and return an opaque correlation ID (`{"error": "Internal error", "request_id": "abc-123"}`).

## 5. A10: Server-Side Request Forgery (SSRF)
- **Defect**: Fetching arbitrary user-provided URLs.
- **Defense**: Validate URL scheme (must be `https://`), resolve DNS, and block private IP ranges (RFC 1918, RFC 3927, loopback `127.0.0.1`, cloud metadata `169.254.169.254`).
