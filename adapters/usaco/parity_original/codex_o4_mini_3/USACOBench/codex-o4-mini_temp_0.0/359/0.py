#!/usr/bin/env python3
"""
Solution to Cow Baseball problem.
Counts triples (X,Y,Z) with Y to the right of X, Z to the right of Y,
and distance YZ in [XY, 2*XY].
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    positions = list(map(int, data[1:]))
    positions.sort()
    from bisect import bisect_left, bisect_right

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            d = positions[j] - positions[i]
            low = positions[j] + d
            high = positions[j] + 2 * d
            # find first k > j where positions[k] >= low
            left = bisect_left(positions, low, j+1, n)
            # find first k > j where positions[k] > high
            right = bisect_right(positions, high, j+1, n)
            # valid Z indices are in [left, right-1]
            if left < right:
                count += (right - left)
    print(count)

if __name__ == "__main__":
    main()
