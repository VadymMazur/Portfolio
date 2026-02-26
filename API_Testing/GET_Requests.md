# 🔍 API Testing: GET Methods & Data Retrieval

## 📌 Document Scope
This technical guide documents the validation of data retrieval via RESTful GET requests. It focuses on functional correctness, query parameter logic, and response integrity for the Users and Products modules.

---

## 🛠 Testing Framework & Tools
* **Protocol:** HTTPS / REST
* **Auth:** Bearer Token-based Authorization
* **Validation Tool:** Postman / Newman
* **Data Format:** JSON (UTF-8)

---

## 📋 API Catalog & Test Scenarios

### 1. User Directory Access
| Scenario | Endpoint | Expected Behavior |
| :--- | :--- | :--- |
| **Fetch All Users** | `GET /users` | Returns a full array of user objects with `id`, `name`, and `email`. |
| **Direct Search (ID)** | `GET /users/:id` | Returns a specific object. Validates `200 OK` vs `404 Not Found`. |
| **Role-Based Filter** | `GET /users?role={val}` | Verifies server-side filtering logic for specific user groups. |

---

### 2. Product Management & Search
| Scenario | Endpoint | Expected Behavior |
| :--- | :--- | :--- |
| **Pagination Logic** | `GET /products?page=2&limit=3` | Validates offset/limit calculations and metadata consistency. |
| **Keyword Search** | `GET /products?search={kw}` | Verifies string pattern matching within the product database. |

---

## 🧪 Detailed Request Specifications

### 🔹 Retrieve User by Identity
**Endpoint:** `{{base_url}}/users/42`  
**Purpose:** Validates individual record integrity.



**Positive Case (ID: 42):**
* **Status Code:** `200 OK`
* **Response Body Structure:**
    ```json
    {
      "id": 42,
      "name": "Charlie",
      "email": "charlie@example.com",
      "status": "active"
    }
    ```

**Negative Case (Non-existent ID):**
* **Status Code:** `404 Not Found`
* **Error Object:**
    ```json
    {
      "error_code": "RESOURCE_NOT_FOUND",
      "message": "User with ID 42 was not found"
    }
    ```

---

### 🔹 Advanced Pagination Testing
**Endpoint:** `{{base_url}}/products?page=2&limit=3`  
**Focus:** Metadata Validation.

**Response Body Analysis:**
```json
{
  "data": [
    { "id": 101, "name": "Wireless Mouse" },
    { "id": 102, "name": "USB Keyboard" },
    { "id": 103, "name": "HD Monitor" }
  ],
  "meta": {
    "current_page": 2,
    "limit": 3,
    "total_records": 9,
    "total_pages": 3
  }
}

## I use the following script to ensure data types are correct for every GET request:

// Validating JSON Schema and Data Types
const jsonData = pm.response.json();

pm.test("Status code is 200", () => {
    pm.response.to.have.status(200);
});

pm.test("Data Integrity Check", () => {
    pm.expect(jsonData.id).to.be.a('number');
    pm.expect(jsonData.email).to.match(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/);
});