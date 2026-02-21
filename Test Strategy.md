                           

\[Catstar\]

**Test Strategy**

**Revision History**

| Date | Version | Author | Description |
| :---- | :---- | :---- | :---- |
| 01.02.2026 | 1.1 | Mazur V. | Development of the “Catstar” startup |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

**Table of Contents**

**[1\. Scope	3](#scope)**

[**2\. Test Approach	4**](#test-approach)

[**3\. Test Environment	6**](#test-environment)

[**4\. Testing Tools	8**](#testing-tools)

[**5\. Release Control	10**](#release-control)

[**6\. Risk Analysis	13**](#risk-analysis)

[**7\. Review and Approvals	14**](#review-and-approvals)

1. # **Scope** {#scope}

This document defines the scope of testing for the “Catstar” application. It covers the main features of the app, including user registration, login, photo upload, viewing the feed, liking and commenting on photos, and sharing them with other users.

It also defines the following parameters:

Document Review: The QA Lead will review this document to ensure accuracy and completeness.

Document Approval: The Product Manager will approve this document before testing activities begin.

Testing Activities and Timelines: Testing will include functional testing, basic non-functional testing (usability, performance, compatibility, and security), and regression testing. All testing activities will follow the timelines defined in the test schedule, which will be updated as the product and QA team grow.

This scope ensures that all critical features are tested and verified while maintaining proper review and approval processes.

2. # **Test Approach** {#test-approach}

**1\. Testing Process:**  
The testing process will follow these steps:

* Review requirements and design documents.

* Prepare test cases and test data.

* Execute tests according to the plan.

* Report and track defects.

* Re-test fixed defects.

* Perform regression testing for new releases.

* Approve testing results before release.

**2\. Test Levels**

* **Unit Testing:** Done by Developers to test small parts of the code.

* **Integration Testing:** Test how different parts of the system work together.

* **System Testing:** Test the whole application with all features.

* **Acceptance Testing:** Ensure the app meets product requirements.

**3\. Roles and Responsibilities**

* **Product Manager (PM):** Approves the testing strategy and verifies that the app meets business requirements.

* **UX/UI Designer:** Reviews usability and design-related issues.

* **Frontend Developer:** Performs unit tests for the user interface.

* **Backend Developer:** Performs unit and integration tests for APIs and server logic.

* **Mobile Developer:** Performs unit and integration tests for mobile app features.

* **QA Lead:** Oversees all QA activities, assigns tasks, and approves final test results.

* **QA Engineer / Tester:** Writes and executes test cases, reports defects, and performs regression testing.

* **Marketing Specialist:** Provides feedback on app functionality from a user perspective.

* **Content Moderator:** Checks user content compliance and reports related issues.

**4\. Types of Testing**

* **Functional Testing:** Ensure features work correctly (uploading photos, likes, comments, sharing).

* **Usability Testing:** Check that the app is easy and pleasant to use.

* **Performance Testing:** Test how the app performs under load.

* **Security Testing:** Verify user data and app security.

* **Regression Testing:** Ensure new changes do not break existing functionality.

* **Compatibility Testing:** Test on different devices, OS versions, and browsers.

**5\. Testing Approach and Automation Tools**

* Manual testing will cover core features and exploratory testing.

* Automation testing will be used for repetitive tasks such as regression tests.

* Suggested tools: Selenium, Appium, or other lightweight automation tools, depending on the app platform.

**6\. Defect Management**

* All defects are logged in the tracking system ( Jira, Trello).

* Defects are prioritized, assigned, and resolved by Developers.

* QA re-tests fixed defects.

* Regression testing is performed before each release.

* The QA Lead and Product Manager give final testing approval.

3. # **Test Environment** {#test-environment}

**1\. 1\. Development Environment**

Windows / macOS

1. IDE / Code Editor – a tool for writing and editing code (Visual Studio, Xcode, Android Studio, etc.).

2. Local Database – a local database to test application features.

3. Required Libraries / SDKs – libraries and SDKs needed for frontend and backend development.

4. Network Access – access to internal servers and APIs.

5. Developer Accounts – user accounts to test authentication and API features.

**1.2. QA / Testing Environment**

**Windows / macOS**

1. **App Installed** – the application or web version installed for testing.

2. **Test Accounts** – user accounts for different test scenarios.

3. **Access to Test Server** – connection to servers with test data.

4. **Browsers** – installed browsers for cross-browser testing (Chrome, Edge, Safari).

5. **Network Access** – stable connection to the internet and internal servers.

6. **Logging / Monitoring Tools** – tools to track errors and logs.

**Android**

1. **App Installed** – test version of the app on a device or emulator.

2. **Test Accounts** – user accounts for testing.

3. **Device or Emulator** – a real Android device or emulator.

4. **Network Access** – access to test servers and the internet.

5. **Logging / Monitoring Tools** – tools to track errors.

**iOS**

1. **App Installed** – test version of the app on a device or simulator.

2. **Test Accounts** – user accounts for testing.

3. **Device or Simulator** – iPhone, iPad, or iOS simulator.

4. **Network Access** – access to test servers and the internet.

5. **Logging / Monitoring Tools** – tools to track errors.

**1.3. Staging Environment (All Platforms)**

2. **Backup and Restore Strategy**

All test data and environment configurations will be backed up to a **secure cloud storage** or **dedicated backup server**.

* **Cloud Storage:** Use services like AWS S3, Google Cloud Storage, or Azure Blob to store backups safely.

* **Dedicated Backup Server:** A separate server that holds copies of test databases and environment files.

* **Frequency:** Backups will be done **daily** for active test data and **before major testing cycles**.

* **Restore:** Data can be restored from backup to any test environment to ensure consistency and to reset environments after testing.

* **Security:** Backups will be encrypted and access-controlled to protect sensitive data.

This ensures that test environments are reliable and testing can continue even if data is lost or corrupted.

4. # **Testing Tools** {#testing-tools}

The following tools will be used for testing the “Catstar” app:

**1\. Test Management Tools**

* **Jira / Trello:** To create, track, and manage test cases and defects.

* **TestRail / Zephyr (optional):** To organize test plans, test suites, and reporting.

**2\. Automation Tools**

* **Selenium:** For automated testing of web application features.

* **Appium:** For automated testing of mobile apps on Android and iOS.

* **Postman / REST Assured:** For API testing and automation.

**3\. Performance and Load Testing Tools**

* **JMeter / Locust:** To test app performance under load.

**4\. Logging and Monitoring Tools**

* **ELK Stack (Elasticsearch, Logstash, Kibana) / Sentry:** To monitor errors and logs during testing.

**Usage Guidelines:**

* Manual testing will be performed for new features and exploratory testing.

* Automation tools will be used for regression testing and repetitive scenarios.

* Test management tools will track all test cases, execution results, and defects.

This set of tools ensures effective test execution, tracking, and reporting across all platforms and environments.

2. **Testing Tools Plan**

**Open-Source Tools**

* **Selenium** – automated web testing

  * **Number of users:** 2–3 QA Engineers \+ 1 QA Lead

* **Appium** – automated mobile testing (Android & iOS)

  * **Number of users:** 2–3 QA Engineers \+ 1 QA Lead

* **Postman / REST Assured** – API testing

  * **Number of users:** 2 QA Engineers \+ 1 Backend Developer

* **JMeter / Locust** – performance and load testing

  * **Number of users:** 1–2 QA Engineers \+ 1 QA Lead

**Total open-source tools:** 4

**Commercial Tools**

* **Jira** – test management, defect tracking

  * **Number of users:** All QA Engineers, QA Lead, PM, and Developers

* **TestRail** – advanced test case management

  * **Number of users:** All QA Engineers \+ QA Lead

**Total commercial tools:** 2

---

**3\. Planning and Usage**

* Open-source tools are mainly used for **automation, performance, and API testing**.

* Commercial tools are used for **test management, tracking, and reporting**.

* All QA Engineers and QA Lead have access to all tools. Developers and PM have access to test management tools for visibility.

5. # **Release Control** {#release-control}

This section describes the release control process for the “Catstar” application. The goal is to make sure that all changes included in a release are properly tested and approved.

**Release Management Plan**

Each release will follow a defined release plan that includes a clear scope of changes, testing activities, and timelines. All new features, improvements, and bug fixes must pass required testing before release.

**Version History**

* Each release will have a unique version number.

* A version history will be maintained and updated for every release.

* The version history will include release date, list of changes, fixed defects, and known issues.

    
  Example:

| Version | Release Date | List of changes | Fixed defects | Known Issues: |  Approved By  |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1.1 | 02.02.2026 | Added photo comments feature | Fixed crash on Android during app launch | Image preview loads slowly on older Android devices | QA LeadProject Manager |
| 1.2  | 03.02.2026 | Improved photo upload speed | Fixed the issue where photo upload failed on slow networks | Minor UI misalignment on macOS Safari  | QA LeadProject Manager |


**Testing Coverage for Releases**

* All changes in a release must be tested in the QA and Staging environments.

* Regression testing will be performed to ensure that existing functionality is not affected.

* Automated tests will be executed where available, especially for critical flows.

* Test results must be documented and reviewed by the QA Lead.

**Release Approval**

* The QA Lead confirms that all planned tests are completed and passed.

* The Product Manager approves the release based on test results and business readiness.

* Only approved releases can be deployed to production.

This release control process ensures quality, traceability, and stability for every release.

**Entry and Exit Criteria for Release**

This section defines the conditions that must be met before testing starts (Entry Criteria) and before a release is approved (Exit Criteria). These criteria help ensure that testing is well-organized and that only stable versions are released.

**Entry Criteria (Start of Testing)**

Testing for a release can start when the following conditions are met:

* Requirements and user stories are clearly defined and approved by the Product Manager.

* The application build is deployed to the QA environment and is stable.

* Test environments are ready and accessible (Windows, macOS, Android, iOS).

* Test data is available or restored from backup.

* Test cases are prepared and reviewed by the QA Lead.

* No critical blocking issues exist in the build.

**Exit Criteria (Release Approval)**

A release can be approved when the following conditions are met:

* All planned test cases are executed.

* No open **Critical** or **High** severity defects remain.

* All fixed defects are re-tested and passed.

* Regression testing is completed successfully.

* Test results are documented and reviewed by the QA Lead.

* The Product Manager approves the release based on test results and business readiness.


  **Defect Severity and Priority Definition**

This section defines how defects are classified by **severity** and **priority**. This helps the team understand the impact of a defect and decide how quickly it must be fixed.

**Defect Severity**

Severity indicates the defect's severity and its impact on the application.

* **Critical**  
  The application crashes, or a main feature does not work. Users cannot use the app.

* **High**  
  A major feature works incorrectly, but the app is still usable.

* **Medium**  
  A feature works incorrectly, but there is a workaround.

* **Low**  
  Minor issues such as small UI problems or text errors. The app works normally.

  **Defect Priority**

Priority shows how quickly the defect must be fixed.

* **High Priority**  
  Must be fixed immediately or before the next release.

* **Medium Priority**  
  Should be fixed soon, but not critical for the current release.

* **Low Priority**  
  Can be fixed in a future release.

* **Severity vs Priority Rules**

* Severity is defined by the **QA Engineer** when the defect is reported.

* The Product Manager sets priority in agreement with the **QA Lead**.

* A defect can have **high severity but low priority**, or **low severity but high priority**, depending on business needs.

6. # **Risk Analysis** {#risk-analysis}

**Risk Management**

This section describes possible risks that may affect testing, quality, or release timelines, and how the team will manage them.

**Identified Risks and Mitigation**

* **Unclear or changing requirements**  
  *Risk:* Tests may be incomplete or incorrect.  
  *Mitigation:* Regular requirement reviews with the Product Manager and early QA involvement.

* **Limited test environments or devices**  
  *Risk:* Issues may appear only on some platforms (Windows, macOS, Android, iOS).  
  *Mitigation:* Use real devices and emulators/simulators, and prioritize testing on critical platforms.

* **Lack of test data**  
  *Risk:* Test scenarios cannot be fully executed.  
  *Mitigation:* Prepare test data in advance and use backup and restore strategies.

* **Time constraints before release**  
  *Risk:* Not all tests can be executed.  
  *Mitigation:* Focus on critical features and use risk-based testing and automation where possible.

* **High number of defects close to release**  
  *Risk:* Release delay or quality issues.  
  *Mitigation:* Continuous testing, early defect reporting, and clear exit criteria.

* **Automation instability**  
  *Risk:* Automated tests give false results.  
  *Mitigation:* Regular maintenance of automated tests and review by the QA Lead.

  **Risk Monitoring and Ownership**

* The **QA Lead** is responsible for identifying and tracking testing risks.

* The **Product Manager** decides on risk acceptance or release impact.

* Risks are reviewed during sprint planning and release meetings.

This risk management approach helps the team reduce issues, keep quality high, and deliver stable releases.

7. # **Review and Approvals** {#review-and-approvals}

This section describes how testing activities and related documents are reviewed and approved.

All testing activities, plans, and strategy documents are reviewed and approved by the **business team**, **project management**, and the **development team**, as required. This ensures that testing aligns with business goals, project timelines, and technical requirements.

Any updates or changes to the test strategy must go through the same review and approval process.

A summary of review changes must be tracked at the beginning of the document. This summary should include:

* Approval date

* Version name or number

* Description of changes

* Review comments

This process provides transparency, traceability, and clear ownership for all changes made to the document.

**Review and Approval Log (Example)**

This log records all reviews and approvals of the test strategy document.

**Version:** 1.0  
**Approval Date:** February 1, 2026

* **Reviewed By:**

  * QA Lead

  * Development Team Representative

  * Business Team Representative

* **Approved By:**

  * Product Manager

    

    **Summary of Changes:**

Initial version of the test strategy created and reviewed.

**Comments:**  
Document approved for use in the project.

