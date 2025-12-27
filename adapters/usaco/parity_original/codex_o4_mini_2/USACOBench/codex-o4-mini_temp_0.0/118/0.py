#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    M = int(next(it))
    cows = []  # list of (P, C)
    for _ in range(N):
        P = int(next(it))
        C = int(next(it))
        cows.append((P, C))

    # Sort cows by coupon price C ascending
    cows.sort(key=lambda x: x[1])
    # Precompute prefix sums of C
    prefix_C = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_C[i] = prefix_C[i - 1] + cows[i - 1][1]

    def can_buy(x):
        # Check if we can buy x cows within budget M
        if x == 0:
            return True
        # sum of C for x cheapest coupon costs
        total = prefix_C[x]
        # if more cows than coupons, add additional costs
        extra = x - K
        if extra > 0:
            # compute deltas for those x cows
            deltas = [cows[i][0] - cows[i][1] for i in range(x)]
            # sort deltas ascending
            deltas.sort()
            # pay full price for extra cows with smallest savings
            total += sum(deltas[:extra])
        return total <= M

    # binary search maximum x
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
