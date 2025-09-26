#!/usr/bin/env python3
"""
Solution for equalizing cow hunger levels via adjacent feeding operations.
"""

import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        h = list(map(int, input().split()))
        # Single cow already equal
        if N == 1:
            print(0)
            continue
        # Compute prefix alternating sums pref[1..N-1]
        pref = [0] * (N + 1)
        pref[1] = h[0]
        for i in range(2, N):
            pref[i] = h[i-1] - pref[i-1]
        # Even-indexed prefix sums must be non-negative
        if any(pref[i] < 0 for i in range(2, N, 2)):
            print(-1)
            continue
        # Odd N: unique final hunger H
        if N % 2 == 1:
            H = h[-1] - pref[N-1]
            if H < 0:
                print(-1)
                continue
            total_ops = 0
            valid = True
            for i in range(1, N):
                if i % 2 == 1:
                    if H > pref[i]:
                        valid = False
                        break
                    total_ops += pref[i] - H
                else:
                    total_ops += pref[i]
            print(2 * total_ops if valid else -1)
        else:
            # Even N: check consistency and choose max H
            if pref[N-1] != h[-1]:
                print(-1)
                continue
            # Maximize H within [0, min odd pref]
            R = min(pref[i] for i in range(1, N, 2))
            if R < 0:
                print(-1)
                continue
            # Total prefix sum S = sum(pref[1..N-1])
            S = sum(pref[i] for i in range(1, N))
            m = N // 2
            total_ops = S - m * R
            print(2 * total_ops)

if __name__ == "__main__":
    main()
