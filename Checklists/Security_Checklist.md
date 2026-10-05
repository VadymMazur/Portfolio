# Security Testing Checklist (Basic OWASP)

**Status:** learning template; not executed. Replace example limits with the product contract before use.

Record build, role, device/browser, dataset and evidence when executing. See the [status definitions](README.md).

## 1. Authentication & Session Management
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SEC-01** | Verify password transmission. | Credentials travel over HTTPS and are absent from URLs and logs; DevTools can still show the request body locally. | Not run |
| **SEC-02** | Check session expiration (Timeout). | The session automatically terminates after a period of inactivity (e.g., 15-30 minutes). | Not run |
| **SEC-03** | Verify concurrent logins. | A user cannot be logged in simultaneously from multiple devices/browsers (if restricted by business logic). | Not run |
| **SEC-04** | "Back" button after Logout. | Clicking the browser's "Back" button after logging out does not restore the authenticated session. | Not run |

## 2. Authorization & Access Control (Broken Access Control)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SEC-05** | Role-Based Access Control (RBAC). | A standard "User" cannot access "Admin" pages by directly typing the admin URL (e.g., `/admin/dashboard`). | Not run |
| **SEC-06** | Insecure Direct Object Reference (IDOR). | Changing the user ID in the URL (e.g., `?user_id=123` to `124`) does not display another user's private data. | Not run |
| **SEC-07** | Hidden UI elements. | Buttons or features hidden from standard users via UI CSS cannot be executed by manipulating the API request. | Not run |

## 3. Data Protection & Encryption
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SEC-08** | Verify HTTPS usage. | Sensitive flows use HTTPS; verify the agreed HTTP redirect or rejection policy rather than requiring one redirect code. | Not run |
| **SEC-09** | Sensitive data masking. | The server returns only permitted sensitive fields; masking and access controls follow the contract. CSS masking alone is insufficient. | Not run |
| **SEC-10** | Check browser cache/autocomplete. | Autocomplete attributes match field purpose and password-manager behavior; sensitive server responses follow the cache policy. Autocomplete is not a security boundary. | Not run |

## 4. Input Validation (Injection & XSS)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SEC-11** | Basic Cross-Site Scripting (XSS). | Entering `<script>alert('Test')</script>` in input fields or comments does not execute the script; it is displayed as plain text or blocked. | Not run |
| **SEC-12** | Basic SQL Injection (SQLi). | Entering `' OR 1=1 --` or `"` in search fields or login forms does not bypass authentication or cause a database error dump. | Not run |
| **SEC-13** | File upload restrictions. | Uploading a `.exe`, `.sh`, or `.php` file instead of a `.jpg` profile picture is rejected by the server (not just the UI). | Not run |

[Back to checklist index](README.md)
