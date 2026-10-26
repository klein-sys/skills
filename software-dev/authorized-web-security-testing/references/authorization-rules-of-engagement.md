# Rules of Engagement & Ethical Guardrails for Security Assessments

Security testing without explicit authorization constitutes unauthorized computer access and is illegal under international computer crime statutes (e.g., CFAA, UK Computer Misuse Act).

---

## 1. Scope Boundary Rules

1. **Explicit In-Scope Targets Only**:
   - Assessments must target strictly specified hostnames, IP addresses, or local ports (e.g., `http://localhost:3000`, `http://127.0.0.1:8080`).
2. **Strictly Out-of-Scope**:
   - Third-party APIs (Stripe, Twilio, AWS, GitHub OAuth, Auth0).
   - Domain Name System (DNS) providers and CDN networks (Cloudflare, Fastly).
   - Any external domain not explicitly owned and hosted by the user for testing.

---

## 2. Safe Testing Constraints

- **No Denial of Service (DoS)**:
  - Do not send volumetric packet floods, slowloris requests, or large payload bombs that could exhaust memory or crash production environments.
- **Non-Destructive Payloads**:
  - For SQL injection verification: Use benign boolean probes (`AND 1=1`) or sleep/delay probes (`pg_sleep(1)`). Never use `DROP TABLE`, `UPDATE`, or `DELETE`.
  - For XSS verification: Use `console.log()` or DOM attribute probes rather than intrusive alert popups or cookie exfiltration scripts.
  - For file upload testing: Upload a benign text file containing an inert identifier (e.g., `echo "security-test" > probe.txt`). Never upload webshells.

---

## 3. Incident Escalation Protocol

If testing uncovers:
1. Active evidence of an existing unauthorized compromise.
2. Exposure of real production customer credentials or secrets.
3. Severe remote code execution capabilities.

**Action**: Stop testing immediately. Do not exploit further. Prepare an urgent briefing for the user detailing the exact endpoint and affected data.
