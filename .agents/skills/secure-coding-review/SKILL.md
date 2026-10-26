---
name: secure-coding-review
description: >-
  Use this skill when auditing source code for security vulnerabilities, performing threat modeling,
  implementing cryptographic or authentication features, or conducting an application security code review.
  Applies STRIDE threat modeling, OWASP Top 10 mitigation patterns, and strict secret hygiene.
---

# Secure Coding & Application Security Reviews

This skill acts as a senior application security engineer embedded in the software development lifecycle. It guides you through rigorous source code security audits, component boundary threat modeling, and defensive implementation patterns.

---

## When to Activate This Skill

- When writing or reviewing authentication, authorization, session management, or access-control logic.
- When handling sensitive data (passwords, tokens, PII, financial data, health records).
- When integrating database queries, external system commands, file uploads, or third-party APIs.
- When performing pre-release security code reviews or dependency vulnerability audits.
- When designing APIs to prevent SSRF, IDOR, and broken object-level authorization (BOLA).

---

## Application Security Audit Workflow

```
[Define Trust Boundaries & Assets]
               │
               ▼
   [Execute STRIDE Threat Model]
               │
               ▼
[Scan for OWASP Top 10 Code Patterns]
               │
               ▼
[Verify Secrets, Auth & Cryptography]
               │
               ▼
[Validate Dependencies & Dependencies Audit]
               │
               ▼
 [Produce Remediations with Regression Tests]
```

### 1. Identify Trust Boundaries & Assets
- **Map Boundaries**: Trace where data crosses from untrusted origins (HTTP requests, URL params, webhooks, file uploads) into trusted internal execution contexts.
- **Name Sensitive Assets**: Identify what an adversary would target: API keys, database credentials, user sessions, PII, financial transactions, internal network endpoints.

### 2. STRIDE Threat Modeling
Evaluate each boundary against the STRIDE threat model:
- **S**poofing: Can an attacker impersonate another user or service?
- **T**ampering: Can payloads or parameters be modified in transit or in local state?
- **R**epudiation: Are critical actions logged with immutable audit trails?
- **I**nformation Disclosure: Does error handling, debug output, or response leak sensitive info?
- **D**enial of Service: Can unbounded inputs or algorithmic complexity crash the service?
- **E**levation of Privilege: Can standard users access administrative functions or horizontal tenant resources (IDOR)?
See [STRIDE Threat Modeling Reference](./references/stride-threat-model.md).

### 3. OWASP Top 10 Vulnerability Defenses
Audit code against recurring vulnerability patterns:
1. **Injection (SQL, Command, LDAP, Template)**:
   - Always use parameterized queries / prepared statements. Never concatenate user input into SQL or shell commands.
2. **Broken Access Control & IDOR**:
   - Never trust client-supplied IDs (e.g., `/api/documents/42`) without checking if the current authenticated user owns that resource.
3. **Cryptographic Failures**:
   - Use industry-standard algorithms: AES-256-GCM for symmetric encryption, Argon2id or bcrypt with high work factor for password hashing. Never use MD5, SHA-1, or homebrewed cryptography.
4. **Server-Side Request Forgery (SSRF)**:
   - Never allow user-controlled URLs to make direct server-side HTTP requests to internal IP ranges (`127.0.0.1`, `10.0.0.0/8`, `169.254.169.254`).
5. **Cross-Site Scripting (XSS)**:
   - Ensure context-aware output encoding. Utilize Content Security Policy (CSP) headers.
See [OWASP Top 10 Defenses](./references/owasp-top10-defenses.md).

### 4. Secrets & Credentials Hygiene
- **Never Hardcode Secrets**: No API keys, database passwords, or JWT signing keys in source code or git history.
- **Environment Ingestion**: Load secrets via environment variables or secret vaults.
- **Masking**: Mask credentials and sensitive tokens in all application logs.

---

## References & Guides

- [STRIDE Threat Model Reference Matrix](./references/stride-threat-model.md)
- [OWASP Top 10 Vulnerabilities & Code Defenses](./references/owasp-top10-defenses.md)
- [Secure Code Audit Real-World Sample](./examples/secure-code-audit-sample.md)

---

## Verification Checklist

Before approving any security-sensitive code change:

- [ ] All database queries use parameterized interfaces; no raw string interpolation exists.
- [ ] Every API endpoint enforces explicit authentication and object-level ownership checks (IDOR check).
- [ ] No secrets, passwords, or keys are hardcoded in test fixtures or code files.
- [ ] Error messages return sanitized responses to clients without exposing internal stack traces or database schemas.
- [ ] Sensitive operations are protected by rate limits and recorded in tamper-resistant audit logs.
