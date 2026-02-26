# ✅ Functional Testing Checklist

## 📌 Document Overview
This checklist serves as a high-level guide to ensure core functional requirements are met during the **Smoke** or **Sanity** testing phases. It covers input validation, authentication flows, error handling, and basic CRUD (Create, Read, Update, Delete) operations.

---

## 📋 Execution Summary
* **Target System:** Web Application / E-commerce (Example)
* **Environment:** Staging / QA
* **Tester:** Vadym Mazur
* **Status Legend:** 🟢 Pass | 🔴 Fail | ⚪ Blocked / N/A

---

### 1. Navigation & UI Elements
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **NAV-01** | Verify all header and footer links. | Links redirect to correct pages without `404 Not Found` errors. | 🟢 Pass |
| **NAV-02** | Test breadcrumb navigation. | Breadcrumbs accurately reflect the user's location in the site hierarchy. | 🟢 Pass |
| **NAV-03** | Verify logo click behavior. | Clicking the site logo consistently redirects to the Homepage. | 🟢 Pass |
| **NAV-04** | Check buttons state. | "Submit" buttons are disabled until mandatory fields are filled out. | 🟢 Pass |

### 2. Forms & Input Validation
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **INP-01** | Validate mandatory fields. | Submitting empty mandatory fields triggers appropriate, highlighted error messages. | 🟢 Pass |
| **INP-02** | Test boundary values on inputs. | Numeric inputs outside the min/max allowed range are cleanly rejected. | 🔴 Fail |
| **INP-03** | Verify special characters handling. | Forms safely reject special chars or sanitize them (preventing XSS/SQLi). | 🟢 Pass |
| **INP-04** | Check dropdown menus. | Dropdowns display correct options, default values, and are fully selectable. | 🟢 Pass |

### 3. User Authentication & Security
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **AUTH-01** | Verify valid login credentials. | User is redirected to the dashboard after entering correct email and password. | 🟢 Pass |
| **AUTH-02** | Verify invalid login attempts. | A clear, non-specific error message is shown (e.g., "Invalid credentials"). | 🟢 Pass |
| **AUTH-03** | Test password field masking. | Password characters are masked (shown as asterisks/dots) during input. | 🟢 Pass |
| **AUTH-04** | Verify session timeout. | User is logged out automatically after 30 minutes of inactivity. | ⚪ N/A |

### 4. Business Logic (CRUD Operations)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **CRUD-01** | **Create:** Add new record. | Item is successfully created and instantly appears in the UI and database. | 🟢 Pass |
| **CRUD-02** | **Read:** Verify displayed data. | Data displayed in the UI matches the database exactly (no truncation). | 🟢 Pass |
| **CRUD-03** | **Update:** Edit existing record. | Changes are saved correctly and reflected without needing a page refresh. | 🟢 Pass |
| **CRUD-04** | **Delete:** Remove existing record. | System asks for confirmation, then deletes the item. Item disappears from UI. | 🟢 Pass |

---

## 🛠 QA Notes & Observations
> **Insight:** Functional checklists are utilized for rapid verification. For failed steps (such as `INP-02` above), detailed bug reports are generated in Jira with corresponding logs and screenshots.

---
[⬅️ Back to Checklists Index](./)