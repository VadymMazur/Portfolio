# 🔐 Login Form Testing Checklist

## 📌 Document Overview
The login form is the critical gateway to the application. This checklist ensures the authentication process is secure, functional, and user-friendly. It covers positive/negative scenarios, session management, and basic security vulnerability checks.

---

## 📋 Execution Summary
* **Target System:** Web Application Authentication Portal
* **Environment:** QA / Staging
* **Tester:** Vadym Mazur
* **Status Legend:** 🟢 Pass | 🔴 Fail | ⚪ Blocked / N/A

---

### 1. UI & Usability Checks
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOG-UI-01** | Verify field placeholders and labels. | "Email/Username" and "Password" fields have clear placeholders and persistent labels. | 🟢 Pass |
| **LOG-UI-02** | Test the "Tab" key navigation. | Pressing `Tab` moves focus sequentially from Email ➔ Password ➔ Login Button. | 🟢 Pass |
| **LOG-UI-03** | Verify the `Enter` key behavior. | Pressing `Enter` while inside the password field triggers the Login submission. | 🟢 Pass |
| **LOG-UI-04** | Check the "Show/Hide Password" toggle. | Clicking the eye icon toggles the password visibility between plain text and masked characters (`•`). | 🟢 Pass |

### 2. Functional Validation (Positive & Negative)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOG-FN-01** | Login with valid credentials (Positive). | User is successfully authenticated and redirected to the personalized Dashboard. | 🟢 Pass |
| **LOG-FN-02** | Login with invalid email/password (Negative). | Login is rejected. A generic error message is shown (e.g., "Invalid email or password") to prevent username enumeration. | 🟢 Pass |
| **LOG-FN-03** | Leave mandatory fields empty. | Submission is blocked. Inline validation errors highlight the empty fields in red. | 🟢 Pass |
| **LOG-FN-04** | Case sensitivity in password field. | Passwords must be strictly case-sensitive (e.g., `Pass123` is not equal to `pass123`). | 🟢 Pass |
| **LOG-FN-05** | Case insensitivity in email field. | Emails should be treated as case-insensitive (e.g., `User@mail.com` = `user@mail.com`). | 🔴 Fail |

### 3. Session Management & "Remember Me"
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOG-SM-01** | Verify "Remember Me" functionality. | If checked, the user remains logged in after closing and reopening the browser. | 🟢 Pass |
| **LOG-SM-02** | Check session termination on Logout. | Clicking "Logout" completely invalidates the session. Clicking the browser's "Back" button should not allow access to the protected page. | 🟢 Pass |
| **LOG-SM-03** | Verify concurrent logins (if restricted). | Logging in from a second device terminates the session on the first device (or prompts the user). | ⚪ N/A |

### 4. Basic Security & Edge Cases
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOG-SC-01** | Test rate limiting (Brute-force protection). | Account is temporarily locked or CAPTCHA appears after 5 consecutive failed login attempts. | 🟢 Pass |
| **LOG-SC-02** | Verify SQL Injection (SQLi) protection. | Entering `' OR 1=1 --` into the fields does not bypass authentication or cause database errors. | 🟢 Pass |
| **LOG-SC-03** | Verify network payload encryption. | Using Chrome DevTools (Network tab), verify that passwords are sent over HTTPS and are not exposed in the URL (GET method). | 🟢 Pass |

---

## 🛠 QA Notes & Observations
> **Insight:** I intentionally marked `LOG-FN-05` (Email case insensitivity) as failed. This is a very common bug where the backend registers `John@mail.com` and `john@mail.com` as two separate users. 
> Additionally, I always check the Network tab (`LOG-SC-03`) to ensure sensitive data is transmitted inside a secure POST payload, not as query parameters.

---
[⬅️ Back to Checklists Index](./)