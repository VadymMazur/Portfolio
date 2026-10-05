# Vadym Mazur | QA Engineer

Web and API testing, test design, SQL validation and Python automation.

This portfolio shows how I investigate failures, check persisted data and turn a defect into a focused regression plan. Start with the case studies; the supporting sections contain planning exercises and reproducible technical examples.

## Selected work

| Work sample | What it demonstrates | Evidence |
|---|---|---|
| **Reserved lead status accepted by the API** | Negative testing of a business rule; response assertions; follow-up GET to verify persistence | [Case study, 5-page PDF](Bug_Reports/TC-API-LEAD-006_QA_Case.pdf) |
| **Telegram connection failure** | UI/network investigation; reproduction steps; separation of observed failure from unconfirmed root cause | [Case study, 2-page PDF](Bug_Reports/CQ-2_Telegram_QA_Case.pdf) |
| **Lead creation: risk and regression design** | Input partitions, state transitions, side-effect checks and proposed release decisions | [Test design](Test_Design/Lead_Creation.md) |
| **UI automation** | Python, Playwright, pytest, Page Objects, UI/API checks, guarded cleanup and Allure | [autotest_ui repository and CI](https://github.com/VadymMazur/autotest_ui) |
| **Performance result review** | Recalculation from raw JMeter samples; mislabeled methods; limits on capacity conclusions | [Reproducible analysis](Performance_Testing/API_Performance_Testing_Report.md) |
| **SQL data validation** | Joins, aggregation, missing relations and total reconciliation on synthetic data | [Runnable SQL exercises](SQL_Queries/README.md) |

## Repository guide

| Folder | Contents |
|---|---|
| [Bug_Reports](Bug_Reports/README.md) | Two CRM cases and three historical website observation logs |
| [Test_Design](Test_Design/Lead_Creation.md) | Proposed coverage derived from the lead-status case; evidence status per case |
| [Test_Plan](Test_Plan/README.md) | Catstar planning exercise: product risks, priorities and release criteria |
| [Checklists](Checklists/README.md) | Unexecuted learning templates for functional, login, localization, security and performance checks |
| [API_Testing](API_Testing/README.md) | Request-design exercises and Postman JavaScript snippets; no exported collection |
| [SQL_Queries](SQL_Queries/README.md) | SQL source, synthetic fixture and a local verification command |
| [Performance_Testing](Performance_Testing/README.md) | Historical evidence, offline analyzer and revised local JMeter plan |
| [Mindmaps](Mindmaps/README.md) | Mermaid reference diagrams for test planning and defect workflow |

## How to read the evidence

- CRM PDFs document supplied observations. They do not claim that defects remain present in later builds or that fixes passed a retest.
- Checklist outcomes are not execution results. Planning assumptions and new regression cases are explicitly marked as proposed.
- The JMeter report describes one short historical run. It does not establish production capacity, an SLA or full API correctness.
- SQL exercises use synthetic data; expected results can be reproduced with Python's standard library.
- Automation CI checks unit tests and synthetic browser interactions. The full CRM journey requires a compatible local application.

## Contact

[LinkedIn](https://www.linkedin.com/in/vadym-mazur-qa/) · [Email](mailto:vadik.mazur@gmail.com) · [Telegram](https://t.me/vadimX9)
