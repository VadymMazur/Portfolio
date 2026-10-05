# API test design

Learning exercises for a fictional user/product API: proposed checks and Postman JavaScript snippets, not a deployed service or recorded results. `{{base_url}}` and `{{access_token}}` are local variables; no credentials are supplied.

| Method | Design focus |
|---|---|
| [GET](GET_Requests.md) | Identity, filtering, pagination and access scope |
| [POST](POST_Requests.md) | Input partitions, side effects and duplicates |
| [PUT](PUT_Requests.md) | Replacement, persistence and idempotent business state |
| [DELETE](DELETE_Requests.md) | Owned test data, authorization and post-deletion checks |

Examples consistently use `/users` and `/products`. Response codes and schemas are exercise assumptions to reconcile with an application's contract before execution. No Postman collection, environment export, Newman run or SoapUI project is included.

For application-specific evidence, see the [reserved lead-status case](../Bug_Reports/TC-API-LEAD-006_QA_Case.pdf) and [proposed regression coverage](../Test_Design/Lead_Creation.md).

[HTTP method semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-9) · [Back to portfolio](../README.md)
