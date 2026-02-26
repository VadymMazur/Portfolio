# ⏱️ Performance & Load Testing Checklist

## 📌 Document Overview
This checklist defines the criteria for validating system responsiveness, stability, and resource consumption under varying workloads. It encompasses both client-side rendering performance and server-side backend load handling.

---

## 📋 Execution Summary
* **Target System:** E-commerce REST API & Frontend Web Portal
* **Environment:** Staging / Pre-Production
* **Primary Tool:** Apache JMeter (Server-side), Chrome DevTools (Client-side)
* **Tester:** Vadym Mazur
* **Status Legend:** 🟢 Pass | 🔴 Fail | ⚪ Blocked / N/A

---

### 1. Client-Side Performance (Web/UI)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **PRF-UI-01** | Verify initial Page Load Time (LCP). | The largest content element renders within 2.5 seconds on a standard 4G connection. | 🟢 Pass |
| **PRF-UI-02** | Check static resource caching. | Repeated visits return `304 Not Modified` for images, CSS, and JS (browser caching is active). | 🟢 Pass |
| **PRF-UI-03** | Validate payload size & optimization. | Images are properly compressed (WebP/JPEG) and large JavaScript bundles are minified. | 🔴 Fail |

### 2. Standard Load Testing (API/Backend)
*Simulating expected, normal day-to-day user traffic.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **PRF-LD-01** | Test baseline API response time. | Under normal load (e.g., 100 concurrent users), the `GET /products` endpoint responds in < 500ms. | 🟢 Pass |
| **PRF-LD-02** | Verify Error Rate during sustained load. | The API error rate (e.g., `500 Internal Server Error`, `504 Timeout`) remains below 1%. | 🟢 Pass |
| **PRF-LD-03** | Database query performance. | Complex search queries do not cause database deadlocks or noticeable spikes in latency. | 🟢 Pass |

### 3. Stress & Spike Testing
*Pushing the system beyond its normal capacity to find the breaking point.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **PRF-ST-01** | Spike Test (Sudden traffic surge). | System handles a sudden 5x traffic spike (e.g., a "Black Friday" sale) without instantly crashing. | 🟢 Pass |
| **PRF-ST-02** | Identify the breaking point. | Determine the exact number of concurrent users required to degrade the response time beyond 5 seconds. | ⚪ N/A |
| **PRF-ST-03** | Graceful degradation & Recovery. | Once the stress load is removed, the system automatically recovers to normal response times without manual restarts. | 🔴 Fail |

### 4. Endurance / Soak Testing
*Running a normal load over an extended period.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **PRF-EN-01** | Monitor for Memory Leaks. | After running a steady load for 12+ hours, server memory usage remains stable (does not constantly climb). | ⚪ N/A |
| **PRF-EN-02** | Token & Session expiration handling. | Simulated users successfully re-authenticate when their access tokens expire during a long-running test. | 🟢 Pass |

---

## 🛠 QA Notes & Observations
> **JMeter Implementation Details:** > For the Load and Stress tests (`PRF-LD-01`, `PRF-ST-01`), I configured a **Thread Group** with an appropriate Ramp-up period to avoid artificial DoS simulation. 
> 
> **Defect Noted (PRF-ST-03):** During stress testing, the system failed to recover automatically after hitting 1,000 concurrent requests. The backend required a manual container restart. A critical bug has been logged for the DevOps team.

---
[⬅️ Back to Checklists Index](./)