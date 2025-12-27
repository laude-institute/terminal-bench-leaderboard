#!/usr/bin/env python3
"""
Solution for trapping Bessie with minimum extra hay.
"""
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    B = int(next(it))
    left = []  # (pos, size)
    right = []
    for _ in range(N):
        s = int(next(it)); p = int(next(it))
        if p <= B:
            left.append((p, s))
        else:
            right.append((p, s))
    # Need bales on both sides
    if not left or not right:
        print(-1)
        return
    # Sort by position
    left.sort(key=lambda x: x[0])
    right.sort(key=lambda x: x[0])
    # Prepare suffix max of p+s for left
    L = len(left)
    ls_pos = [p for p, _ in left]
    ls_ps = [p + s for p, s in left]
    suffix_max = [0] * L
    suffix_max[-1] = ls_ps[-1]
    for i in range(L-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], ls_ps[i])
    # Prepare prefix min of p-s for right
    R = len(right)
    rs_pos = [p for p, _ in right]
    rs_ms = [p - s for p, s in right]
    prefix_min = [0] * R
    prefix_min[0] = rs_ms[0]
    for i in range(1, R):
        prefix_min[i] = min(prefix_min[i-1], rs_ms[i])
    # Evaluate candidates
    ans = float('inf')
    # Right bale blocks, left may need extra
    for p, s in right:
        low = p - s
        # find first left pos >= low
        i = bisect.bisect_left(ls_pos, low)
        if i < L:
            extra = p - suffix_max[i]
            if extra < 0:
                extra = 0
            ans = min(ans, extra)
    # Left bale blocks, right may need extra
    for p, s in left:
        high = p + s
        # find last right pos <= high
        j = bisect.bisect_right(rs_pos, high) - 1
        if j >= 0:
            extra = prefix_min[j] - p
            if extra < 0:
                extra = 0
            ans = min(ans, extra)
    # Output result
    print(-1 if ans == float('inf') else ans)

if __name__ == '__main__':
    main()
