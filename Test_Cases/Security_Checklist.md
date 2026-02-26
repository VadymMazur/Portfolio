# 🛡️ Security Testing Checklist (Basic OWASP)

## 📌 Document Overview
This checklist focuses on essential security validations that can be performed during functional testing. It is designed to identify common vulnerabilities (inspired by the OWASP Top 10) such as Broken Access Control, Sensitive Data Exposure, and basic Injection flaws before they reach production.

---

## 📋 Execution Summary
* **Target System:** Web Application / Admin Portal
* **Environment:** QA / Staging
* **Tester:** Vadym Mazur
* **Status Legend:** 🟢 Pass | 🔴 Fail | ⚪ Blocked / N/A

---

### 🔑 1. Authentication & Session Management
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SEC-01** | Verify password transmission. | Passwords are never sent in plain text or via `GET` parameters (visible in the URL). | 🟢 Pass |
| **SEC-02** | Check session expiration (Timeout). | The session automatically terminates after a period of inactivity (e.g., 15-30 minutes). | 🟢 Pass |
| **SEC-03** | Verify concurrent logins. | A user cannot be logged in simultaneously from multiple devices/browsers (if restricted by business logic). | ⚪ N/A |
| **SEC-04** | "Back" button after Logout. | Clicking the browser's "Back" button after logging out does not restore the authenticated session. | 🟢 Pass |

### 🛑 2. Authorization & Access Control (Broken Access Control)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SEC-05** | Role-Based Access Control (RBAC). | A standard "User" cannot access "Admin" pages by directly typing the admin URL (e.g., `/admin/dashboard`). | 🟢 Pass |
| **SEC-06** | Insecure Direct Object Reference (IDOR). | Changing the user ID in the URL (e.g., `?user_id=123` to `124`) does not display another user's private data. | 🔴 Fail |
| **SEC-07** | Hidden UI elements. | Buttons or features hidden from standard users via UI CSS cannot be executed by manipulating the API request. | 🟢 Pass |

### 🔒 3. Data Protection & Encryption
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SEC-08** | Verify HTTPS usage. | The entire application forces HTTPS. HTTP requests are strictly redirected to HTTPS (`301 Moved Permanently`). | 🟢 Pass |
| **SEC-09** | Sensitive data masking. | Credit card numbers, SSNs, and passwords are masked (`****`) in the UI and are not visible in the HTML source code. | 🟢 Pass |
| **SEC-10** | Check browser cache/autocomplete. | Forms containing sensitive info have `autocomplete="off"` to prevent the browser from saving passwords or card details. | 🟢 Pass |

### 💉 4. Input Validation (Injection & XSS)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SEC-11** | Basic Cross-Site Scripting (XSS). | Entering `<script>alert('Test')</script>` in input fields or comments does not execute the script; it is displayed as plain text or blocked. | 🟢 Pass |
| **SEC-12** | Basic SQL Injection (SQLi). | Entering `' OR 1=1 --` or `"` in search fields or login forms does not bypass authentication or cause a database error dump. | 🟢 Pass |
| **SEC-13** | File upload restrictions. | Uploading a `.exe`, `.sh`, or `.php` file instead of a `.jpg` profile picture is rejected by the server (not just the UI). | 🟢 Pass |

---

## 🛠 QA Notes & Observations
> **Insight on IDOR (SEC-06):** > During testing, I discovered a critical Insecure Direct Object Reference (IDOR) vulnerability. By intercepting the request in DevTools and changing the `order_id` parameter, I was able to view another customer's invoice. 
> *Action taken:* Immediately raised a `P1 - Critical` bug ticket in Jira, as this is a severe violation of user data privacy.

---
[⬅️ Back to Checklists Index](./)