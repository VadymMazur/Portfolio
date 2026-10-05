"""Recalculate historical JMeter metrics offline; does not send HTTP requests."""

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', nargs='?', type=Path,
                        default=Path(__file__).parent / 'evidence' / 'recorded_run.jtl')
    args = parser.parse_args()
    with args.file.open(encoding='utf-8-sig', newline='') as source:
        rows = list(csv.DictReader(source))
    if not rows:
        raise SystemExit('No samples found.')
    groups = defaultdict(list)
    for row in rows:
        groups[row['label']].append(row)
    print('| Label | Samples | Errors | Mean ms | Min ms | Max ms | p90 ms | p95 ms |')
    print('|---|---:|---:|---:|---:|---:|---:|---:|')
    for label, samples in sorted(groups.items()):
        values = sorted(int(row['elapsed']) for row in samples)
        errors = sum(row['success'].lower() != 'true' for row in samples)
        p90 = values[math.ceil(.90 * len(values)) - 1]
        p95 = values[math.ceil(.95 * len(values)) - 1]
        print(f'| {label} | {len(values)} | {errors} | {sum(values)/len(values):.2f} | '
              f'{values[0]} | {values[-1]} | {p90} | {p95} |')
    start = min(int(row['timeStamp']) for row in rows)
    end = max(int(row['timeStamp']) + int(row['elapsed']) for row in rows)
    duration = (end - start) / 1000
    print(f'\nSamples: {len(rows)}; failed: {sum(r["success"].lower() != "true" for r in rows)}')
    print(f'Mean elapsed: {sum(int(r["elapsed"]) for r in rows)/len(rows):.2f} ms')
    print(f'Sample window: {duration:.3f} s; aggregate throughput: {len(rows)/duration:.2f} samples/s')
    print(f'Peak recorded active threads: {max(int(r["allThreads"]) for r in rows)}')
    print('Percentiles: nearest rank. Labels do not establish the HTTP method.')


if __name__ == '__main__':
    main()
