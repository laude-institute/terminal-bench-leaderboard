#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, B = map(int, input().split())
    bonuses = {}
    for _ in range(B):
        K, P, A = map(int, input().split())
        bonuses.setdefault(K, []).append((P, A))
    # Sort bonuses for each K by threshold
    for k in bonuses:
        bonuses[k].sort()
    # Read skill matrix: skills[i][j] = skill of cow i in event j
    skills = [list(map(int, input().split())) for _ in range(N)]

    # dp[mask]: max score after assigning first popcount(mask) events
    size = 1 << N
    dp = [-10**18] * size
    dp[0] = 0
    for mask in range(1, size):
        k = mask.bit_count()  # number of cows assigned = event index
        best = -10**18
        # assign last event k to cow i
        for i in range(N):
            if mask & (1 << i):
                prev = mask ^ (1 << i)
                score = dp[prev] + skills[i][k-1]
                if score > best:
                    best = score
        # apply bonuses for completing k events
        if k in bonuses:
            # add bonuses in order, possibly cascading
            for P, A in bonuses[k]:
                if best >= P:
                    best += A
                else:
                    break
        dp[mask] = best
    # full mask: all cows assigned
    print(dp[size-1])

if __name__ == '__main__':
    main()
