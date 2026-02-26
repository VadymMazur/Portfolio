# 🗑️ API Testing: DELETE Request Validation

### 📝 Project Overview
This module demonstrates the verification of data removal via REST API. The focus is on ensuring that the resource is correctly deleted from the database and subsequent requests return appropriate error codes.

---

### 🚀 Endpoint Details
* **Method:** `DELETE`
* **URL:** `{{base_url}}/api/v1/users/{{user_id}}`
* **Auth:** Bearer Token (Admin Access Required)

---

### 🔍 Test Scenarios & Verification

#### ✅ 1. Successful Resource Deletion (Positive)
* **Description:** Delete an existing user by a valid ID.
* **Expected Status Code:** `204 No Content` or `200 OK`.
* **Post-condition:** A `GET` request to the same ID must return `404 Not Found`.

#### ❌ 2. Deletion with Invalid ID (Negative)
* **Description:** Attempt to delete a user using a non-existent or malformed ID.
* **Expected Status Code:** `404 Not Found`.
* **Response Body:** ```json
    {
      "error": "User not found",
      "code": "USER_001"
    }
    ```

#### ❌ 3. Unauthorized Access (Security)
* **Description:** Attempt to delete a resource without a valid Authorization header.
* **Expected Status Code:** `401 Unauthorized`.

---

### 🛠️ Implementation in Postman

To automate this test, I used the following **Pre-request Script** to ensure a resource exists before deletion:

```javascript
// Postman Pre-request Script
pm.sendRequest({
    url: pm.environment.get("base_url") + "/api/v1/users",
    method: 'POST',
    body: { mode: 'raw', raw: JSON.stringify({ name: "Temp User" }) }
}, function (err, res) {
    pm.environment.set("temp_user_id", res.json().id);
});
## Tests tab for validation:

pm.test("Status code is 204", function () {
    pm.response.to.have.status(204);
});

pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});