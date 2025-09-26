#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    L = int(data[1])
    c = list(map(int, data[2:2+n]))
    c.sort()
    # Binary search for maximum h
    left, right = 0, n
    while left < right:
        mid = (left + right + 1) // 2
        # Count papers with citations >= mid
        idx = bisect.bisect_left(c, mid)
        cnt_ge = n - idx
        # Count papers with citations == mid-1
        lo = bisect.bisect_left(c, mid-1)
        hi = bisect.bisect_right(c, mid-1)
        cnt_eq = hi - lo
        # Number of additional citations needed
        needed = max(0, mid - cnt_ge)
        # Check if we can boost enough papers
        if needed <= L and needed <= cnt_eq:
            left = mid
        else:
            right = mid - 1
    print(left)

if __name__ == "__main__":
    main()
