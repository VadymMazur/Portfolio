# 📤 API Testing: POST Methods & Resource Creation

## 📌 Document Overview
This section demonstrates the validation of data submission and resource creation. Key focus areas include payload structure, data types, authentication flows, and multi-part data handling.

---

## 📋 POST Request Catalog

| Module | Scenario | Request Type | Auth Required |
| :--- | :--- | :--- | :--- |
| **Auth** | User Login | `application/json` | No |
| **Users** | Account Creation | `application/json` | Yes (Admin) |
| **Inventory**| Product Review | `application/json` | Yes (User) |
| **Media** | Image Upload | `multipart/form-data` | Yes (User) |
| **Sales** | Order Placement | `application/json` | Yes (User) |

---

## 🧪 Detailed Test Scenarios

### 1. Account Creation (User Management)
**Endpoint:** `POST /users`  
**Description:** Validates the system's ability to create a new user entity while enforcing password security.

**Request Body:**
```json
{
  "name": "Eve",
  "email": "eve@example.com",
  "password": "securePassword123"
}
## Expected Results:

Status Code: 201 Created

Data Masking: Verified that the password field is not returned in the response body.

Database Integrity: Response id is generated as a unique integer.

## 2. Authentication & JWT Generation
Endpoint: POST /auth/login

Logic: Verifies credential validation and token issuance.

Success Criteria:

Status: 200 OK (Standard for login)

Header: Set-Cookie or Authorization header contains a valid JWT.

Payload:
{
  "token": "eyJhbGciOiJIUzI1Ni...",
  "expires_in": 3600,
  "user_id": 51
}

Gemini said
To make your POST Requests documentation even more professional, we will focus on Input Validation and Data Integrity.

For a recruiter, the most important part of a POST request is how you test the Request Body. This version introduces a "Validation Logic" section, which proves you consider boundary values and field constraints.

Markdown
# 📤 API Testing: POST Methods & Resource Creation

## 📌 Document Overview
This section demonstrates the validation of data submission and resource creation. Key focus areas include payload structure, data types, authentication flows, and multi-part data handling.

---

## 📋 POST Request Catalog

| Module | Scenario | Request Type | Auth Required |
| :--- | :--- | :--- | :--- |
| **Auth** | User Login | `application/json` | No |
| **Users** | Account Creation | `application/json` | Yes (Admin) |
| **Inventory**| Product Review | `application/json` | Yes (User) |
| **Media** | Image Upload | `multipart/form-data` | Yes (User) |
| **Sales** | Order Placement | `application/json` | Yes (User) |

---

## 🧪 Detailed Test Scenarios

### 1. Account Creation (User Management)
**Endpoint:** `POST /users`  
**Description:** Validates the system's ability to create a new user entity while enforcing password security.

**Request Body:**
```json
{
  "name": "Eve",
  "email": "eve@example.com",
  "password": "securePassword123"
}
Expected Results:

Status Code: 201 Created

Data Masking: Verified that the password field is not returned in the response body.

Database Integrity: Response id is generated as a unique integer.

2. Authentication & JWT Generation
Endpoint: POST /auth/login

Logic: Verifies credential validation and token issuance.

Success Criteria:

Status: 200 OK (Standard for login)

Header: Set-Cookie or Authorization header contains a valid JWT.

Payload:

JSON
{
  "token": "eyJhbGciOiJIUzI1Ni...",
  "expires_in": 3600,
  "user_id": 51
}
## 3. File Upload (Multipart Handling)
Endpoint: POST /uploads/images

Testing Focus: Binary data handling and file constraints.

Headers: Content-Type: multipart/form-data

Form-Data Fields:

file: mouse.jpg (Binary)

description: "Product Image"

Validation Points: * Verify support for .jpg, .png formats.

Check system behavior when file exceeds size limit (e.g., > 5MB).

## 4. Complex Data Structures (Order Placement)
Endpoint: POST /orders

Complexity: Validates nested objects and arrays.

Validation Logic (QA Insights):

I perform Boundary Value Analysis on the quantity field (testing values: 0, 1, and max allowed). I also verify that total is correctly calculated based on the sum of product_id prices.

Sample Request:
{
  "products": [
    { "product_id": 101, "quantity": 2 },
    { "product_id": 106, "quantity": 1 }
  ],
  "shipping_address": {
    "street": "123 Market St",
    "postal_code": "12345"
  },
  "payment_method": "credit_card"
}