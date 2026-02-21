# 🧪 Black-Box Test Design Techniques: Part 1

[cite_start]This repository contains the completed homework for Lesson 10, focusing on **Equivalence Partitioning (EP)** and **Boundary Value Analysis (BVA)**.

---

## 🟢 Must-Have Level

### 1. Speed Control System
The system monitors speed with the following rules:
* **≤ 50 km/h:** No reaction.
* **> 50 and < 55 km/h:** Warning issued.
* **≥ 55 and < 60 km/h:** Fine issued.
* **≥ 60 km/h:** Fine + penalty points.

[cite_start]**Correct Test Dataset:** `50, 51, 55, 56, 60, 61` (Option D).
* [cite_start]**Rationale:** This set covers all equivalence classes and boundary values effectively.

### 2. Fitness App Notifications
Step count feedback logic:
* **0–1000:** "Couch Potato"
* **1001–2000:** "Lazybones"
* **2001–4000:** "Move your body!"
* **4001–6000:** "Not bad!"
* **> 6000:** "Well done, keep it up!"

[cite_start]**Correct Test Dataset:** `666, 999, 2222, 5555, 6666` (Option D).
* [cite_start]**Rationale:** This selection provides the best coverage for all defined valid equivalence classes.

---

## 🟡 Intermediate Level

### 1. Solar Exposure Device
* [cite_start]**Task:** Determine the minimum number of additional test cases needed to cover all valid equivalence classes based on time (<3h, 3-6h, >6h) and intensity (Very Low, Low, Medium, High).
* [cite_start]**Answer:** **2 additional test cases** (Option B).
* [cite_start]**Rationale:** Two more cases are required to cover the remaining valid classes and boundary values. [cite_start]Test Case 3 is redundant as it duplicates Test Case 1.

### 2. Video Playback Resolution
* [cite_start]**Question:** Which test case results from applying the Equivalence Partitioning technique for supported resolutions (640x480, 1280x720, 1600x1200, 1920x1080)? 
* [cite_start]**Answer:** **Option D** (Check any single resolution from the list).
* [cite_start]**Rationale:** Since all values belong to the same "Supported Resolution" class, testing one value assumes the others will likely work correctly as well.

---

## 🔴 Maximum Level: "Cat Lovers" Startup Requirements

### 📋 Requirements Specification
* **Photo Uploads:**
    * [cite_start]Minimum file size: **10 KB**.
    * [cite_start]Maximum file size: **10 MB**.
    * [cite_start]Resolution: **200x200 px** to **5000x5000 px**.
    * [cite_start]Formats: **JPEG, PNG, HEIC**.
* **Comments:**
    * [cite_start]Minimum length: **1 character**.
    * [cite_start]Maximum length: **500 characters**.

### 🛠 Test Cases (EP & BVA)

| TC ID | Scenario | Input/Condition | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC1** | Min Boundary (Invalid) | Photo < 10 KB | [cite_start]Upload Error  | Not executed |
| **TC2** | Max Boundary (Invalid) | Photo > 10 MB | [cite_start]Upload Error  | Not executed |
| **TC3** | Min Boundary (Valid) | Photo = 10 KB | [cite_start]Success  | Not executed |
| **TC4** | Mid Range (Valid) | Photo = 5 MB | [cite_start]Success  | Not executed |
| **TC5** | Max Boundary (Valid) | Photo = 10 MB | [cite_start]Success  | Not executed |
| **TC6** | Min Comment (Invalid) | 0 characters | [cite_start]"Send" button disabled  | Not executed |
| **TC7** | Min Comment (Valid) | 1 character | [cite_start]"Send" button active  | Not executed |
| **TC8** | Mid Comment (Valid) | 250 characters | [cite_start]"Send" button active  | Not executed |
| **TC9** | Max Comment (Valid) | 500 characters | [cite_start]"Send" button active  | Not executed |
| **TC10**| Max Comment (Invalid) | 501 characters | [cite_start]"Send" disabled / Error  | Not executed |
| **TC11**| Format Check (Invalid)| .pdf or .docx | [cite_start]"Invalid Format" message | Not executed |

---
[cite_start]*Prepared by Vadym Mazur*