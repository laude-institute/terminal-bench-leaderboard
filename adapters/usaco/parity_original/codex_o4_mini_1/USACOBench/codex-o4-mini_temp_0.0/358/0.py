#!/usr/bin/env python3
"""
Problem: Record Keeping
Reads groups of three cow names, counts occurrences of each group (order-insensitive),
and prints the maximum occurrence count.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    # First value is N, the number of records
    it = iter(data)
    n = int(next(it))
    counts = {}
    # Process each group of three names
    for _ in range(n):
        group = [next(it), next(it), next(it)]
        # Sort to normalize order
        key = tuple(sorted(group))
        counts[key] = counts.get(key, 0) + 1
    # Find the maximum occurrence
    max_count = max(counts.values()) if counts else 0
    print(max_count)

if __name__ == '__main__':
    main()
