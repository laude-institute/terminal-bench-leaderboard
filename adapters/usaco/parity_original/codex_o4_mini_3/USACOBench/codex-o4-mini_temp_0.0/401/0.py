#!/usr/bin/env python3
"""
Solution to the Cow Decathlon problem.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    B = int(next(it))
    # bonuses_by_k[k] = list of (P, A) for bonuses at k events
    bonuses_by_k = [[] for _ in range(N+1)]
    for _ in range(B):
        k = int(next(it))
        P = int(next(it))
        A = int(next(it))
        bonuses_by_k[k].append((P, A))
    # skills[j][i]: cow j's skill in event i
    skills = [[0]*N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            skills[j][i] = int(next(it))
    size = 1 << N
    # dp[mask]: max score for assignment mask (bits are assigned cows)
    dp = [-10**18] * size
    dp[0] = 0
    # precompute popcounts
    pcounts = [0] * size
    for m in range(1, size):
        pcounts[m] = pcounts[m >> 1] + (m & 1)
    # DP over masks
    for mask in range(size):
        e = pcounts[mask]
        if e >= N:
            continue
        cur = dp[mask]
        # skip unreachable states
        if cur < -10**17:
            continue
        # assign next event e to an unassigned cow j
        for j in range(N):
            if not (mask >> j) & 1:
                newmask = mask | (1 << j)
                score = cur + skills[j][e]
                # apply any bonuses for completing e+1 events
                for P, A in bonuses_by_k[e+1]:
                    if score >= P:
                        score += A
                if score > dp[newmask]:
                    dp[newmask] = score
    # result is full mask
    print(dp[size - 1])

if __name__ == "__main__":
    main()
