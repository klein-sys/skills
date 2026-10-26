# STRIDE Threat Modeling Reference

STRIDE is a mnemonic threat modeling framework created to discover vulnerabilities systematically across system boundaries.

| Threat Category | Property Violated | Question to Ask | Defensive Pattern / Countermeasure |
| :--- | :--- | :--- | :--- |
| **S**poofing | Authenticity | Can an attacker pretend to be another entity (user, service, hardware)? | Strong multi-factor authentication, cryptographic signatures (HMAC, JWT with asymmetric keys), mTLS for internal microservices. |
| **T**ampering | Integrity | Can data in transit or storage be modified without detection? | Cryptographic hashes, digital signatures, TLS 1.3 encryption, database write-ahead log integrity checks. |
| **R**epudiation | Non-repudiation | Can a user deny having performed a critical action? | Append-only audit logs, secure timestamping, recording principal ID and transaction hashes. |
| **I**nformation Disclosure | Confidentiality | Can unauthorized parties read private data, tokens, or system internals? | Encryption at rest and in transit, strict object-level authorization, masking secrets in logs, generic error messages. |
| **D**enial of Service | Availability | Can an adversary exhaust resources (CPU, RAM, DB connections, disk)? | Rate limiting, token buckets, payload size limits, request timeouts, caching, async worker queues. |
| **E**levation of Privilege | Authorization | Can a normal user execute admin operations or access another tenant's data? | Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), strict tenant isolation filters in all queries. |
