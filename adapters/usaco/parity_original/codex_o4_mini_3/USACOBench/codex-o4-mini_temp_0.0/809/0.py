#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    # Day 1 must be a breakout
    if A[0] not in (-1, 0):
        print(-1)
        return

    # dp[c] = (min_breakouts, max_breakouts) ending with counter c on current day
    dp = {0: (1, 1)}
    # Process days 2..n
    for i in range(1, n):
        a = A[i]
        dp2 = {}
        for c_prev, (minb, maxb) in dp.items():
            # Option 1: breakout today -> counter = 0
            if a in (-1, 0):
                c = 0
                mn, mx = minb + 1, maxb + 1
                if c in dp2:
                    old_mn, old_mx = dp2[c]
                    dp2[c] = (min(old_mn, mn), max(old_mx, mx))
                else:
                    dp2[c] = (mn, mx)
            # Option 2: no breakout -> counter increments
            c_new = c_prev + 1
            if a in (-1, c_new):
                mn, mx = minb, maxb
                if c_new in dp2:
                    old_mn, old_mx = dp2[c_new]
                    dp2[c_new] = (min(old_mn, mn), max(old_mx, mx))
                else:
                    dp2[c_new] = (mn, mx)
        dp = dp2
        if not dp:
            print(-1)
            return

    # Collect overall min and max breakouts
    overall_min = min(x[0] for x in dp.values())
    overall_max = max(x[1] for x in dp.values())
    print(overall_min, overall_max)


if __name__ == '__main__':
    main()
