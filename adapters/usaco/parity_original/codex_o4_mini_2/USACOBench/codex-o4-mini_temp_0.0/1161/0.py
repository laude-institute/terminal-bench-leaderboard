#!/usr/bin/env python3
"""
Solution for weighted maximal matchings on number line cows.
T=1: minimum sum of weights of unpaired cows (minimal weight independent dominating set).
T=2: maximum sum of weights of unpaired cows (maximum weight independent set).
"""
import sys

def main():
    data = sys.stdin.read().split()
    T, N, K = map(int, data[:3])
    xs = [0]*N
    ws = [0]*N
    idx = 3
    for i in range(N):
        xs[i] = int(data[idx]); ws[i] = int(data[idx+1]); idx += 2

    # Precompute prev index: for each i, find last j < i with xs[i] - xs[j] > K
    prev = [ -1 ] * N
    j = 0
    for i in range(N):
        while j < i and xs[i] - xs[j] > K:
            j += 1
        prev[i] = j - 1

    # DP for T=2: maximum sum of weights of unpaired (free) cows
    if T == 2:
        dp = [0] * (N+1)
        for i in range(1, N+1):
            # leave i-1 free
            take = dp[i-1] + ws[i-1]
            # skip i-1 (i-1 not free)
            skip = dp[prev[i-1]+1] if prev[i-1] >= 0 else 0
            dp[i] = max(take, skip)
        print(dp[N])
        return

    # T==1: minimal weights of unpaired (free) cows - need minimal weight independent dominating set
    # TODO: implement weighted independent dominating set on unit interval graph
    # Placeholder greedy: process each connected block
    res = 0
    i = 0
    while i < N:
        # find block where consecutive xs within K
        j = i
        while j+1 < N and xs[j+1] - xs[j] <= K:
            j += 1
        # block [i..j]
        # if block size odd: pick minimal weight cow at minimal undominated index
        block = ws[i:j+1]
        if (j - i + 1) % 2 == 1:
            res += min(block)
        i = j + 1
    print(res)

if __name__ == '__main__':
    main()
