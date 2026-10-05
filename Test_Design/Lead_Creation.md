# Lead creation: risk and regression design

**Basis:** [TC-API-LEAD-006 evidence](../Bug_Reports/TC-API-LEAD-006_QA_Case.pdf). The reported rule reserves `converted` for the conversion workflow. Two invalid creations and one persistence check are documented. This design adds proposed coverage; it does not claim additional executions.

## Risk and oracle

Direct creation with a conversion-only status can produce conflicting lifecycle fields. Potential downstream effects include incorrect filtering, reporting or workflow decisions; these effects have not been demonstrated by the supplied evidence.

The rejection oracle has two parts: **HTTP 400 with validation information**, and **no lead persisted for the unique test marker**. Checking only the response misses partial-write defects; checking only a generic list count can confuse another test's data with this attempt.

## Coverage matrix

| ID | Technique / input | Expected result | Evidence status |
|---|---|---|---|
| LC-01 | Valid partition: fresh contact and permitted initial status | 201; detail/list reads match submitted data | Proposed; listed as collection coverage, no assessed result |
| LC-02 | Required-field partition: omit `first_name` | 400; no saved lead | Proposed; listed in supplied collection |
| LC-03 | Decision combination: neither phone nor email | 400; no saved lead | Proposed; listed in supplied collection |
| LC-04 | Invalid partition: malformed email | 400; no saved lead | Proposed; listed in supplied collection |
| LC-05 | Normalization: same email with different letter case | 400; no additional lead under reported contract | Proposed; listed in supplied collection |
| LC-06 | Forbidden state: `status: converted` at creation | 400; no saved lead | Documented failure: 201 twice; one GET confirms persistence |
| LC-07 | Valid state transition through approved conversion workflow | Consistent conversion fields and associated records, atomically | Proposed regression; exact workflow contract needed |
| LC-08 | Unknown, null, omitted and empty status separately | Contract-defined validation/default; no forbidden state | Proposed; clarify defaults before execution |
| LC-09 | Valid data under role without create permission / wrong workspace | Denied according to access contract; no cross-scope write | Proposed; role matrix and fixture needed |
| LC-10 | Allowed text-length boundary N-1, N, N+1 | Accept through N; reject N+1 without partial write | Proposed; obtain field limit N first |

## Contact decision table

This is a proposed design based on the reported requirement for at least one contact channel. Confirm that each channel is sufficient independently before execution.

| Valid email | Valid phone | Proposed expectation |
|---|---|---|
| Yes | No | Accept, subject to other required fields |
| No | Yes | Accept, subject to other required fields |
| Yes | Yes | Accept and preserve both |
| No | No | Reject; missing channels and invalid channel formats are separate partitions |

## Execution and data control

Use a disposable environment, record build/role/workspace, and verify session/CSRF setup. Generate unique title/email per attempt. Capture the outgoing fields, status, validation body and follow-up read with the same marker. Verify identifiers before cleanup. If an invalid creation succeeds, record the defect before removing only its synthetic records.

Record each case as Passed, Failed, Blocked or Not run with an evidence link. Never infer outcomes for the rest of a collection from a single screenshot.

## Triage and release recommendation

Reproduce LC-06 on the candidate build, then retest it after a fix and execute LC-01/LC-05/LC-07 for adjacent regressions. If the lifecycle invariant still fails, recommend blocking the affected change pending correction or explicit product risk acceptance. A proposed release decision is not a claim of an actual release gate or approval.

[Back to portfolio](../README.md)
