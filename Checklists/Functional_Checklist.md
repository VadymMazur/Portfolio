# Functional Testing Checklist

**Status:** learning template; not executed. Replace example limits with the product contract before use.

Record build, role, device/browser, dataset and evidence when executing. See the [status definitions](README.md).

## 1. Navigation & UI Elements
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **NAV-01** | Verify all header and footer links. | Links redirect to correct pages without `404 Not Found` errors. | Not run |
| **NAV-02** | Test breadcrumb navigation. | Breadcrumbs accurately reflect the user's location in the site hierarchy. | Not run |
| **NAV-03** | Verify logo click behavior. | Clicking the site logo consistently redirects to the Homepage. | Not run |
| **NAV-04** | Check buttons state. | Invalid submission produces clear validation; disabling the button is required only if specified by the design. | Not run |

## 2. Forms & Input Validation
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **INP-01** | Validate mandatory fields. | Submitting empty mandatory fields triggers appropriate, highlighted error messages. | Not run |
| **INP-02** | Test boundary values on inputs. | Numeric inputs outside the min/max allowed range are cleanly rejected. | Not run |
| **INP-03** | Verify special characters handling. | Legitimate punctuation is preserved; output is encoded and injection attempts do not execute. Backend protection requires separate verification. | Not run |
| **INP-04** | Check dropdown menus. | Dropdowns display correct options, default values, and are fully selectable. | Not run |

## 3. User Authentication & Security
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **AUTH-01** | Verify valid login credentials. | User is redirected to the dashboard after entering correct email and password. | Not run |
| **AUTH-02** | Verify invalid login attempts. | A clear, non-specific error message is shown (e.g., "Invalid credentials"). | Not run |
| **AUTH-03** | Test password field masking. | Password characters are masked (shown as asterisks/dots) during input. | Not run |
| **AUTH-04** | Verify session timeout. | Expiry follows the configured inactivity policy; protected requests are rejected after expiry. | Not run |

## 4. Business Logic (CRUD Operations)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **CRUD-01** | **Create:** Add new record. | Item is successfully created and instantly appears in the UI and database. | Not run |
| **CRUD-02** | **Read:** Verify displayed data. | Data displayed in the UI matches the database exactly (no truncation). | Not run |
| **CRUD-03** | **Update:** Edit existing record. | Changes are saved correctly and reflected without needing a page refresh. | Not run |
| **CRUD-04** | **Delete:** Remove existing record. | System asks for confirmation, then deletes the item. Item disappears from UI. | Not run |

[Back to checklist index](README.md)
