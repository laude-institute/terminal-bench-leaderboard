#!/usr/bin/env python3
"""
Solution to the barn cow meeting problem.
"""
import sys
import bisect

def main():
    data = sys.stdin
    N, L = map(int, data.readline().split())
    total_weight = 0
    stops = []
    rights = []
    lefts = []
    # Read cows and compute stop times
    for _ in range(N):
        w, x, d = map(int, data.readline().split())
        total_weight += w
        if d == -1:
            t = x
            lefts.append(x)
        else:
            t = L - x
            rights.append(x)
        stops.append((t, w))
    # Determine time T when stopped weight >= half
    stops.sort()
    target = (total_weight + 1) // 2
    cum = 0
    T = 0
    for t, w in stops:
        cum += w
        if cum >= target:
            T = t
            break
    # Count meetings: pairs (i,j) with i moving right, j moving left
    # that meet by time T: (xj - xi)/2 <= T -> xj <= xi + 2*T
    lefts.sort()
    meetings = 0
    for x in rights:
        # indices in lefts where xj > x and xj <= x + 2*T
        lo = bisect.bisect_right(lefts, x)
        hi = bisect.bisect_right(lefts, x + 2 * T) - 1
        if hi >= lo:
            meetings += hi - lo + 1
    print(meetings)

if __name__ == "__main__":
    main()
