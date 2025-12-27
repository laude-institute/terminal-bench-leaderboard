#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # read log entries, 1-based
    a = [0] + [int(next(it)) for _ in range(n)]

    # costFirst[i]: mismatches with single breakout at day 1 (expected t-1)
    costFirst = [0] * (n + 1)
    for i in range(1, n + 1):
        # expected at day i is i-1
        costFirst[i] = costFirst[i-1] + (1 if a[i] != i-1 else 0)

    # costBetween[j][i]: cost for days j+1..i, given breakout at j (expected[t] = t-j)
    costBetween = [[0] * (n + 1) for _ in range(n + 1)]
    for j in range(1, n + 1):
        s = 0
        for i in range(j + 1, n + 1):
            # expected at day i is i-j
            if a[i] != i - j:
                s += 1
            costBetween[j][i] = s

    # dp[i][k]: min mismatches in first i days with exactly k breakouts and breakout at day i
    INF = 10**9
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    # base k=1: breakout at day1 only
    for i in range(1, n + 1):
        dp[i][1] = costFirst[i]

    # fill dp for k >= 2
    for k in range(2, n + 1):
        for i in range(k, n + 1):  # last breakout at day i
            # mismatch at day i for the breakout: expected 0
            mi = 1 if a[i] != 0 else 0
            # consider previous breakout at day j (< i)
            best = INF
            for j in range(k-1, i):
                # dp[j][k-1] + cost of no-breakout days j+1..i-1 + mismatch at i
                cost_seg = costBetween[j][i-1]
                val = dp[j][k-1] + cost_seg + mi
                if val < best:
                    best = val
            dp[i][k] = best

    # compute answers for k = 1..n
    out = []
    for k in range(1, n + 1):
        ans = INF
        for i in range(k, n + 1):
            # tail segment after last breakout at day i: days i+1..n
            tail = costBetween[i][n]
            val = dp[i][k] + tail
            if val < ans:
                ans = val
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
