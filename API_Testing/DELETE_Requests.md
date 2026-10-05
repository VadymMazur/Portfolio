# DELETE: access scope and lifecycle

**Status:** proposed exercise; not executed. Assume `DELETE /users/{{temp_user_id}}` returns 204 without a body and hides the deleted user from normal reads. Physical vs soft deletion is a separate requirement.

## Setup

Create a disposable user in a separate setup request with a unique `example.test` email. Configure authentication for both setup and deletion. Never use shared or arbitrary records.

```javascript
// Tests on setup POST /users.
pm.environment.unset("temp_user_id");
pm.test("Setup created a disposable user", () => {
    pm.response.to.have.status(201);
    const body = pm.response.json();
    pm.expect(body.id).to.be.a("number");
    pm.environment.set("temp_user_id", body.id);
});
```

Stop if setup fails. Separate setup makes failures easier to inspect than an unchecked asynchronous pre-request call.

| ID | Condition | Expected result under this exercise contract |
|---|---|---|
| DEL-01 | Owned disposable user | 204; empty body; GET 404; list excludes ID |
| DEL-02 | Repeat DELETE | 404 here; remains deleted. Different codes do not alone violate idempotency |
| DEL-03 | Malformed ID | 400; distinguish invalid syntax from a well-formed missing ID |
| DEL-04 | Missing/invalid credentials | 401; record unchanged |
| DEL-05 | No permission or outside scope | 403 or concealed 404 per contract; no deletion |
| DEL-06 | Dependent objects exist | Defined restrict/cascade/soft-delete behavior; no orphaning |

```javascript
// Tests on DEL-01 only.
pm.test("Delete returns no content", () => {
    pm.response.to.have.status(204);
    pm.expect(pm.response.text()).to.eql("");
});
```

Run GET verification separately. A 204 alone does not prove physical deletion or correct treatment of related data.

[Back to API index](README.md)
