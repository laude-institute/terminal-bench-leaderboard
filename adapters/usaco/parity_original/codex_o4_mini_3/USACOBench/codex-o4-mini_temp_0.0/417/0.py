#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    # Read number of fields N and number of breeds B
    N = int(next(it)); B = int(next(it))
    # Read moo volumes for each breed
    V = [int(next(it)) for _ in range(B)]
    # Read recorded volumes for each field
    rec = [int(next(it)) for _ in range(N)]

    # Compute required volume from cows in each field after wind contribution
    needed = [0] * N
    prev = 0
    for i in range(N):
        carried = prev - 1 if prev > 0 else 0
        needed[i] = rec[i] - carried
        if needed[i] < 0:
            print(-1)
            return
        prev = rec[i]

    # Prepare unbounded knapsack DP up to maximum needed volume
    max_needed = max(needed)
    INF = max_needed + 1
    dp = [INF] * (max_needed + 1)
    dp[0] = 0
    for v in range(1, max_needed + 1):
        best = INF
        for coin in V:
            if v >= coin:
                c = dp[v - coin] + 1
                if c < best:
                    best = c
        dp[v] = best

    # Sum minimal cows for each field
    total = 0
    for x in needed:
        if dp[x] > max_needed:
            print(-1)
            return
        total += dp[x]

    print(total)

if __name__ == '__main__':
    main()
