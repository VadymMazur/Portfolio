# SELECT: filtering and aggregation

The executable source is [validation.sql](validation.sql); exact expected rows are in [verify_examples.py](verify_examples.py).

| Query | QA purpose | Expected result |
|---|---|---|
| `customers_by_country` | Verify membership in an allowed country set | Customers 1 and 2, ordered deterministically |
| `longest_matching_tracks` | Check pattern matching and descending numeric sort | Track 2 (350000 ms), then track 1 (300000 ms) |
| `invoice_range` | Verify inclusive numeric boundaries | Invoices 101 (300 cents) and 102 (250 cents) |
| `revenue_by_country` | Compare grouped invoice totals | USA: 300; Canada: 250 cents |

`BETWEEN` includes both endpoints. The fixture checks the upper boundary, an interior value and an outside value; it does not by itself cover every boundary partition.

Aggregation joins only known customers. Invoice 103 is excluded because its customer is missing; the separate orphan query is essential to avoid hiding bad data in a plausible revenue report. Revenue here means stored invoice totals, not reconciled line totals or proof of a payment.

`HAVING SUM(i.TotalCents)` states the aggregate explicitly. Stable secondary sort keys make tied results reproducible. NULL behavior and collation need separate fixtures for broader coverage.

[Run the examples](README.md)
