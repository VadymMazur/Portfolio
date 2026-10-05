# GET: retrieval, scope and pagination

**Status:** proposed exercise; not executed. Assume `/users/{id}` returns an object and `/products` returns `{data, meta}` with one-based pagination and a stable sort.

| ID | Input / condition | Expected result | Risk |
|---|---|---|---|
| GET-01 | Existing user visible to this actor | 200; ID and fields match fixture | Wrong-record response |
| GET-02 | Well-formed nonexistent ID | 404 under this contract | Absence confused with validation failure |
| GET-03 | Existing user outside actor scope | Denied per contract; no private fields | Data disclosure |
| GET-04 | Filter with matches, then no matches | Every item satisfies filter; empty collection for no matches | Incorrect filtering |
| GET-05 | Pages 1, 2 and 3; limit 3; fixed set of 9 | No gaps/duplicates; consistent totals and deterministic order | Off-by-one and unstable pagination |
| GET-06 | Page 0, negative/non-integer page, excessive limit | Defined validation response | Invalid input and uncontrolled result size |

Postman assertion for GET-01 only; do not apply this object-level check to array responses:

```javascript
pm.test("Visible user matches the requested fixture", () => {
    pm.response.to.have.status(200);
    const body = pm.response.json();
    pm.expect(body.id).to.eql(Number(pm.variables.get("user_id")));
    pm.expect(body.email).to.eql(pm.variables.get("expected_email"));
    pm.expect(body).not.to.have.property("password");
});
```

Prepare variables from an owned synthetic fixture. Record actor, dataset version and sort order before pagination checks. A loose email regex does not validate identity or the full schema.

[Back to API index](README.md)
