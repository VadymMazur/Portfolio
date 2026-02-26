# 🎨 Mindmap: Test Design Techniques

## 📌 Overview
Test design techniques are essential for writing effective and efficient test cases. By applying these methods, a QA Engineer can maximize test coverage while minimizing the execution time, ensuring that critical bugs are caught without redundant testing.

---

## 🧠 Test Design Classification

```mermaid
graph LR
  TDT((Test Design)) --> Black[Black Box <br/> Specification-based]
  TDT --> White[White Box <br/> Structure-based]
  TDT --> Exp[Experience-based]

  %% Black Box Techniques
  Black --> EP[Equivalence Partitioning]
  Black --> BVA[Boundary Value Analysis]
  Black --> DT[Decision Tables]
  Black --> ST[State Transition]
  Black --> UC[Use Case Testing]

  %% White Box Techniques
  White --> SC[Statement / Logic Coverage]
  White --> DC[Branch / Path Coverage]

  %% Experience-based Techniques
  Exp --> EG[Error Guessing]
  Exp --> ET[Exploratory Testing]

  ```
## 🔑 Core Black Box Techniques Explained
As a Manual QA, I heavily utilize Black Box techniques to validate business logic and user flows:

### 1. Equivalence Partitioning (EP)
Dividing input data into equivalent classes (both valid and invalid).

Goal: Instead of testing every possible value, test only one representative value from each partition to reduce test execution time.

### 2. Boundary Value Analysis (BVA)
Testing the extreme edges of input ranges.

Goal: Bugs frequently occur at the boundaries of conditions. I test the exact boundary value, one step below, and one step above (e.g., min-1, min, min+1).

### 3. Decision Tables
Creating a matrix of conditions and expected actions.

Goal: Perfect for complex business logic where different combinations of inputs result in different outcomes (e.g., calculating shipping discounts based on user role and cart total).

### 4. State Transition
Testing the software's behavior as it moves from one state to another.

Goal: Highly effective for e-commerce (e.g., Cart -> Checkout -> Paid -> Shipped) or security flows (e.g., Account Locked after 3 failed login attempts).

### 5. Use Case Testing
Designing tests based on user interactions and specific actor scenarios.

Goal: Validating the end-to-end functionality from the end-user's perspective.

### 🛠 When to apply?
Strict Validation Rules: Combine EP + BVA for fields like passwords, age restrictions, or price filters.

Complex Financial Logic: Use Decision Tables to map out tax rates or loan approvals.

User Journeys: Apply State Transition and Use Case Testing to verify checkout flows and order lifecycles.

[⬅️ Back to Mindmaps Index](./README.md)