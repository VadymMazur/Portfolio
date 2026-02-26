# 🐾 [Catstar] Test Strategy

## 📜 Revision History

| Date | Version | Author | Description |
| :--- | :---: | :--- | :--- |
| **01.02.2026** | `1.1` | Mazur V. | Development of the “Catstar” startup |

---

## 📑 Table of Contents

1. [Scope](#1-scope)
2. [Test Approach](#2-test-approach)
3. [Test Environment](#3-test-environment)
4. [Testing Tools](#4-testing-tools)
5. [Release Control](#5-release-control)
6. [Risk Analysis](#6-risk-analysis)
7. [Review and Approvals](#7-review-and-approvals)

## 1. Scope

> This document defines the scope of testing for the **“Catstar”** application. It covers the main features of the app, including user registration, login, photo upload, viewing the feed, liking and commenting on photos, and sharing them with other users.

It also defines the following parameters:

* **📝 Document Review:** The QA Lead will review this document to ensure accuracy and completeness.
* **✅ Document Approval:** The Product Manager will approve this document before testing activities begin.
* **⏱️ Testing Activities and Timelines:** Testing will include functional testing, basic non-functional testing (usability, performance, compatibility, and security), and regression testing. All testing activities will follow the timelines defined in the test schedule, which will be updated as the product and QA team grow.

*This scope ensures that all critical features are tested and verified while maintaining proper review and approval processes.*

## 2. Test Approach

### 🔄 2.1 Testing Process
The testing process will follow these steps:
1. **Review** requirements and design documents.
2. **Prepare** test cases and test data.
3. **Execute** tests according to the plan.
4. **Report and track** defects.
5. **Re-test** fixed defects.
6. **Perform** regression testing for new releases.
7. **Approve** testing results before release.

### 🎚️ 2.2 Test Levels

| Test Level | Description |
| :--- | :--- |
| **Unit Testing** | Done by Developers to test small parts of the code. |
| **Integration Testing** | Test how different parts of the system work together. |
| **System Testing** | Test the whole application with all features. |
| **Acceptance Testing**| Ensure the app meets product requirements. |

### 👥 2.3 Roles and Responsibilities

| Role | Responsibilities |
| :--- | :--- |
| **Product Manager (PM)** | Approves the testing strategy and verifies that the app meets business requirements. |
| **UX/UI Designer** | Reviews usability and design-related issues. |
| **Frontend Developer** | Performs unit tests for the user interface. |
| **Backend Developer** | Performs unit and integration tests for APIs and server logic. |
| **Mobile Developer** | Performs unit and integration tests for mobile app features. |
| **QA Lead** | Oversees all QA activities, assigns tasks, and approves final test results. |
| **QA Engineer / Tester** | Writes and executes test cases, reports defects, and performs regression testing. |
| **Marketing Specialist** | Provides feedback on app functionality from a user perspective. |
| **Content Moderator** | Checks user content compliance and reports related issues. |

### 🎯 2.4 Types of Testing
* ⚙️ **Functional Testing:** Ensure features work correctly (uploading photos, likes, comments, sharing).
* 🧑‍💻 **Usability Testing:** Check that the app is easy and pleasant to use.
* 🚀 **Performance Testing:** Test how the app performs under load.
* 🛡️ **Security Testing:** Verify user data and app security.
* 🔁 **Regression Testing:** Ensure new changes do not break existing functionality.
* 📱 **Compatibility Testing:** Test on different devices, OS versions, and browsers.

### 🛠️ 2.5 Testing Approach and Automation Tools
* **Manual testing** will cover core features and exploratory testing.
* **Automation testing** will be used for repetitive tasks such as regression tests.
* **Suggested tools:** Selenium, Appium, or other lightweight automation tools, depending on the app platform.

### 🐞 2.6 Defect Management
* All defects are logged in the tracking system (Jira, Trello).
* Defects are prioritized, assigned, and resolved by Developers.
* QA re-tests fixed defects.
* Regression testing is performed before each release.
* The QA Lead and Product Manager give final testing approval.

## 3. Test Environment

### 💻 3.1 Development Environment (Windows / macOS)
* **IDE / Code Editor:** A tool for writing and editing code (Visual Studio, Xcode, Android Studio, etc.).
* **Local Database:** A local database to test application features.
* **Required Libraries / SDKs:** Libraries and SDKs needed for frontend and backend development.
* **Network Access:** Access to internal servers and APIs.
* **Developer Accounts:** User accounts to test authentication and API features.

### 🧪 3.2 QA / Testing Environment

| Platform | Environment Requirements |
| :--- | :--- |
| 🖥️ **Windows / macOS** | • **App Installed:** The application or web version<br>• **Test Accounts:** For different test scenarios<br>• **Access to Test Server:** Connection to test data<br>• **Browsers:** Chrome, Edge, Safari<br>• **Network Access:** Stable internet/internal servers<br>• **Logging / Monitoring:** Tools to track errors |
| 🤖 **Android** | • **App Installed:** Test version on device or emulator<br>• **Test Accounts:** User accounts for testing<br>• **Device / Emulator:** Real Android device or emulator<br>• **Network Access:** Access to test servers/internet<br>• **Logging / Monitoring:** Tools to track errors |
| 🍏 **iOS** | • **App Installed:** Test version on device or simulator<br>• **Test Accounts:** User accounts for testing<br>• **Device / Simulator:** iPhone, iPad, or iOS simulator<br>• **Network Access:** Access to test servers/internet<br>• **Logging / Monitoring:** Tools to track errors |

### 🚀 3.3 Staging Environment (All Platforms)
*(The staging environment will mirror the production environment configurations to ensure accurate final testing before release).*

### 💾 3.4 Backup and Restore Strategy
All test data and environment configurations will be backed up to a secure cloud storage or dedicated backup server.

| Strategy Component | Details |
| :--- | :--- |
| ☁️ **Cloud Storage** | Use services like AWS S3, Google Cloud Storage, or Azure Blob to store backups safely. |
| 🗄️ **Dedicated Server** | A separate server that holds copies of test databases and environment files. |
| ⏱️ **Frequency** | Backups will be done daily for active test data and before major testing cycles. |
| 🔄 **Restore** | Data can be restored from backup to any test environment to ensure consistency and to reset environments after testing. |
| 🛡️ **Security** | Backups will be encrypted and access-controlled to protect sensitive data. |

> *This ensures that test environments are reliable and testing can continue even if data is lost or corrupted.*

## 4. Testing Tools

The following tools will be used for testing the **“Catstar”** app to ensure effective test execution, tracking, and reporting across all platforms and environments.

### 🛠️ 4.1 Tool Categories & Stack

| Category | Tools | Purpose |
| :--- | :--- | :--- |
| 📋 **Test Management** | Jira / Trello<br>TestRail / Zephyr *(optional)* | Create, track, and manage test cases, test suites, and defects. |
| 🤖 **Automation** | Selenium<br>Appium<br>Postman / REST Assured | Automated web testing.<br>Automated mobile testing (Android & iOS).<br>API testing and automation. |
| ⚡ **Performance** | JMeter / Locust | Test app performance under load. |
| 📊 **Monitoring** | ELK Stack / Sentry | Monitor errors and logs during testing. |

### 📈 4.2 Testing Tools Plan (Licensing & Allocation)

| License Type | Tool | Allocated Users |
| :--- | :--- | :--- |
| 🟢 **Open-Source**<br>*(Total: 4)* | **Selenium**<br>**Appium**<br>**Postman / REST Assured**<br>**JMeter / Locust** | 2–3 QA Engineers + 1 QA Lead<br>2–3 QA Engineers + 1 QA Lead<br>2 QA Engineers + 1 Backend Developer<br>1–2 QA Engineers + 1 QA Lead |
| 💼 **Commercial**<br>*(Total: 2)* | **Jira**<br>**TestRail** | All QA Engineers, QA Lead, PM, and Developers<br>All QA Engineers + QA Lead |

### 💡 4.3 Planning and Usage Guidelines

* 🧑‍💻 **Manual vs. Automation:** Manual testing will be performed for new features and exploratory testing. Automation tools (open-source) will be used for regression testing and repetitive scenarios.
* 📝 **Test Management:** Commercial tools (Jira, TestRail) will track all test cases, execution results, and defects.
* 🔐 **Access & Visibility:** All QA Engineers and the QA Lead have access to all tools. Developers and the PM have access to test management tools for full visibility.

## 5. Release Control

> This section describes the release control process for the **“Catstar”** application. The goal is to make sure that all changes included in a release are properly tested, version-controlled, and approved.

### 🔄 5.1 Release Management Plan
Each release will follow a defined release plan that includes a clear scope of changes, testing activities, and timelines. All new features, improvements, and bug fixes must pass required testing before release.

### 🌿 5.2 Git Branching & Version Control
To maintain code stability and align with the release testing cycles, the team follows a strict Git branching strategy:
* **`main` / `master` branch:** Contains only stable, production-ready code. Every approved release is merged here and explicitly tagged with the release version (e.g., `v1.1`, `v1.2`).
* **`develop` branch:** The main integration branch where new features are combined. Basic QA checks (smoke tests) can be performed here.
* **`release/vX.X` branches:** Created from `develop` specifically for the QA and Staging phases. Once this branch is created, no new features are added—only bug fixes identified during QA testing are committed here until the release is approved.
* **`hotfix` branches:** Created directly from `main` to address critical production defects. These require immediate QA verification before being merged back into `main` and `develop`.


### 📦 5.3 Version History
Each release will have a unique version number explicitly tied to a Git tag. A version history will be maintained to track changes, fixed defects, and known issues.

| Version | Release Date | List of changes | Fixed defects | Known Issues | Approved By |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1.1** | `02.02.2026` | Added photo comments feature | Fixed crash on Android during app launch | Image preview loads slowly on older Android devices | QA Lead, PM |
| **1.2** | `03.02.2026` | Improved photo upload speed | Fixed the issue where photo upload failed on slow networks | Minor UI misalignment on macOS Safari | QA Lead, PM |

### 🧪 5.4 Testing Coverage for Releases
* All changes in a release must be tested in the QA and Staging environments.
* Regression testing will be performed to ensure that existing functionality is not affected.
* Automated tests will be executed where available, especially for critical flows.
* Test results must be documented and reviewed by the QA Lead.

### ✅ 5.5 Release Approval
1. The **QA Lead** confirms that all planned tests are completed and passed.
2. The **Product Manager** approves the release based on test results and business readiness.
3. Only approved releases (from the specific `release` branch) can be deployed to production.

---

### 🚪 5.6 Entry and Exit Criteria for Release

| 🟢 Entry Criteria (Start of Testing) | 🔴 Exit Criteria (Release Approval) |
| :--- | :--- |
| 🔲 Requirements and user stories are clearly defined and approved by the PM.<br>🔲 The app build is deployed to the QA environment and is stable.<br>🔲 Test environments are ready and accessible (Windows, macOS, Android, iOS).<br>🔲 Test data is available or restored from backup.<br>🔲 Test cases are prepared and reviewed by the QA Lead.<br>🔲 No critical blocking issues exist in the build. | 🔲 All planned test cases are executed.<br>🔲 No open Critical or High severity defects remain.<br>🔲 All fixed defects are re-tested and passed.<br>🔲 Regression testing is completed successfully.<br>🔲 Test results are documented and reviewed by the QA Lead.<br>🔲 The PM approves the release based on test results and business readiness. |

---

### 🐞 5.7 Defect Severity and Priority Definition

#### 🔴 Defect Severity (Impact on the application)
| Level | Description |
| :---: | :--- |
| **Critical** | The application crashes, or a main feature does not work. Users cannot use the app. |
| **High** | A major feature works incorrectly, but the app is still usable. |
| **Medium** | A feature works incorrectly, but there is a workaround. |
| **Low** | Minor issues such as small UI problems or text errors. The app works normally. |

#### ⏱️ Defect Priority (Urgency of the fix)
| Level | Description |
| :---: | :--- |
| **High** | Must be fixed immediately or before the next release. |
| **Medium** | Should be fixed soon, but not critical for the current release. |
| **Low** | Can be fixed in a future release. |

#### ⚖️ Severity vs Priority Rules
* **Severity** is defined by the *QA Engineer* when the defect is reported.
* **Priority** is set by the *Product Manager* in agreement with the *QA Lead*.
* *Rule of thumb:* A defect can have high severity but low priority, or low severity but high priority, depending on business needs.

## 6. Risk Analysis

### 🛡️ 6.1 Risk Management
This section describes possible risks that may affect testing, quality, or release timelines, and how the team will manage them.

### ⚠️ 6.2 Identified Risks and Mitigation

| Risk Category | 🔴 Potential Risk (Impact) | 🟢 Mitigation Strategy |
| :--- | :--- | :--- |
| **Unclear or changing requirements** | Tests may be incomplete or incorrect. | Regular requirement reviews with the Product Manager and early QA involvement. |
| **Limited test environments or devices** | Issues may appear only on some platforms (Windows, macOS, Android, iOS). | Use real devices and emulators/simulators, and prioritize testing on critical platforms. |
| **Lack of test data** | Test scenarios cannot be fully executed. | Prepare test data in advance and use backup and restore strategies. |
| **Time constraints before release** | Not all tests can be executed. | Focus on critical features and use risk-based testing and automation where possible. |
| **High number of defects close to release**| Release delay or quality issues. | Continuous testing, early defect reporting, and clear exit criteria. |
| **Automation instability** | Automated tests give false results. | Regular maintenance of automated tests and review by the QA Lead. |

### 👁️‍🗨️ 6.3 Risk Monitoring and Ownership
* 🧑‍✈️ **The QA Lead** is responsible for identifying and tracking testing risks.
* 👔 **The Product Manager** decides on risk acceptance or release impact.
* 🔄 **Meetings:** Risks are reviewed during sprint planning and release meetings.

> *This risk management approach helps the team reduce issues, keep quality high, and deliver stable releases.*

## 7. Review and Approvals

> This section describes how testing activities and related documents are reviewed and approved. All testing activities, plans, and strategy documents must align with business goals, project timelines, and technical requirements.

### 🔄 7.1 The Approval Process
Any updates or changes to the test strategy must go through a formal review and approval process:
1. **Drafting / Updating:** The QA team drafts the document or proposes changes.
2. **Review:** The Business Team, Project Management, and the Development Team review the document as required.
3. **Tracking:** A summary of review changes (Approval date, Version, Description) must be recorded in the **Revision History** at the beginning of this document.
4. **Approval:** The Product Manager provides final sign-off.

*This process provides transparency, traceability, and clear ownership for all changes made to the document.*

### ✍️ 7.2 Formal Sign-off Matrix
This log records all formal reviews and approvals of the current Test Strategy document version.

**Current Version:** `1.0` | **Approval Date:** `February 1, 2026`

| Role | Name / Title | Status | Comments |
| :--- | :--- | :---: | :--- |
| **QA Lead** | *[Name/Title]* | 🔍 Reviewed | Initial version of the test strategy created and reviewed. |
| **Dev Representative** | *[Name/Title]* | 🔍 Reviewed | No technical blockers identified. |
| **Business Representative** | *[Name/Title]* | 🔍 Reviewed | Aligns with business goals. |
| **Product Manager** | *[Name/Title]* | ✅ **Approved** | Document approved for use in the project. |

*(Note: Any future major updates to the strategy will require a new sign-off cycle).*

