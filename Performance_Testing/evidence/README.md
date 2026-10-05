# Historical evidence

- `recorded_run.jtl`: original raw samples, previously named `results2.jtl`; contents unchanged.
- `console_summary.png`: original console capture, previously `summary_report.png`; contents unchanged.
- `original_plan.jmx`: snapshot of the plan before the portfolio review. Contains historical public-service targets and incorrect methods under two labels; retained only for inspection, not as the recommended run configuration.

The screenshot names a locally stored plan whose path differs from the repository file. No immutable plan hash was captured with the run, so exact run-to-plan provenance cannot be established. The repository snapshot is context, not proof that every historical request used that exact configuration.

The JTL has labels, URLs and response codes but no HTTP-method column. Do not infer verified PATCH/DELETE execution from labels alone. See the [analysis](../API_Performance_Testing_Report.md).
