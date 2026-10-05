# Localization Checklist

**Status:** learning template; not executed. Replace example limits with the product contract before use.

Record build, role, device/browser, dataset and evidence when executing. See the [status definitions](README.md).

## 1. UI, Text & Translation Verification
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LOC-01** | Verify translation completeness. | No un-translated strings, raw localization keys (e.g., `ui.button.submit`), or hardcoded text are visible. | Not run |
| **LOC-02** | Test text expansion/contraction. | UI elements (buttons, menus) dynamically adjust to longer words (e.g., German) without text truncation or overlapping. | Not run |
| **LOC-03** | Verify special characters (Encoding). | Accented characters (é, ö, ü) and Cyrillic/Asian scripts render correctly (UTF-8 encoding). | Not run |
| **LOC-04** | Check tone and context. | Terminology is consistent across the application and appropriate for the cultural context. | Not run |

## 2. Regional Formats & Standards
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **FMT-01** | Validate Date and Time formats. | Dates match local standards (e.g., `MM/DD/YYYY` for US, `DD.MM.YYYY` for de-DE) and 12h/24h time formats are respected. | Not run |
| **FMT-02** | Check Currency symbols & placement. | Currency symbols are correct and positioned properly (e.g., `$100.00` vs `100,00 €`). | Not run |
| **FMT-03** | Verify Number formatting. | Decimal and thousand separators match the locale (e.g., `1,000.50` in US vs `1.000,50` in de-DE). | Not run |
| **FMT-04** | Test measurement units. | System correctly converts and displays Metric (kg, km) vs. Imperial (lbs, miles) units. | Not run |

## 3. Layout & Alignment (RTL / LTR)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **LAY-01** | Verify Right-to-Left (RTL) support. | For languages like Arabic/Hebrew, text direction and direction-sensitive controls follow the locale design; numbers and non-directional icons retain their intended orientation. | Not run |
| **LAY-02** | Check image & icon localization. | Culturally sensitive graphics or direction-specific icons (e.g., "Next" arrows) are appropriately mirrored or localized. | Not run |

## 4. Functional & Backend L10n
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **FUN-01** | Validate Timezone calculations. | Server correctly converts UTC timestamps to the user's local timezone for notifications and logs. | Not run |
| **FUN-02** | Test linguistic sorting (Collation). | Lists (e.g., dropdowns, tables) are sorted according to the specific language's alphabet rules. | Not run |
| **FUN-03** | Input validation for local chars. | Registration forms and search bars accept and correctly process region-specific characters. | Not run |

[Back to checklist index](README.md)
