# JMeter: configuration and evidence review

This section demonstrates how to inspect a test plan, recalculate results and identify limits in the evidence. It contains a historical public-demo run and a separate corrected local method-check plan.

| Artifact | Purpose |
|---|---|
| [Analysis](API_Performance_Testing_Report.md) | Recalculated metrics and findings |
| [Historical evidence](evidence/README.md) | Original samples, console screenshot and pre-review plan |
| [Offline analyzer](analyze_results.py) | Reproduces metrics without sending requests |
| [Revised JMeter plan](Test_plan.jmx) | Correct HTTP methods; ten requests against loopback by default |
| [Local stub](local_stub.py) | Stateless synthetic responses for checking plan wiring |

## Reproduce the recorded metrics

From the repository root, with Python 3.10+:

```powershell
python Performance_Testing/analyze_results.py
```

The script reads the committed JTL, uses elapsed response time, and calculates p90/p95 with the nearest-rank method. It does not run a load test.

## Check the revised plan locally

Requires Java and Apache JMeter; the plan was checked with JMeter 5.6.3. In the first terminal:

```powershell
python Performance_Testing/local_stub.py
```

In another terminal, from the repository root:

```powershell
New-Item -ItemType Directory -Force Performance_Testing/output
jmeter -n -t Performance_Testing/Test_plan.jmx -l Performance_Testing/output/local-smoke.jtl -j Performance_Testing/output/jmeter.log
```

Use a fresh output filename for each run so samples are not appended to an earlier run. Stop the stub with Ctrl+C. If port 8765 is occupied, choose another local port with `--port` on the stub and `-Jport=` on JMeter.

The plan uses two groups, each with one user, one loop and five requests: GET, POST, PUT, PATCH and DELETE. It checks the stub's expected status codes and a 1000 ms duration limit. That duration is a local smoke guard, not a product SLA. Writes are echoed without persistence; this check establishes method wiring, not CRUD correctness or capacity. Generated output is ignored by Git.

**Local verification, 5 October 2026:** JMeter completed 10/10 samples without errors; the local server log confirmed two requests for each of GET, POST, PUT, PATCH and DELETE. This verifies wiring against the stub only.

The historical public-service plan is retained for audit only. New load experiments require an owned/authorized test system, agreed workload, duration, stop criteria and monitoring.

[Back to portfolio](../README.md)
