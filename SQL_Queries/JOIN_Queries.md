# JOIN: cardinality and data integrity

These examples use the synthetic music-store schema consistently. They are not bug-ticket or QA-workload tables.

| Query in [validation.sql](validation.sql) | Why this join or predicate | Expected evidence |
|---|---|---|
| `album_track_counts` | LEFT JOIN retains empty albums; count child IDs rather than `COUNT(*)` | Album counts 2, 1 and 0 |
| `customer_support` | LEFT JOIN retains customers without an assigned representative | Customer 3 has NULL representative |
| `invoice_details` | Inner join expands invoice lines into named tracks | Four line rows; one invoice can appear more than once |
| `orphan_invoices` | Anti-join detects missing customer references | Invoice 103 points to missing customer 999 |
| `mismatched_totals` | Group lines by invoice and compare stored total with quantity × price | Invoice 102: 250 stored vs 200 calculated cents |
| `customers_without_invoices` | NOT EXISTS avoids multiplying customer rows | Customer 3 |

Grouping albums by ID and title avoids combining different albums with identical titles. Joining a parent to multiple children changes row cardinality; aggregate children before joining another one-to-many relation to avoid inflated totals.

The two detected inconsistencies are deliberately seeded, not production findings. All queries are read-only; the verification runner recreates the fixture in memory on each run.

[Run the examples](README.md)
