#!/usr/bin/env python3
"""
Count ways to assign N cows to N stalls with height constraints.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    # Sort cow heights and stall limits for DP ordering
    a = sorted(int(x) for x in data[1:1+N])
    b = sorted(int(x) for x in data[1+N:1+2*N])
    size = 1 << N
    # dp[mask] = number of ways to assign cows in 'mask' to first popcount(mask) stalls
    dp = [0] * size
    dp[0] = 1
    # Precompute popcounts for all masks
    pc = [0] * size
    for mask in range(1, size):
        pc[mask] = pc[mask >> 1] + (mask & 1)

    # Build DP
    for mask in range(size):
        k = pc[mask]
        if k >= N:
            continue
        limit = b[k]
        # Try assigning each unused cow j to stall k
        for j in range(N):
            if not (mask & (1 << j)) and a[j] <= limit:
                dp[mask | (1 << j)] += dp[mask]

    # Result: all cows assigned
    print(dp[size - 1])

if __name__ == "__main__":
    main()
