# 🐛 Bug Report Log: Oxford Medical Website

**Project:** Oxford Medical  
**Environment:** OS: Windows 11 | Browsers: Chrome, Firefox, Edge | Build: ver 1.1  
**Reporter/Assignee:** Vadym Mazur  

| ID | Title | Priority | Severity | Status | Actual Result | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **bug_001** | Hotline number not fully displayed | P3•Med | S3•Maj | Open | Phone number is cut off on the main page. | [Link](https://drive.google.com/file/d/1Ch_8lhw9ty97JwEN1wnSlP4Yh4i0RqdQ/view?usp=drive_link) |
| **bug_002** | Text responsiveness issues (<1024px) | P4•Low | S3•Maj | Open | Text blocks are cut off or half-visible when resizing window. | [Link](https://drive.google.com/file/d/1mKRGmTP9jOswzFlvSn_SuBOltZ7qCdm3/view?usp=drive_link) |
| **bug_003** | Mixed target audience content | P3•Med | S3•Maj | Open | "Emergency care" container mixes visitor info and job candidate info. | [Link](https://drive.google.com/file/d/1TbdECjk4B4QOjGCKKiJBtiSdGfJ8v-cw/view?usp=drive_link) |
| **bug_004** | Confusing appointment booking UX | P1•Crit | S3•Maj | Open | Blue highlighted clinic name/date in Cart are not clickable. | [Link](https://drive.google.com/file/d/1-fmpIUdyKo1kB31KpsGz7IH_K4sIonBv/view?usp=drive_link) |
| **bug_005** | Sorting fails in "Special offers" | P3•Med | S4•Min | Open | Sorting by clinic list does not function in the offers block. | [Link](https://drive.google.com/file/d/1l37harmGmvqYVM_PnI_3lpfM-iUjH2yT/view?usp=drive_link) |
| **bug_006** | Localization defect (RU remains in UA) | P4•Low | S4•Min | Open | Header titles remain in Russian after switching to Ukrainian. | [Link](https://drive.google.com/file/d/1PeFzdwK8xRnqdoJpFoOTIKPkbvF7XfUK/view?usp=drive_link) |

---

## 🔍 Detailed Bug Descriptions

### bug_004: UX Confusing appointment booking (Critical)
* **Description:** In the Cart section, the clinic name and appointment date are highlighted in blue (mimicking links), but they are not clickable, making the booking process frustrating.
* **Steps to Reproduce:** Open site -> Add service to Cart -> Navigate to Cart -> Try to click highlighted blue text.
* **Expected Result:** Elements should be interactive or lead to the next step of the appointment.

### bug_006: Language Switcher Issue
* **Description:** Header elements do not translate when switching from RU to UA.
* **Steps to Reproduce:** Open site -> Click Language button -> Choose UA -> Observe header text.
* **Expected Result:** All header text must correspond to the selected language.Some text
