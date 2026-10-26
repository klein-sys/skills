---
name: authorized-web-security-testing
description: >-
  Use this skill when conducting authorized security assessments, penetration testing simulations, or
  vulnerability verification against local test environments or explicitly authorized web applications.
  Enforces strict authorization checks, rules of engagement, and OWASP Web Security Testing Guide (WSTG v4.2)
  methodology.
---

# Authorized Web Application Security Testing

This skill provides a structured, ethical, and defensive methodology for assessing web application security. Modeled on the industry-standard **OWASP Web Security Testing Guide (WSTG v4.2)**, it strictly mandates verifiable authorization, rules of engagement, and non-destructive testing procedures.

---

## CRITICAL SAFETY & ETHICAL DIRECTIVE

> [!CAUTION]
> **UNAUTHORIZED SECURITY TESTING IS STRICTLY PROHIBITED.**
> 1. Never test any external host, URL, domain, or IP without explicit written authorization and verified scope.
> 2. By default, testing must only be performed on `localhost`, local Docker containers, ephemeral CI environments, or designated staging instances owned by the user.
> 3. Never execute destructive payloads (e.g., dropping database tables, flooding network interfaces, denial of service).
> 4. Immediately halt testing and notify the user if sensitive data (e.g., third-party PII, unexpected production databases) is encountered.

---

## When to Activate This Skill

- When validating security defenses of a newly built web app running on localhost or staging.
- When performing pre-deployment vulnerability verification for an authorized project.
- When drafting a security test plan based on OWASP WSTG v4.2 standards.
- When writing automated security regression tests (e.g., verifying that XSS or SQLi payloads are safely rejected).

---

## Testing Workflow & Methodology

```
[Verify Authorization & Scope]
               │
               ▼
[Target Reconnaissance & Surface Mapping]
               │
               ▼
  [Execute WSTG Inspection Modules]
   - Authentication & Sessions
   - Authorization & Access Control (IDOR)
   - Input Validation & Injection Defenses
   - Business Logic & State Transitions
               │
               ▼
 [Risk Scoring & Verification of Fixes]
               │
               ▼
  [Structured Remediation Report]
```

### 1. Verification of Scope & Authorization
Before invoking any testing tools or requests, confirm:
1. Target URL/Host (e.g., `http://localhost:8000`).
2. Scope boundaries (allowed routes vs forbidden third-party payment gateways/OAuth providers).
3. Test account credentials provided by the user for authenticated testing.
See [Authorization & Rules of Engagement](./references/authorization-rules-of-engagement.md).

### 2. Surface & Architecture Mapping (WSTG-INFO & WSTG-CONF)
- Catalog all endpoints, query parameters, headers, and HTTP methods.
- Check security response headers (`Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`).
- Inspect CORS configuration (`Access-Control-Allow-Origin: *` with credentials).

### 3. Core WSTG Assessment Categories
Execute non-destructive inspection across key areas:
- **Authentication & Password Management (WSTG-ATHN)**:
  - Test for rate limiting on login/reset routes to prevent brute-force attacks.
  - Verify session invalidation upon logout.
- **Authorization & Multi-Tenancy (WSTG-ATHZ)**:
  - Test Horizontal Privilege Escalation (IDOR): Access User B's resources using User A's session.
  - Test Vertical Privilege Escalation: Access administrative endpoints (`/admin`) using a non-privileged token.
- **Input Validation & Injection (WSTG-INPV)**:
  - Test parameter handling with benign boundary payloads (e.g., `' OR '1'='1`, `<script>alert(1)</script>`, `../../etc/passwd`).
  - Observe application behavior: proper 400 Bad Request vs unhandled 500 error leaking SQL syntax.
- **Session Management (WSTG-SESS)**:
  - Verify cookie flags: `HttpOnly`, `Secure`, `SameSite=Lax` or `Strict`.
- **Business Logic Testing (WSTG-BUSL)**:
  - Test workflow bypasses (e.g., skipping payment step in checkout, negative item quantities).
See [OWASP WSTG v4.2 Test Matrix](./references/wstg-v42-test-matrix.md).

### 4. Findings & Remediation Reporting
Document all validated vulnerabilities in a structured report format:
- Finding Title & WSTG Test ID
- Severity (Critical, High, Medium, Low, Informational)
- CVSS v3.1 Score
- Steps to Reproduce (non-destructive)
- Root Cause Analysis
- Concrete Remediation Snippet
See [Security Assessment Report Template](./examples/security-assessment-report-template.md).

---

## References & Guides

- [OWASP WSTG v4.2 Comprehensive Test Matrix](./references/wstg-v42-test-matrix.md)
- [Rules of Engagement & Ethical Guardrails](./references/authorization-rules-of-engagement.md)
- [Security Assessment Report Template](./examples/security-assessment-report-template.md)

---

## Verification Checklist

Before completing an authorized security assessment:

- [ ] Written authorization and defined test boundaries were verified prior to testing.
- [ ] No destructive, data-wiping, or DoS payloads were transmitted.
- [ ] Every finding has an isolated, reproducible proof-of-concept.
- [ ] Remediation recommendations include both defensive code examples and preventative tests.
- [ ] All test data, test user accounts, and temporary logs are properly cleaned up.
