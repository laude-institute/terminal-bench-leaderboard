#!/usr/bin/env python3
"""
Reads N, preferred temperatures p and current temperatures t,
computes the minimum number of operations to adjust stalls
so each stall reaches its preferred temperature by applying
range +1 or -1 operations.
"""

import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    p = list(map(int, data[1:1+n]))
    t = list(map(int, data[1+n:1+2*n]))

    total = 0
    prev_diff = 0
    # Iterate through stalls, compute difference array changes
    for i in range(n):
        diff = p[i] - t[i]
        total += abs(diff - prev_diff)
        prev_diff = diff
    # Return to zero at end
    total += abs(prev_diff)

    # Each operation contributes two difference changes
    print(total // 2)

if __name__ == "__main__":
    main()
