#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    positions = list(map(int, data[1:]))
    positions.sort()
    count = 0
    # For each pair (i, j), count valid k
    for i in range(n):
        for j in range(i+1, n):
            d = positions[j] - positions[i]
            # Z must satisfy positions[j] + d <= positions[k] <= positions[j] + 2*d
            left = bisect.bisect_left(positions, positions[j] + d, j+1, n)
            right = bisect.bisect_right(positions, positions[j] + 2*d, j+1, n) - 1
            if left <= right:
                count += (right - left + 1)
    print(count)

if __name__ == '__main__':
    main()
