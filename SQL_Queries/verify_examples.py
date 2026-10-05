"""Execute the documented exercises against an in-memory synthetic fixture."""

import re
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED = {
    'customers_by_country': [(1, 'Customer Alpha', 'USA'), (2, 'Customer Beta', 'Canada')],
    'longest_matching_tracks': [(2, 'Love Example B', 350000), (1, 'Love Example A', 300000)],
    'invoice_range': [(101, 300), (102, 250)],
    'revenue_by_country': [('USA', 1, 300), ('Canada', 1, 250)],
    'album_track_counts': [(1, 'Synthetic Album A', 2), (2, 'Synthetic Album B', 1), (3, 'Empty Album', 0)],
    'customer_support': [(1, 'Customer Alpha', 'Support Alpha'), (2, 'Customer Beta', 'Support Beta'), (3, 'Customer Gamma', None)],
    'invoice_details': [(101, 'Love Example A', 100, 1), (101, 'Love Example B', 100, 2), (102, 'Another Example', 100, 2), (103, 'Love Example A', 100, 1)],
    'orphan_invoices': [(103, 999)],
    'mismatched_totals': [(102, 250, 200)],
    'customers_without_invoices': [(3,)],
}


def main():
    parts = re.split(r'^-- name: (\w+)\s*$', (ROOT / 'validation.sql').read_text(), flags=re.M)
    queries = list(zip(parts[1::2], parts[2::2]))
    if len(queries) != len(EXPECTED) or {name for name, _ in queries} != set(EXPECTED):
        raise SystemExit('The query list and expected-result catalogue differ.')
    with sqlite3.connect(':memory:') as connection:
        connection.executescript((ROOT / 'fixture.sql').read_text())
        for name, sql in queries:
            actual = connection.execute(sql).fetchall()
            if actual != EXPECTED[name]:
                raise SystemExit(f'{name}: expected {EXPECTED[name]!r}, got {actual!r}')
            print(f'PASS {name}: {actual}')
    print(f'{len(queries)} SQL examples verified; no external database used.')


if __name__ == '__main__':
    main()
