# Login Form Testing Checklist

**Status:** learning template; not executed. Replace example limits with the product contract before use.

Record build, role, device/browser, dataset and evidence when executing. See the [status definitions](README.md).

## 1. UI & Usability Checks
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOG-UI-01** | Verify field placeholders and labels. | "Email/Username" and "Password" fields have clear placeholders and persistent labels. | Not run |
| **LOG-UI-02** | Test the "Tab" key navigation. | Pressing `Tab` moves focus sequentially from Email -> Password -> Login button. | Not run |
| **LOG-UI-03** | Verify the `Enter` key behavior. | Pressing `Enter` while inside the password field triggers the Login submission. | Not run |
| **LOG-UI-04** | Check the "Show/Hide Password" toggle. | Clicking the eye icon toggles the password visibility between plain text and masked characters (`•`). | Not run |

## 2. Functional Validation (Positive & Negative)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOG-FN-01** | Login with valid credentials (Positive). | User is successfully authenticated and redirected to the personalized Dashboard. | Not run |
| **LOG-FN-02** | Login with invalid email/password (Negative). | Login is rejected. A generic error message is shown (e.g., "Invalid email or password") to prevent username enumeration. | Not run |
| **LOG-FN-03** | Leave mandatory fields empty. | Submission is blocked. Inline validation errors highlight the empty fields in red. | Not run |
| **LOG-FN-04** | Case sensitivity in password field. | Passwords must be strictly case-sensitive (e.g., `Pass123` is not equal to `pass123`). | Not run |
| **LOG-FN-05** | Case insensitivity in email field. | Login and duplicate handling follow the documented email-normalization policy; test case variants consistently. | Not run |

## 3. Session Management & "Remember Me"
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOG-SM-01** | Verify "Remember Me" functionality. | If checked, the user remains logged in after closing and reopening the browser. | Not run |
| **LOG-SM-02** | Check session termination on Logout. | Clicking "Logout" completely invalidates the session. Clicking the browser's "Back" button should not allow access to the protected page. | Not run |
| **LOG-SM-03** | Verify concurrent logins (if restricted). | Logging in from a second device terminates the session on the first device (or prompts the user). | Not run |

## 4. Basic Security & Edge Cases
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOG-SC-01** | Test rate limiting (Brute-force protection). | The configured rate-limit/lockout threshold is enforced; test below, at and above it without assuming a fixed count. | Not run |
| **LOG-SC-02** | Verify SQL Injection (SQLi) protection. | Entering `' OR 1=1 --` into the fields does not bypass authentication or cause database errors. | Not run |
| **LOG-SC-03** | Verify network payload encryption. | Using Chrome DevTools (Network tab), verify that passwords are sent over HTTPS and are not exposed in the URL (GET method). | Not run |

[Back to checklist index](README.md)
