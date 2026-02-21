# 🏦 Monobank Mobile App: Test Documentation & Estimation Analysis

This repository contains professional QA documentation for the **Monobank** mobile application, focusing on core banking functionalities. It includes high-level and low-level test cases, along with a detailed time estimation using industry-standard techniques.

---

## 📋 1. Test Cases Suite

### High-Level Test Case
| Field | Details |
| :--- | :--- |
| **ID** | `MONO_001` |
| **Summary** | Verify core functionality for an authorized user. |
| **Description** | Ensure that the user can successfully log in and utilize primary features: balance check, transaction history, and financial transfers. |
| **Preconditions** | Active account, app installed, stable internet connection. |
| **Expected Result** | Core features work correctly without critical errors or crashes. |
| **Priority** | High |

---

### Low-Level Test Cases (LLTC)

#### LLTC MONO_001: User Authorization
* **Summary:** Authenticate user via phone number and PIN/Biometrics.
* **Steps:**
    1. Launch the Monobank app.
    2. Enter the registered phone number.
    3. Receive and enter the SMS confirmation code.
    4. Confirm entry using PIN code or Biometrics.
* **Expected Result:** User is successfully authorized; the main dashboard is displayed.
* **Priority:** High

#### LLTC MONO_002: Balance & History Visualization
* **Summary:** Verify correct display of card balance and transaction list.
* **Steps:**
    1. Navigate to the main screen.
    2. Check the card balance display.
    3. Tap on the card to open transaction history.
    4. Scroll through the transaction list.
* **Expected Result:** Balance is accurate; history loads without errors; transaction details (date, amount, description) are correct.
* **Priority:** High

#### LLTC MONO_003: Funds Transfer
* **Summary:** Execute a money transfer between cards.
* **Steps:**
    1. Navigate to the "Transfers" (Перекази) section.
    2. Select the sender's card.
    3. Enter the recipient's card details and transfer amount.
    4. Confirm the operation (PIN/Biometrics).
* **Expected Result:** Transfer is successful; status is displayed; card balance updates immediately.
* **Priority:** High

---

## ⏱️ 2. Time Estimation Analysis

### Execution Breakdown per Environment
| Test Case ID | Execution Time |
| :--- | :--- |
| LLTC_MONO_001 | 3 minutes |
| LLTC_MONO_002 | 3 minutes |
| LLTC_MONO_003 | 4 minutes |
| **Net Execution Time** | **10 minutes** |

**Total Estimated Time Calculation:**
* **Base Time:** 10 mins
* **Buffer (30% for unforeseen issues):** +3 mins
* **Bug Reporting (Administrative overhead):** +10 mins
* **Total:** **25 minutes** per mobile environment (iOS/Android).

---

## 📈 3. Estimation Techniques Applied

### Technique A: WBS (Work Breakdown Structure)
We decomposed each task into granular sub-tasks to ensure accuracy:

* **Authorization (3.5 mins):** Launch (30s) + Phone entry (30s) + SMS wait/entry (1.5m) + PIN/Result (1m).
* **Balance & History (3.5 mins):** Navigation (30s) + Balance check (30s) + History loading (1m) + Data validation (1.5m).
* **Transfers (5 mins):** Section navigation (1m) + Data entry (2m) + Confirmation (1m) + Status check (1m).
* **WBS Total (with buffer & reporting):** **26 minutes**.



### Technique B: Three-Point Estimation (PERT)
To account for risks, we used the following values:
* **Optimistic ($a$):** 25 mins (Everything goes perfectly)
* **Most Likely ($m$):** 26 mins (Based on WBS)
* **Pessimistic ($b$):** 60 mins (Network issues, complex bugs found)

**Formula:** $E = \frac{a + 4m + b}{6}$ 
*(Note: Using the standard PERT weighted average for higher accuracy)*

$$E = \frac{25 + (4 \times 26) + 60}{6} = \frac{189}{6} \approx 31.5 \text{ minutes}$$

> **Final Decision:** We should allocate **~32-35 minutes** for this test suite to remain realistic and reliable.

---
*Created by [VadymMazur/QA] for QA Portfolio.*
