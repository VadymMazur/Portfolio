# SQL validation exercises

Ten executable examples on a small synthetic music-store schema. These demonstrate data inspection and reconciliation, not access to a production database. The fixture is inspired by common music-store examples but is not a copy of Chinook or its expected outputs.

```powershell
python SQL_Queries/verify_examples.py
```

Run from the repository root with Python 3.10+. Only the standard-library SQLite engine is used; the database exists in memory and no server or credentials are needed.

| File | Purpose |
|---|---|
| [fixture.sql](fixture.sql) | Synthetic tables and seed data |
| [validation.sql](validation.sql) | Ten named SELECT queries |
| [verify_examples.py](verify_examples.py) | Executes queries and compares exact expected rows |
| [SELECT guide](SELECT_Queries.md) | Filtering, boundaries and aggregation |
| [JOIN guide](JOIN_Queries.md) | Cardinality, missing relations and reconciliation |

Two defects are deliberately seeded: invoice 103 references missing customer 999; invoice 102 stores 250 cents although its lines total 200. The fixture intentionally omits that foreign-key constraint to simulate an invalid import. A real system should prevent invalid references rather than rely only on detection queries.

Money uses integer cents to avoid floating-point comparison noise. SQLite syntax and results are verified here; portability to another SQL dialect requires a separate check.

[Back to portfolio](../README.md)
