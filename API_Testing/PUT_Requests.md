# 🔄 API Testing: PUT Methods & Resource Updates

## 📌 Document Overview
This document covers the validation of `PUT` requests, specifically focusing on **Full Resource Updates**. Unlike `PATCH`, these requests are designed to replace the entire state of an existing entity. Key testing areas include data integrity, timestamp validation, and schema consistency.

---

## 📋 PUT Request Catalog

| Module | Scenario | Update Scope | Auth Level |
| :--- | :--- | :--- | :--- |
| **Users** | Profile Update | Full Object Replacement | User/Admin |
| **Inventory**| Product Specification | Metadata & Stock Override | Manager/Admin |

---

## 🧪 Detailed Test Scenarios

### 1. Full User Profile Update
**Endpoint:** `PUT /users/51`  
**Description:** Verifies the ability to replace all user attributes (Name, Email, Contact, Address) in a single operation.

**Request Body:**
```json
{
  "name": "Eve Cooper",
  "email": "eve.cooper@example.com",
  "phone": "+1-555-1234",
  "address": {
    "street": "456 Innovation Rd",
    "city": "Techville",
    "postal_code": "54321",
    "country": "USA"
  }
}
```
### Success Criteria:

Status Code: 200 OK.

Timestamp Validation: The updated_at field must reflect the current server time and be later than the created_at value.

Data Persistence: A follow-up GET /users/51 must return the newly updated values exactly as provided in the PUT payload.

## 2. Product Catalog Replacement
Endpoint: PUT /products/101

Testing Focus: Integrity of mandatory fields.

Body:

```json
{
  "name": "Wireless Mouse Pro",
  "description": "Ergonomic wireless mouse with customizable DPI and silent buttons.",
  "price": 49.99,
  "stock": 120,
  "category": "Accessories"
}
```
### Validation Logic (QA Insights):

Idempotency Check: I verify that sending the same PUT request multiple times results in the same state (Idempotency).
Null Field Test: I test system behavior when a mandatory field (e.g., price) is missing from the PUT body—expecting a 400 Bad Request since PUT requires the full object.

## ⚙️ Postman Automation (Validation Script)
I implement these checks to ensure the server handles updates correctly:

```Java
const response = pm.response.json();

pm.test("Update Successful - Status 200", () => {
    pm.response.to.have.status(200);
});

pm.test("Metadata: updated_at is present", () => {
    pm.expect(response).to.have.property('updated_at');
    // Verify ISO 8601 Date Format
    pm.expect(Date.parse(response.updated_at)).to.not.be.NaN;
});

pm.test("Data Consistency: Name matches request", () => {
    const requestData = JSON.parse(pm.request.body.raw);
    pm.expect(response.name).to.eql(requestData.name);
});
```
[⬅️ Back to Api Testing Index](./)