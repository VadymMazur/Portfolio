# Performance & Load Testing Checklist

**Status:** learning template; not executed. Replace example limits with the product contract before use.

Record build, role, device/browser, dataset and evidence when executing. See the [status definitions](README.md).

## 1. Client-Side Performance (Web/UI)
| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **PRF-UI-01** | Measure Largest Contentful Paint (LCP), separately from full load time. | Record device/network and agreed LCP target. Evaluate repeated measurements; a single navigation is not field-performance evidence. | Not run |
| **PRF-UI-02** | Check static resource caching. | Fresh cached resources may need no request; stale validators can produce 304. Check cache headers and observed revalidation behavior. | Not run |
| **PRF-UI-03** | Validate payload size & optimization. | Images are properly compressed (WebP/JPEG) and large JavaScript bundles are minified. | Not run |

## 2. Standard Load Testing (API/Backend)
*Simulating expected, normal day-to-day user traffic.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **PRF-LD-01** | Test baseline API response time. | Under normal load (e.g., 100 concurrent users), the `GET /products` endpoint responds in < 500ms. | Not run |
| **PRF-LD-02** | Verify Error Rate during sustained load. | The API error rate (e.g., `500 Internal Server Error`, `504 Timeout`) remains below 1%. | Not run |
| **PRF-LD-03** | Database query performance. | Complex search queries do not cause database deadlocks or noticeable spikes in latency. | Not run |

## 3. Stress & Spike Testing
*Pushing the system beyond its normal capacity to find the breaking point.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **PRF-ST-01** | Spike Test (Sudden traffic surge). | System handles a sudden 5x traffic spike (e.g., a "Black Friday" sale) without instantly crashing. | Not run |
| **PRF-ST-02** | Identify the breaking point. | Identify the first tested workload that violates agreed latency/error criteria; record duration and distinguish virtual users from requests per second. | Not run |
| **PRF-ST-03** | Graceful degradation & Recovery. | Once the stress load is removed, the system automatically recovers to normal response times without manual restarts. | Not run |

## 4. Endurance / Soak Testing
*Running a normal load over an extended period.*

| Task ID | Verification Step | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **PRF-EN-01** | Monitor for Memory Leaks. | After running a steady load for 12+ hours, server memory usage remains stable (does not constantly climb). | Not run |
| **PRF-EN-02** | Token & Session expiration handling. | Simulated users successfully re-authenticate when their access tokens expire during a long-running test. | Not run |

[Back to checklist index](README.md)
