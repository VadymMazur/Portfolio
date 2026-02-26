# 🌍 Localization Checklist

## 📌 Document Overview
This checklist focuses on verifying the software's adaptability to different languages, regional differences, and technical requirements of target markets. It ensures that the application provides a native-like experience for international users without UI breakage or functional defects.

---

## 📋 Execution Summary
* **Target System:** Web/Mobile Application (Multi-language Support)
* **Environment:** QA-Staging (Locales: `en-US`, `uk-UA`, `de-DE`, `ar-SA`)
* **Tester:** Vadym Mazur
* **Status Legend:** 🟢 Pass | 🔴 Fail | ⚪ Blocked / N/A

---

### 1. UI, Text & Translation Verification
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOC-01** | Verify translation completeness. | No un-translated strings, raw localization keys (e.g., `ui.button.submit`), or hardcoded text are visible. | 🟢 Pass |
| **LOC-02** | Test text expansion/contraction. | UI elements (buttons, menus) dynamically adjust to longer words (e.g., German) without text truncation or overlapping. | 🔴 Fail |
| **LOC-03** | Verify special characters (Encoding). | Accented characters (é, ö, ü) and Cyrillic/Asian scripts render correctly (UTF-8 encoding). | 🟢 Pass |
| **LOC-04** | Check tone and context. | Terminology is consistent across the application and appropriate for the cultural context. | 🟢 Pass |

### 2. Regional Formats & Standards
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **FMT-01** | Validate Date and Time formats. | Dates match local standards (e.g., `MM/DD/YYYY` for US, `DD.MM.YYYY` for EU) and 12h/24h time formats are respected. | 🟢 Pass |
| **FMT-02** | Check Currency symbols & placement. | Currency symbols are correct and positioned properly (e.g., `$100.00` vs `100,00 €`). | 🟢 Pass |
| **FMT-03** | Verify Number formatting. | Decimal and thousand separators match the locale (e.g., `1,000.50` in US vs `1.000,50` in EU). | 🟢 Pass |
| **FMT-04** | Test measurement units. | System correctly converts and displays Metric (kg, km) vs. Imperial (lbs, miles) units. | ⚪ N/A |

### 3. Layout & Alignment (RTL / LTR)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LAY-01** | Verify Right-to-Left (RTL) support. | For languages like Arabic/Hebrew, the entire layout (menus, text alignment, progress bars) mirrors correctly. | ⚪ N/A |
| **LAY-02** | Check image & icon localization. | Culturally sensitive graphics or direction-specific icons (e.g., "Next" arrows) are appropriately mirrored or localized. | 🟢 Pass |

### 4. Functional & Backend L10n
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **FUN-01** | Validate Timezone calculations. | Server correctly converts UTC timestamps to the user's local timezone for notifications and logs. | 🟢 Pass |
| **FUN-02** | Test linguistic sorting (Collation). | Lists (e.g., dropdowns, tables) are sorted according to the specific language's alphabet rules. | 🟢 Pass |
| **FUN-03** | Input validation for local chars. | Registration forms and search bars accept and correctly process region-specific characters. | 🟢 Pass |

---

## 🛠 QA Notes & Observations
> **Insight:** Text expansion (LOC-02) is a common issue during German localization due to compound words. When this fails, I attach DevTools screenshots showing the CSS `overflow` behavior in the bug report to help front-end developers fix the container responsiveness.

---
[⬅️ Back to Checklists Index](./)