# PUT: replacement and persistence

**Status:** proposed exercise; not executed. Assume `PUT /users/{id}` replaces the writable profile and returns 200. Required, optional and server-managed fields must be defined by the contract.

```json
{"name": "Synthetic Updated User", "email": "updated@example.test"}
```

| ID | Check | Expected evidence |
|---|---|---|
| PUT-01 | Valid replacement of owned record | 200; follow-up GET matches writable values |
| PUT-02 | Identical replacement twice | Same intended business state; no duplicate business effect |
| PUT-03 | Omit required vs optional fields separately | Documented rejection, default or removal behavior |
| PUT-04 | Invalid value in one field | Error with no partial write if atomic replacement is required |
| PUT-05 | Modify immutable ID or another user's record | No unauthorized mutation |
| PUT-06 | Stale version/ETag where supported | Defined conflict/precondition response; no silent lost update |

```javascript
pm.test("Updated representation matches submitted fields", () => {
    pm.response.to.have.status(200);
    const actual = pm.response.json();
    const submitted = JSON.parse(pm.variables.replaceIn(pm.request.body.raw));
    pm.expect(actual.name).to.eql(submitted.name);
    pm.expect(actual.email).to.eql(submitted.email);
});
```

The snippet assumes raw JSON and verifies the response only. Use GET for persistence. For timestamps, check parseability, ordering and clock tolerance rather than exact equality with the tester's clock. Idempotency concerns intended resource state, not identical timestamps or response bytes.

[Back to API index](README.md)
