# OWASP Web Security Testing Guide (WSTG v4.2) Test Matrix

*Derived from OWASP Web Security Testing Guide v4.2 under CC-BY-SA-4.0 License. © OWASP Foundation.*

This matrix provides a standardized reference of assessment checkpoints for authorized web application security reviews:

| WSTG ID | Assessment Area | Core Objective | Key Test Procedure |
| :--- | :--- | :--- | :--- |
| **WSTG-INFO-02** | Fingerprinting | Identify web server / framework versions | Inspect `Server`, `X-Powered-By` headers and default error pages. |
| **WSTG-CONF-07** | Transport Security | Verify TLS and HSTS compliance | Check `Strict-Transport-Security: max-age=31536000; includeSubDomains`. |
| **WSTG-ATHN-02** | Default Credentials | Ensure no default passwords remain | Test known vendor defaults on administrative entrypoints. |
| **WSTG-ATHN-03** | Lockout & Rate Limit | Mitigate credential brute-forcing | Send 10 consecutive invalid logins; verify 429 status or exponential backoff. |
| **WSTG-ATHZ-02** | BOLA / IDOR | Prevent horizontal privilege escalation | Request resource `/api/v1/invoices/102` using user account 101 credentials. |
| **WSTG-ATHZ-03** | Privilege Escalation | Prevent vertical access to admin APIs | Invoke `/api/admin/users` with standard `role: user` token. |
| **WSTG-SESS-02** | Cookie Attributes | Prevent session hijacking via script/network | Verify cookies have `HttpOnly`, `Secure`, and `SameSite=Lax/Strict`. |
| **WSTG-INPV-01** | Reflected XSS | Ensure script tags cannot execute in browser | Inject benign string `<b id=test>probe</b>`; inspect raw DOM reflection. |
| **WSTG-INPV-02** | Stored XSS | Prevent persistent payload storage | Store profile name with encoded characters; verify proper context escaping. |
| **WSTG-INPV-05** | SQL Injection | Prevent database query manipulation | Test single quotes and boolean probes (`' OR 1=1 --`) via parameterized APIs. |
| **WSTG-INPV-12** | SSRF | Prevent internal network scanning | Supply internal URLs (`http://169.254.169.254`, `http://localhost:22`) to webhooks. |
| **WSTG-BUSL-01** | Business Logic | Prevent workflow circumvention | Skip mandatory intermediate checkout or verification steps. |
| **WSTG-CLNT-07** | Clickjacking | Prevent malicious iframe framing | Verify `X-Frame-Options: DENY` or CSP `frame-ancestors 'none'`. |
