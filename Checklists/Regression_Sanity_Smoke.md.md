# 🔄 Testing Types Checklist: Smoke, Sanity & Regression

## 📌 Document Overview
This document outlines the standard checklists for three critical testing phases: **Smoke**, **Sanity**, and **Regression** testing. It demonstrates a structured approach to verifying builds at different stages of the Software Development Life Cycle (SDLC), ensuring both stability and correct feature implementation.

---

## 📋 Execution Summary
* **Target System:** Web/Mobile Application
* **Environment:** QA / Pre-Production
* **Tester:** Vadym Mazur
* **Status Legend:** 🟢 Pass | 🔴 Fail | ⚪ Blocked / N/A

---

### 💨 1. Smoke Testing (Build Verification Test)
*Executed immediately after a new build is deployed to ensure critical functionalities are working. "Wide and shallow" approach.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SMK-01** | Verify application launch/load. | The application loads without `500 Internal Server Error` or white screens. | 🟢 Pass |
| **SMK-02** | Test user authentication (Login). | Existing users can successfully log in and access the dashboard. | 🟢 Pass |
| **SMK-03** | Verify primary navigation. | Main menu links (Home, Profile, Settings) are accessible and functional. | 🟢 Pass |
| **SMK-04** | Core business flow check. | A user can complete the primary action (e.g., adding an item to the cart and reaching checkout). | 🟢 Pass |

### 🧠 2. Sanity Testing
*Executed after receiving a software build with minor changes in code or functionality. "Narrow and deep" approach focusing on the modified components.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **SNT-01** | Verify recent bug fixes. | Previously reported and "Fixed" defects can no longer be reproduced. | 🟢 Pass |
| **SNT-02** | Deep test of the new feature. | The newly introduced feature (e.g., "Export to PDF") works flawlessly under various conditions. | 🔴 Fail |
| **SNT-03** | Verify adjacent integrations. | Components directly interacting with the new feature (e.g., the "Print" button) still function correctly. | 🟢 Pass |
| **SNT-04** | Database schema validation. | New data entries related to the new feature are correctly saved and retrieved from the database. | 🟢 Pass |

### 🔁 3. Regression Testing
*Executed before a major release to confirm that recent code changes have not adversely affected existing features.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **REG-01** | Execute full Smoke Test suite. | All critical paths pass without issues. | 🟢 Pass |
| **REG-02** | Re-run old Test Cases. | Historical test cases across all stable modules pass consistently. | 🟢 Pass |
| **REG-03** | Verify boundary & edge cases. | Legacy modules handle extreme inputs correctly, remaining unchanged by new code. | 🟢 Pass |
| **REG-04** | Test legacy API endpoints. | Older API versions remain backward-compatible and return expected payloads. | 🟢 Pass |

---

## 🛠 QA Notes & Interview Insights
> **Strategic Difference:** > * I use **Smoke Testing** to decide whether to *accept or reject* a build for further testing. 
> * I use **Sanity Testing** to verify *specific fixes or newly added features*. 
> * I use **Regression Testing** as the final safety net before a production release to ensure *no old features were broken* by new commits.
> 
> *Note on SNT-02:* The PDF export feature failed during Sanity testing due to a formatting error. The build was NOT promoted to full Regression testing until this specific module was fixed by the development team.

---
[⬅️ Back to Checklists Index](./)