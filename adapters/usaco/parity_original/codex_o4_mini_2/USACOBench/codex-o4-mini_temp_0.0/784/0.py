#!/usr/bin/env python3
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
    # Coverage count for each time unit 0..1000
    max_time = 1000
    count = [0] * max_time
    for s, e in intervals:
        for t in range(s, e):
            count[t] += 1
    # Total covered time
    total = sum(1 for c in count if c > 0)
    # Compute best after removing one lifeguard
    best = 0
    for s, e in intervals:
        unique = 0
        for t in range(s, e):
            if count[t] == 1:
                unique += 1
        covered_if_removed = total - unique
        if covered_if_removed > best:
            best = covered_if_removed
    # Output result
    print(best)

if __name__ == '__main__':
    main()
