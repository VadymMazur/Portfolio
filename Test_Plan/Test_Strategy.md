# Catstar: risk-based test strategy

**Status:** planning exercise, revised 5 October 2026. Proposed scope and criteria, not an executed project or formal sign-off. Author: Vadym Mazur.

## Assumptions and open questions

Assume registration, sign-in, photo upload, feed browsing, likes, comments and sharing. Requirements, traffic profile, supported platforms and moderation rules are not supplied. Confirm upload formats/size, visibility rules, deletion semantics, rate limits and accessibility targets before accepting cases as a release baseline.

## Scope and priorities

| Risk | Impact | Priority | First checks and oracle |
|---|---|---|---|
| Unauthorized photo/account access | Private data disclosure or mutation | High | Owner vs second account vs anonymous; API access matches visibility contract |
| Upload interruption/retry | Lost image, duplicate post, orphaned storage | High | Interrupt and retry; reconcile UI, API and storage metadata |
| Registration/login failure | Core journey blocked | High | Input partitions, expiry, logout and recovery |
| Likes/comments inconsistency | Lost/duplicate interaction | Medium | Retry and two-account updates; compare count and persisted records |
| Feed pagination | Missing/duplicate posts | Medium | Seeded feed, page boundaries and refresh after new content |
| Layout/localization | Unusable controls or misread information | Medium | Agreed device/locale set, keyboard navigation, text expansion |

Under time pressure, execute authentication, ownership and upload/persistence checks first. Record omitted areas and their risks; do not describe unexecuted scope as covered.

## Approach

1. Review requirements and assign unresolved decisions to an owner.
2. Design partitions, boundaries and transitions; map each case to a risk.
3. Verify a stable build and seeded data before deeper testing.
4. Use API checks for validation/ownership and UI journeys for user-visible integration.
5. Explore interruption/retry behavior beyond scripted happy paths.
6. Retest fixes and affected regression; retain evidence by build.

Automate stable, repeated journeys after expected behavior is agreed. Developers own unit/component checks; QA combines integration, system and exploratory evidence. Select tools for the actual platform.

## Environment and data

Use a disposable environment with recorded build, browser/device versions and configuration. Seed two users with different ownership, public/private photos if supported, boundary-sized files and a deterministic feed. Keep credentials out of reports. Clean only owned records; document leftovers after cleanup failure.

Select devices from support policy and usage data. A proposed starting set is desktop Chromium plus one real mobile device; this does not imply Safari/iOS coverage.

## Entry, exit and stop criteria

**Entry:** testable build, agreed high-risk acceptance criteria, environment, roles/data and diagnostics. Unresolved requirements block associated cases.

**Exit proposal:** agreed high-risk cases executed; no unresolved critical access or data-loss issue; fixes retested; affected regression complete. Report failed, blocked and unexecuted cases separately. Residual risk acceptance needs a named product decision-maker and rationale.

**Stop:** unexpected data outside the disposable dataset changes, environment instability invalidates results, or a blocker prevents meaningful coverage. Preserve evidence and resume after the cause is addressed.

## Defect and release reporting

A defect records build, role, preconditions, exact steps, expected basis, actual behavior, occurrence count, evidence and impact. Severity describes impact; priority is a scheduling proposal.

A release note records build, scope, executed/passed/failed/blocked counts, unresolved risks and QA recommendation. Product ownership decides release acceptance. No real approvals or release dates are asserted by this exercise.

[Back to planning index](README.md)
