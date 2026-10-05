# Defect evidence and observation logs

## Featured CRM cases

| Case | Finding | Evidence limit |
|---|---|---|
| [Reserved lead status](TC-API-LEAD-006_QA_Case.pdf) | Creation accepted a conversion-only status; follow-up GET confirmed persistence for one attempt | Two creations, one persistence check; no evidenced fix/retest |
| [Telegram connection](CQ-2_Telegram_QA_Case.pdf) | Connection returned HTTP 400 and remained disconnected | Token validity and root cause unconfirmed |

These are defect case studies with linked test scenarios, not standalone test-case specifications. [Lead-creation regression design](../Test_Design/Lead_Creation.md) shows how the first finding informs further coverage.

## Historical website observations

| Log | Context |
|---|---|
| [Oxford Medical](Def_001.md) | Desktop layout, localization and booking usability observations |
| [Zpolis](Def_002.md) | Mobile-browser navigation and visual observations |
| [DPCOZT](Def_003.md) | Mobile navigation, contact affordances and visual observations |

These logs preserve the originally reported observations and external evidence references. They were not rerun during this review. Missing build/browser detail, incomplete reproduction data and ambiguous dates are stated rather than reconstructed. External evidence access has not been verified; the local CRM PDFs are the primary review samples.

Severity describes user impact; priority describes urgency. Historical labels are reporter assessments, not a current product decision. Visual preferences require a design requirement or usability rationale before being treated as confirmed defects.

[Back to portfolio](../README.md)
