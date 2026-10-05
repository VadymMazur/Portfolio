# POST: creation and validation

**Status:** proposed exercise; not executed. Assume authorized `POST /users` returns 201 and a unique ID; invalid input returns 400; duplicate normalized email returns 409. These are exercise assumptions, not universal rules.

```json
{"name": "Synthetic User", "email": "qa.unique-run@example.test", "password": "Example-only-not-a-real-password-42!"}
```

| Partition | Check | Expected result |
|---|---|---|
| Valid | Unique email and required fields | 201; follow-up GET matches; password absent |
| Required name | Missing, null, empty, whitespace-only separately | 400; no created record |
| Email | Valid, malformed, missing, duplicate, case-variant duplicate | Contract-consistent validation and normalization |
| Length | Documented maximum N: N-1, N, N+1 | Accept through N; reject N+1 without truncation |
| Privileged fields | Unauthorized role/owner value | No privilege escalation or reassignment |
| Retry | Repeat after simulated timeout | Defined duplicate/idempotency-key behavior; POST is not inherently idempotent |

For rejected creation, search by the unique marker to check that nothing was saved. For success, save the returned ID for narrowly scoped cleanup. Record response and persistence checks separately.

## Authentication and other design examples

- Token contract: check token location, lifetime and expiry/revocation. Cookie session: check invalidation, cookie attributes and CSRF. Do not assume every login uses JWT or an Authorization response header.
- Upload: use a multipart file part and let Postman generate the boundary. Check extension/content mismatch and size at limit-1/limit/limit+1, including server-side rejection and storage effects.
- Order: check quantities and totals against authoritative server prices, including rounding. Client-supplied totals must not override pricing rules.

[Back to API index](README.md)
