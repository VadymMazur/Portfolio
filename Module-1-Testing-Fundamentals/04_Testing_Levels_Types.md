📑 Testing Levels & Type
| Testing Type          | What is tested                          | When applied                          | Limitations                                                                 | Features                                                                 |
|------------------------|-----------------------------------------|---------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Functional testing** | External system behavior                | Security testing, Interaction testing | Does not evaluate system quality: performance, load, security, usability, scalability | Possible logical errors may be missed; risk of over-testing              |
| **Non-functional testing** | How the system works                | Load testing, Stress testing, Stability/Reliability, Volume testing, Installation, Usability, Failover & Recovery, Configuration | High cost and complexity; environment dependency; does not check business logic | Automated testing simulating multiple business users on the resource     |
| **Regression testing** | Confirmation of program operability     | After bug fixes, updates, releases    | Impossible to test 100% due to limited time/resources; does not find new defect types | Includes Smoke Testing, Build Verification, Sanity Testing; applied after merges, migrations, OS/DB/web/app server changes |

## 🔄 Difference Between Regression and Retestin
- Regression testing checks the operability of existing functionality after system changes.
- Retesting verifies a specific bug fix to confirm it has been resolved.
- Regression covers a broader set of tests, while retesting focuses on one or a few related cases.
- The goal of regression is to detect side effects of changes; the goal of retesting is to confirm the fix.
- Regression is repeated in every release, while retesting is performed only after a specific bug fix

## ⚖️ Is Functional Testing Alone Enough?
Functional testing alone is insufficient for commercial products, because even correctly working features may be slow, insecure, or inconvenient.
Non-functional requirements directly affect user experience, stability, and trust in the product.
Limiting testing only to functionality is risky and may lead to product failure.
Theoretically, functional testing may be enough for educational or demo products where performance and usability are not critical.

## 💨 Smoke Testing Necessity
Smoke testing is essential for quick verification that the system is suitable for further testing after a new build or release.
It helps detect critical/blocking defects early (e.g., app not launching, core functions broken).
This prevents wasting time on deep testing of an unstable product.
Smoke testing is relevant almost always, especially in CI/CD pipelines

## 🧪 Test Cases (Cat App Example)
### TC-01: Upload cat photo
- Status: Not executed
- Precondition: User is authorized
- Steps: Upload photo → Select cat photo → Confirm
- Expected Result: Photo successfully uploaded and displayed in feed

### TC-02: Restriction on non-cat photos
- Status: Not executed
- Precondition: User is authorized
- Steps: Upload photo → Select dog/human photo → Confirm
- Expected Result: Error message, photo not uploaded

### TC-03: Add friend
- Status: Not executed
- Precondition: Another user exists
- Steps: Search user → Click "Add friend"
- Expected Result: User added to friends list

### TC-04: Like photo
- Status: Not executed
- Precondition: Photo exists in feed
- Steps: Open feed → Click heart icon
- Expected Result: Likes count increases by 1

### TC-05: Add comment
- Status: Not executed
- Precondition: Photo exists in feed
- Steps: Open photo → Enter comment → Send
- Expected Result: Comment appears under photo

## 📋 Non-Functional Requirement
1. **Performance**
   - Requirement: Photo upload ≤ 3 seconds
   - Verification: Test under Wi-Fi/4G, measure upload time

2. **Reliability / Stability**
   - Requirement: No crashes during 100 consecutive actions
   - Verification: Stress test with repeated actions

3. **Security**
   - Requirement: User data (login, email, photos) protected
   - Verification: Unauthorized access attempts, encryption checks

4. **Usability**
   - Requirement: Upload photo or like in ≤ 3 clicks
   - Verification: Usability test with real users

5. **Scalability**
   - Requirement: Support 1000 concurrent users without slowdown
   - Verification: Load test with 1000 virtual users