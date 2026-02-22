# 🧪 Black-Box Test Design Techniques: Part 2

This repository contains the completed homework for Lesson 11, focusing on State Transition Diagrams, Decision Tables, and Use Case development for a "Catstar" startup.

---

## 🟢 Must-Have Level

### 1. State Transition Analysis
**Question:** Which statement regarding the state transition diagram and the test case table is correct?  
**Answer:** **A**. [cite_start]These test cases cover both valid and invalid transitions on the diagram[cite: 1].

### 2. Decision Table: Employee Bonuses
Conditions: Employment > 1 year AND Goals achieved.  
[cite_start]**Missing Scenario Identification:** * **Scenario:** Condition 1 = YES, Condition 2 = YES, Condition 3 = NO, Action = YES[cite: 1].
* [cite_start]**Rationale:** In a real-world scenario, if the tenure and goal-setting conditions are met, a bonus might still be awarded even if a specific secondary goal wasn't fully reached[cite: 1].

---

## 🟡 Intermediate Level: Videogame Logic Testing

### 🏰 "Castle of Riddles" State Transition
The game logic involves choosing paths (Left/Right) and answering riddles from a Dragon or a Witch.

**Test Execution Summary:**
[cite_start]A total of **7 test cases** are sufficient to cover all possible outcomes (Win/Lose) and paths within the game[cite: 1].

| TC ID | Way | Player Action | Result 1 | Result 2 | Outcome |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tc1** | Right | Correct Answer | Game Ends | - | [cite_start]**Win** [cite: 1] |
| **Tc2** | Right | Wrong -> Correct | 2nd Riddle | Game Ends | [cite_start]**Win** [cite: 1] |
| **Tc3** | Right | Wrong -> Wrong | 2nd Riddle | Dragon eats you | [cite_start]**Lose** [cite: 1] |
| **Tc4** | Left | Correct Answer | Game Ends | - | [cite_start]**Win** [cite: 1] |
| **Tc5** | Left | Wrong -> Correct | Moved to Dragon | Game Ends | [cite_start]**Win** [cite: 1] |
| **Tc6** | Left | Wrong -> Wrong (1) | Moved to Dragon | 2nd Riddle (T) | [cite_start]**Win** [cite: 1] |
| **Tc7** | Left | Wrong -> Wrong (2) | Moved to Dragon | Dragon eats you | [cite_start]**Lose** [cite: 1] |

---

## 🔴 Maximum Level: Cat Photo Startup Use Cases

### A. Use Case Scenarios
1.  [cite_start]**User Registration:** Create an account via email or social media to access app features[cite: 1].
2.  [cite_start]**App Login:** Registered users log in to view and publish cat photos[cite: 1].
3.  [cite_start]**Upload Cat Photo:** Select a photo from the device, add a description, and publish it to the feed[cite: 1].
4.  [cite_start]**Feed Browsing:** Scroll through the feed and view other users' cat photos in full size[cite: 1].
5.  [cite_start]**Liking Photos:** Interact with content by liking photos to support authors[cite: 1].

### B. Decision Table: Feed Interaction
This table analyzes the system's behavior based on authorization and action states.

| Condition | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 |
| :--- | :--- | :--- | :--- | :--- |
| **Authorized?** | YES (+) | YES (+) | YES (+) | [cite_start]NO (-) [cite: 1] |
| **View Feed?** | YES (+) | NO (-) | YES (+) | [cite_start]NO (-) [cite: 1] |
| **Like Photo?** | YES (+) | NO (-) | YES (+) | [cite_start]NO (-) [cite: 1] |
| **Result** | Browses & Likes | Display Error | Auth Failure | [cite_start]Access Denied [cite: 1] |

---
*Prepared by Vadym Mazur*