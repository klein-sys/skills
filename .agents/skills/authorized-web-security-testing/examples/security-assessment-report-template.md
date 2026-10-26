# Security Assessment Findings Report Template

## Executive Summary
- **Target Application**: [App Name]
- **Target URL / Scope**: `http://localhost:3000`
- **Assessment Date**: YYYY-MM-DD
- **Assessment Type**: Authorized White-Box / Gray-Box Web Application Security Review
- **Summary of Findings**: 0 Critical, 1 High, 2 Medium, 1 Low

---

## Detailed Vulnerability Findings

### Finding SEC-01: Insecure Direct Object Reference (IDOR) on Invoices Endpoint
- **Severity**: High (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N - Score: 6.5)
- **WSTG Reference**: WSTG-ATHZ-02 (Testing for BOLA / IDOR)
- **Affected Endpoint**: `GET /api/v1/invoices/{invoice_id}`

#### 1. Description
The application exposes customer invoices through a REST endpoint that accepts an integer invoice identifier. While the user must be authenticated with a valid JWT token, the server does not verify that the invoice belongs to the requesting tenant.

#### 2. Non-Destructive Proof of Concept (PoC)
1. Authenticate as User A (Tenant ID 1001, Session Token A).
2. Request invoice belonging to Tenant ID 1002:
   ```bash
   curl -H "Authorization: Bearer <TOKEN_A>" "http://localhost:3000/api/v1/invoices/8842"
   ```
3. Application responds with HTTP 200 OK containing full billing details of Tenant ID 1002.

#### 3. Root Cause
In `src/controllers/invoice_controller.py`:
```python
# Flawed implementation
invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
```

#### 4. Remediation Guidance
Enforce tenancy scoping in the database query:
```python
# Remediated implementation
invoice = db.query(Invoice).filter(
    Invoice.id == invoice_id,
    Invoice.tenant_id == current_user.tenant_id
).first()

if not invoice:
    raise HTTPException(status_code=404, detail="Invoice not found")
```

#### 5. Verification Test
Add an automated regression test in `tests/security/test_invoice_authz.py` verifying that requesting another tenant's invoice returns a 404 status.
