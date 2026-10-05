# Testing Types Checklist: Smoke, Sanity & Regression

**Status:** learning template; not executed. Replace example limits with the product contract before use.

Record build, role, device/browser, dataset and evidence when executing. See the [status definitions](README.md).

## 1. Smoke Testing (Build Verification Test)
*Executed immediately after a new build is deployed to ensure critical functionalities are working. "Wide and shallow" approach.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SMK-01** | Verify application launch/load. | The application loads without `500 Internal Server Error` or white screens. | Not run |
| **SMK-02** | Test user authentication (Login). | Existing users can successfully log in and access the dashboard. | Not run |
| **SMK-03** | Verify primary navigation. | Main menu links (Home, Profile, Settings) are accessible and functional. | Not run |
| **SMK-04** | Core business flow check. | A user can complete the primary action (e.g., adding an item to the cart and reaching checkout). | Not run |

## 2. Sanity Testing
*Executed after receiving a software build with minor changes in code or functionality. "Narrow and deep" approach focusing on the modified components.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SNT-01** | Verify recent bug fixes. | Previously reported and "Fixed" defects can no longer be reproduced. | Not run |
| **SNT-02** | Deep test of the new feature. | The newly introduced feature (e.g., "Export to PDF") meets the documented acceptance criteria. | Not run |
| **SNT-03** | Verify adjacent integrations. | Components directly interacting with the new feature (e.g., the "Print" button) still function correctly. | Not run |
| **SNT-04** | Database schema validation. | New data entries related to the new feature are correctly saved and retrieved from the database. | Not run |

## 3. Regression Testing
*Executed before a major release to confirm that recent code changes have not adversely affected existing features.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **REG-01** | Execute full Smoke Test suite. | All critical paths pass without issues. | Not run |
| **REG-02** | Re-run old Test Cases. | Historical test cases across all stable modules pass consistently. | Not run |
| **REG-03** | Verify boundary & edge cases. | Legacy modules handle extreme inputs correctly, remaining unchanged by new code. | Not run |
| **REG-04** | Test legacy API endpoints. | Older API versions remain backward-compatible and return expected payloads. | Not run |

[Back to checklist index](README.md)
