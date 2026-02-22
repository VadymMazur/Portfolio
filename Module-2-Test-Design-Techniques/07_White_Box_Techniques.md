# 🧪 Lesson 9: Test Design Techniques (White-Box Focus)

This repository contains the completed homework for Lesson 9, covering static and dynamic testing analysis, decision coverage theory, and algorithm design for a cat-sharing application.

---

## 📊 1. Static vs. Dynamic Testing Analysis

A comparative analysis of testing techniques, highlighting their advantages and limitations.

| Feature | Static Testing | Dynamic Testing |
| :--- | :--- | :--- |
| **Main Goal** | [cite_start]Preventing defects  | [cite_start]Detecting defects  |
| **Advantage #1** | [cite_start]Low cost of fixing issues  | [cite_start]High quality standards  |
| **Advantage #2** | [cite_start]Reduces effort for bug fixes  | [cite_start]Identifies complex errors  |
| **Advantage #3** | [cite_start]Does not require a finished product  | [cite_start]Enables automation  |
| **Limitation #1** | [cite_start]Significant time spent on meetings  | [cite_start]Executed in late development stages  |
| **Limitation #2** | [cite_start]May hinder vulnerability discovery  | [cite_start]Covers limited code areas  |
| **Limitation #3** | [cite_start]Doesn't check real system behavior  | [cite_start]May detect fewer total defects  |

---

## 🧠 2. Decision & Statement Coverage Theory

### Scenario: Single "IF" Condition
**Question:** If the code has one "IF" condition (no loops or cases), why does any single test provide 50% decision coverage?
[cite_start]**Correct Statement:** This is correct because the result of any "IF" condition test will be either **True** or **False**.

### Pseudocode Analysis
**Workflow:** `Switch PC on` -> `Start MS Word` -> `IF MS Word starts THEN` -> `Write a poem` -> `Close MS Word`.
* **Required Test Cases:**
  * [cite_start]**1** for Statement Coverage.
  * [cite_start]**2** for Decision Coverage.

---

## 🐾 3. "Catstar" Startup Algorithm

I designed a decision-making algorithm for our cat photo-sharing app's interactive assistant.

### Logic Flow:
1. **Initial Prompt:** Ask the user what pet they have.
2. **Path A (User has a cat):**
   - Ask for breed type: "Short-haired" or "Long-haired?".
   - **If Long-haired:** Offer groomer contacts.
     - **If Yes:** Provide local cat salon address.
     - **If No:** Suggest a pet care store.
   - **If Short-haired:** Suggest a general pet shop.
3. **Path B (User does not have a cat):**
   - Respond: "Come back when you decide to get a pet."

### 🧪 Minimum Test Cases Required
[cite_start]To ensure 100% path and decision coverage (all questions asked and all combinations tested), a minimum of **4 test cases** is required.

---
*Prepared by Vadym Mazur*