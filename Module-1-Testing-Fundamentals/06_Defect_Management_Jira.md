# QA & Bug Management Strategy

This repository contains the documentation for our startup's transition to a professional bug-tracking system (**Jira**) and our strategic approach to defect categorization.

---

## ⚖️ 1. Severity vs. Priority: Real-World Scenarios

Understanding the difference between technical impact (**Severity**) and business urgency (**Priority**) is crucial for our "Catstar" app's success.

### 🔴 Critical Severity / 🔵 Low Priority
**Bug:** The application crashes immediately when a user attempts to upload a photo in `.TIFF` format on the "Legacy Browser Support" page.
* **Why Critical:** It is a complete system failure (crash) for that specific action. The function is entirely broken.
* **Why Low Priority:** Less than 0.5% of our users use `.TIFF` files (most use `.jpg` or `.png`), and the "Legacy" page is rarely visited. It doesn't block the main business flow.

### 🟡 Minor Severity / 🔥 Highest Priority
**Bug:** The "Donate to Cat Shelter" button on the home page has a typo: it says **"Donat now"** instead of **"Donate now"**.
* **Why Minor:** Technically, the button works perfectly. The link is active, and the transaction goes through. Nothing is "broken."
* **Why Highest Priority:** This is our main monetization/charity feature. A typo on the primary Call-to-Action (CTA) ruins brand trust and looks unprofessional to investors. It must be fixed immediately.

---

## 🔄 2. Bug Life Cycle (Jira Workflow)

To solve the team's coordination issues, we have implemented the following **Bug Life Cycle**. This ensures every defect is tracked from discovery to resolution.

### The Workflow Diagram
`New` → `Assign` → `Open` → `In Progress` → `Fixed` → `Ready for QA` → `Testing` → `Verified` → `Done`
*(Reopened / Rejected paths included)*

### Status Definitions & Rationales

| Status | Description | Why it’s necessary? |
| :--- | :--- | :--- |
| **New** | Bug is reported by QA. | Initial logging of the issue. |
| **Assign** | Responsible developer is picked. | Establishes accountability. |
| **Open / To Do** | Bug is confirmed and prioritized. | Moves the bug into the active "Work Queue." |
| **In Progress** | Developer is actively coding a fix. | Prevents double-work and shows real-time status. |
| **Fixed** | Code changes are completed. | Signals that the development phase is over. |
| **Ready for QA** | Fix is deployed to the Test Environment. | Crucial step so QA knows *where* and *when* to test. |
| **Testing** | QA is performing regression/verification. | Ensures the fix is being actively validated. |
| **Verified** | QA confirms the fix works. | Final quality gate before closing. |
| **Done** | Bug is officially closed. | Task is removed from the active sprint. |

### Handling Exceptions
* **Reopened:** If the fix fails during the `Testing` phase, the bug moves back to `Open` to ensure we don't release broken code.
* **Rejected:** Used for duplicates or issues that cannot be reproduced, keeping our backlog clean and relevant.

---

## 🚀 Conclusion
By implementing this **Jira Workflow** and strict **Severity/Priority** definitions, our "Catstar" startup ensures that we focus on what matters most: high-quality content and a seamless user experience for cat lovers worldwide.
