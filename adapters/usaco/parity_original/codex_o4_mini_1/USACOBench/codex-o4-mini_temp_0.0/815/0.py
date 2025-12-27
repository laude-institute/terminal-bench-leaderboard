#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    a = list(map(int, data[1:]))
    INF = 10**9
    # dp[i][b][c] = min mismatches up to day i (1-based), with b breakouts, and counter = c on day i
    # dimensions: (N+1) x (N+2) x (N+2)
    dp = [[[INF] * (N+1) for _ in range(N+2)] for __ in range(N+1)]
    # Day 1 must be a breakout, counter = 0
    dp[1][1][0] = 0 if a[0] == 0 else 1
    for i in range(1, N):
        for b in range(1, i+1):
            for c in range(0, i):
                prev = dp[i][b][c]
                if prev >= INF:
                    continue
                # no breakout today
                c2 = c + 1
                cost = prev + (0 if a[i] == c2 else 1)
                if cost < dp[i+1][b][c2]:
                    dp[i+1][b][c2] = cost
                # breakout today
                cost2 = prev + (0 if a[i] == 0 else 1)
                if cost2 < dp[i+1][b+1][0]:
                    dp[i+1][b+1][0] = cost2
    # Output answers for k = 1..N
    out = []
    for k in range(1, N+1):
        best = min(dp[N][k])
        out.append(str(best))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
