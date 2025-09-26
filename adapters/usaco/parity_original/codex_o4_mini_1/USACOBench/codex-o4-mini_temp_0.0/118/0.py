#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    line = data.readline().split()
    if not line:
        return
    N, K, M = map(int, line)
    cows = []  # list of (C, diff)
    for _ in range(N):
        P, C = map(int, data.readline().split())
        cows.append((C, P - C))
    # Sort by coupon price C ascending
    cows.sort(key=lambda x: x[0])
    # Prefix sums of C
    prefixC = [0] * (N + 1)
    for i in range(N):
        prefixC[i+1] = prefixC[i] + cows[i][0]

    def can_buy(x):
        if x == 0:
            return True
        # sum of smallest x C_i
        sumC = prefixC[x]
        # need to pay full price for x-K cows: penalty diffs
        t = x - K
        sum_penalty = 0
        if t > 0:
            # collect diffs of first x cows
            diffs = [cows[i][1] for i in range(x)]
            diffs.sort()
            # sum smallest t diffs
            sum_penalty = sum(diffs[:t])
        return (sumC + sum_penalty) <= M

    # binary search max x
    lo, hi = 0, N
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_buy(mid):
            lo = mid
        else:
            hi = mid - 1
    print(lo)

if __name__ == '__main__':
    main()
