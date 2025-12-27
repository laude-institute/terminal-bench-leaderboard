#!/usr/bin/env python3
"""
Solution to 'Haybale Restacking'.
Compute minimum work to transform A to B on a circle.
Approach: compute prefix sums of differences, find median,
and sum absolute deviations from median.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    d = []
    idx = 1
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        d.append(a - b)
    # Build prefix sums (excluding full cycle)
    s = []
    cur = 0
    for x in d:
        s.append(cur)
        cur += x
    # Find median of prefix sums
    s.sort()
    med = s[n//2]
    # Compute total cost
    total = 0
    for x in s:
        total += abs(x - med)
    sys.stdout.write(str(total))

if __name__ == '__main__':
    main()
