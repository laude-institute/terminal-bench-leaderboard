#!/usr/bin/env python3
"""
Solution for cow meetings problem.
"""
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    N = int(data[0]); L = int(data[1])
    idx = 2
    total_weight = 0
    times = []
    rights = []
    lefts = []
    for _ in range(N):
        w = int(data[idx]); x = int(data[idx+1]); d = int(data[idx+2])
        idx += 3
        total_weight += w
        if d == -1:
            # time to left barn
            t = x
            lefts.append(x)
        else:
            # time to right barn
            t = L - x
            rights.append(x)
        times.append((t, w))
    # Find earliest time T when stopped weight >= half
    times.sort()
    half = (total_weight + 1) // 2
    cum = 0
    T = 0
    for t, w in times:
        cum += w
        if cum >= half:
            T = t
            break
    # Count meetings: pairs of right-moving and left-moving cows
    rights.sort()
    lefts.sort()
    ans = 0
    # Two-pointer via binary search
    for xi in rights:
        j = bisect.bisect_right(lefts, xi)
        k = bisect.bisect_right(lefts, xi + 2 * T) - 1
        if k >= j:
            ans += (k - j + 1)
    print(ans)

if __name__ == "__main__":
    main()
