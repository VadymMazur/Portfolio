# JMeter run review: JSONPlaceholder

**Historical run:** 1 March 2026, as shown in the console capture and sample timestamps. **Analysis revised:** 5 October 2026. No new load was sent to the public service during this review.

## Result and interpretation

The committed JTL contains **3,000 samples**, all marked `success=true`. Recalculated mean elapsed response time is **138.04 ms**, not the earlier report's approximate 132 ms. This is a recorded sampler result, not proof that every API behavior or business rule passed.

## Recalculated metrics

Labels below are preserved exactly as recorded. They do not prove which HTTP method was sent.

| Label | Samples | Errors | Mean ms | Min ms | Max ms | p90 ms | p95 ms |
|---|---:|---:|---:|---:|---:|---:|---:|
| Delete -> | 600 | 0 | 156.02 | 134 | 484 | 145 | 372 |
| GET ->List of posts | 600 | 0 | 63.44 | 26 | 505 | 99 | 124 |
| Patch -> | 600 | 0 | 149.40 | 134 | 483 | 145 | 154 |
| Post -> | 600 | 0 | 155.68 | 134 | 451 | 153 | 357 |
| Put -> | 600 | 0 | 165.65 | 134 | 485 | 355 | 362 |

- **Observed sample window:** 11.707 seconds, from earliest start to latest start + elapsed time.
- **Aggregate throughput over that window:** 256.26 samples/second.
- **Peak recorded `allThreads`:** 126 active JMeter threads. This is neither open socket count nor requests/second.
- **Percentiles:** nearest rank, calculated independently within each label.

The console reports 254.4 samples/second over its own run interval. Its denominator differs from the JTL sample window; the two throughput figures should not be presented as the same calculation. The `elapsed` field is response time; it is not the separate JMeter `Latency` field.

Run `python Performance_Testing/analyze_results.py` from the repository root to reproduce this table.

## Plan audit

The [archived plan](evidence/original_plan.jmx) contains two groups: 100 users each, ramp-up periods of 10 and 2 seconds, three loops, and five samplers per loop. Its nominal request count is **2 × 100 × 3 × 5 = 3,000**. The previous report used four samplers and an incorrect 1,200-request subtotal.

Four material limitations were found:

1. Samplers labeled `Patch ->` and `Delete ->` are configured as **PUT in both groups**. The JTL does not include request methods, so PATCH/DELETE coverage cannot be established from the labels.
2. The plan's duration assertions are **1000 ms**, not the previously described 500 ms.
3. Several response assertions accept either 200 or 201 rather than requiring an operation-specific code. A green sampler can therefore conceal a wrong method or weak expectation.
4. Size assertions constrain recorded byte counts. They do not validate JSON schema, persisted state, packet integrity or absence of server memory problems.

The console names a local plan with a different path/name from the repository file. No exact plan hash was stored with the run. The archived configuration is relevant context, but exact run-to-plan identity is unconfirmed.

## What the run does not establish

This short sample does not determine maximum capacity, sustained-load stability, recovery, memory leaks or a production SLA. No CPU, memory, database or backend traces are provided. Response-size consistency does not prove correct business data. The thread-group name "Stress Testing" does not prove a breaking point was reached.

JSONPlaceholder simulates create/update/delete responses rather than persisting those changes. Consequently, successful write responses here are not evidence of database persistence. [JSONPlaceholder guide](https://jsonplaceholder.typicode.com/guide/)

## Correction and next experiment

The [revised plan](Test_plan.jmx) uses actual PATCH/DELETE methods, explicit JSON headers, per-method expected codes and a loopback target. It is intentionally a ten-request smoke check against the [synthetic stub](local_stub.py), separate from the historical measurement. The original evidence remains unchanged.

For a meaningful performance experiment, first specify a business workload, independent test data, baseline, warm-up and sustained duration, latency percentiles/error thresholds, monitoring and stop criteria on an authorized environment. Evaluate persistence and side effects separately from timings.

[JMeter component reference](https://jmeter.apache.org/usermanual/component_reference.html) · [Evidence files](evidence/README.md) · [Back to performance index](README.md)
