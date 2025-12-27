#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline

    # Read input
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Sort cows and stalls
    a.sort()
    b.sort()

    # Precompute valid placements: valid[i][j] is True if cow i can go in stall j
    valid = [[a[i] <= b[j] for j in range(N)] for i in range(N)]

    # DP over subsets of cows: dp[mask] = ways to assign cows in mask to first k stalls
    M = 1 << N
    dp = [0] * M
    dp[0] = 1

    for mask in range(1, M):
        k = mask.bit_count()  # number of cows assigned, corresponds to stall index k-1
        total = 0
        # Try placing one of the cows in the k-th stall
        for i in range(N):
            if (mask >> i) & 1 and valid[i][k-1]:
                total += dp[mask ^ (1 << i)]
        dp[mask] = total

    # Full assignment mask has all cows placed
    print(dp[M - 1])

if __name__ == "__main__":
    main()
