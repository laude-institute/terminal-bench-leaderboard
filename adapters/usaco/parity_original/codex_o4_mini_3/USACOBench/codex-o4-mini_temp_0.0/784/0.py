#!/usr/bin/env python3
"""
Reads lifeguard shifts, computes maximum coverage after firing one lifeguard.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    intervals = []
    for _ in range(n):
        start = int(next(it))
        end = int(next(it))
        intervals.append((start, end))

    # coverage[t] = number of lifeguards covering time t
    coverage = [0] * 1000
    for start, end in intervals:
        for t in range(start, end):
            coverage[t] += 1

    # total covered time with all lifeguards
    total_covered = sum(1 for c in coverage if c > 0)

    # compute best coverage after removing one lifeguard
    best = 0
    for start, end in intervals:
        # count unique coverage of this lifeguard
        unique = 0
        for t in range(start, end):
            if coverage[t] == 1:
                unique += 1
        # coverage after firing = total - unique
        covered_after = total_covered - unique
        if covered_after > best:
            best = covered_after

    print(best)

if __name__ == '__main__':
    main()
