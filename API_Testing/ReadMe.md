# 🔌 API Testing Framework & Documentation

## 📌 Overview
This directory serves as a comprehensive guide to the API testing methodologies applied in this portfolio. It covers the validation of RESTful services, focusing on data integrity, security, and performance. The goal is to ensure that the backend architecture meets both functional requirements and industry-standard security protocols.



---

## 📂 Documentation Index
Detailed test scenarios and request specifications are organized by HTTP method:

* [**GET Requests**](GET_Requests.md) – Validation of data retrieval, query parameters, and pagination logic.
* [**POST Requests**](POST_Requests.md) – Testing resource creation, authentication flows, and payload validation.
* [**PUT Requests**](PUT_Requests.md) – Verification of full resource updates and data consistency.
* [**DELETE Requests**](DELETE_Requests.md) – Testing resource removal, state changes, and error handling.

---

## 🎯 Testing Strategy & Validation Layers
When testing these endpoints, I apply a three-layer validation approach:

1.  **Transport Layer:** Verifying HTTP status codes, headers (Content-Type, Cache-Control), and response times.
2.  **Data Layer:** Validating JSON schema, data types (string vs integer), and mandatory vs optional fields.
3.  **Business Logic Layer:** Testing boundary values, negative scenarios, and state transitions (e.g., verifying a deleted user cannot login).

---

## 🛠 Toolset
* **Primary Tool:** [Postman](https://www.postman.com/) (Collections, Environment Variables, Automated Tests).
* **Debugging:** [Chrome DevTools](https://developer.chrome.com/docs/devtools/network/) (Network Tab) & [Fiddler](https://www.telerik.com/fiddler).
* **Documentation:** [Swagger/OpenAPI](https://swagger.io/) for contract testing.
* **CLI:** `cURL` for quick endpoint verification.

---

## 🚦 HTTP Reference Guides

### Core Methods
| Method | Purpose | Testing Focus |
| :--- | :--- | :--- |
| **GET** | Retrieve data | Filters, Sorting, Pagination |
| **POST** | Create resource | Payload validation, Security |
| **PUT** | Replace resource | Full object integrity, Idempotency |
| **PATCH** | Partial update | Field-specific changes |
| **DELETE** | Remove resource | Cleanup, Dependencies |

### Key Response Codes
| Class | Category | Common Examples |
| :--- | :--- | :--- |
| **2xx** | Success | `200 OK`, `201 Created`, `204 No Content` |
| **3xx** | Redirection | `301 Moved`, `304 Not Modified` |
| **4xx** | Client Error | `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `429 Rate Limit` |
| **5xx** | Server Error | `500 Internal Error`, `503 Service Unavailable`, `504 Gateway Timeout` |



---
[⬅️ Back to Main Portfolio](../README.md)