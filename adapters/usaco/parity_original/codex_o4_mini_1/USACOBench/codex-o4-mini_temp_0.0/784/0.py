#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    intervals = []  # list of (start, end)
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        intervals.append((a, b))

    # time range 0..1000, track coverage count per unit
    max_time = 1000
    cover = [0] * max_time
    for a, b in intervals:
        for t in range(a, b):
            cover[t] += 1

    # total covered time
    total_covered = sum(1 for t in range(max_time) if cover[t] > 0)

    # find minimum unique coverage among lifeguards
    min_unique = total_covered  # upper bound
    for a, b in intervals:
        unique = 0
        for t in range(a, b):
            if cover[t] == 1:
                unique += 1
        if unique < min_unique:
            min_unique = unique

    # best coverage after firing one = total - smallest unique
    result = total_covered - min_unique
    print(result)

if __name__ == '__main__':
    main()
