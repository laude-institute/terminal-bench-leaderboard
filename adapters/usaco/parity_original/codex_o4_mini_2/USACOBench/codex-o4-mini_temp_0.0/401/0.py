#!/usr/bin/env python3
"""
Solution to the Cow Decathlon problem using bitmask DP.
Each DP state represents assigned cows to the first k events.
Bonuses applied when cumulative score meets thresholds.
"""
import sys

def main():
    input = sys.stdin.readline
    # Read N cows/events and B bonuses
    N, B = map(int, input().split())
    # Organize bonuses by event count K
    bonuses_by_k = [[] for _ in range(N + 1)]
    for _ in range(B):
        K, P, A = map(int, input().split())
        bonuses_by_k[K].append((P, A))
    # Read skill matrix: skill[j][e] = cow j's score at event e
    skills = [list(map(int, input().split())) for _ in range(N)]

    M = 1 << N
    # Initialize DP array: dp[mask] = max score for assigned cows in mask
    NEG_INF = -10**18
    dp = [NEG_INF] * M
    dp[0] = 0

    # Iterate over all subsets of cows
    for mask in range(M):
        # Number of events already assigned
        k = mask.bit_count()
        # Apply any bonuses for k events
        for P, A in bonuses_by_k[k]:
            if dp[mask] >= P:
                dp[mask] += A
        # Assign one more cow to event k (0-indexed)
        for j in range(N):
            if not (mask & (1 << j)):
                new_mask = mask | (1 << j)
                score = dp[mask] + skills[j][k]
                if score > dp[new_mask]:
                    dp[new_mask] = score

    # Full assignment mask
    print(dp[M - 1])

if __name__ == '__main__':
    main()
