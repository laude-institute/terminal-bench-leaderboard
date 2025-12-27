#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    # dp_min[i][d]: min breakouts up to day i with last breakout on day d
    # dp_max similarly
    INF = 10**9
    dp_min = [[INF] * (n+1) for _ in range(n+1)]
    dp_max = [[-INF] * (n+1) for _ in range(n+1)]
    # Day 1 must have breakout
    if a[0] not in (-1, 0):
        print(-1)
        return
    dp_min[1][1] = 1
    dp_max[1][1] = 1
    # Process days 2..n
    for i in range(2, n+1):
        ai = a[i-1]
        for prev in range(1, i):
            if dp_min[i-1][prev] < INF:
                # Option 1: no breakout today
                cnt = i - prev
                if ai == -1 or ai == cnt:
                    dp_min[i][prev] = min(dp_min[i][prev], dp_min[i-1][prev])
                    dp_max[i][prev] = max(dp_max[i][prev], dp_max[i-1][prev])
        # Option 2: breakout today
        if ai == -1 or ai == 0:
            for prev in range(1, i):
                if dp_min[i-1][prev] < INF:
                    dp_min[i][i] = min(dp_min[i][i], dp_min[i-1][prev] + 1)
                    dp_max[i][i] = max(dp_max[i][i], dp_max[i-1][prev] + 1)
    # Answer
    res_min = min(dp_min[n][1:])
    res_max = max(dp_max[n][1:])
    if res_min >= INF:
        print(-1)
    else:
        print(res_min, res_max)

if __name__ == '__main__':
    main()
