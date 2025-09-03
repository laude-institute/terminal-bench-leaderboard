#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    a = list(map(int, data[1:]))

    INF = 10**9
    # dp_prev_min[c]: minimum breakouts up to previous day with counter=c
    # dp_prev_max[c]: maximum breakouts up to previous day with counter=c
    dp_prev_min = [INF] * (N + 1)
    dp_prev_max = [-INF] * (N + 1)
    # Day 1 must be a breakout, counter=0
    if a[0] not in (-1, 0):
        print(-1)
        return
    dp_prev_min[0] = dp_prev_max[0] = 1

    # Process days 2..N
    for i in range(1, N):
        dp_cur_min = [INF] * (N + 1)
        dp_cur_max = [-INF] * (N + 1)
        ai = a[i]
        for prev_c in range(N + 1):
            if dp_prev_min[prev_c] == INF:
                continue
            # Option 1: no breakout, counter increments
            c = prev_c + 1
            if c <= N and (ai == -1 or ai == c):
                dp_cur_min[c] = min(dp_cur_min[c], dp_prev_min[prev_c])
                dp_cur_max[c] = max(dp_cur_max[c], dp_prev_max[prev_c])
            # Option 2: breakout, counter resets to 0
            if ai in (-1, 0):
                dp_cur_min[0] = min(dp_cur_min[0], dp_prev_min[prev_c] + 1)
                dp_cur_max[0] = max(dp_cur_max[0], dp_prev_max[prev_c] + 1)
        dp_prev_min, dp_prev_max = dp_cur_min, dp_cur_max

    # Determine final answer
    mn = min(dp_prev_min)
    mx = max(dp_prev_max)
    if mn == INF:
        print(-1)
    else:
        print(mn, mx)

if __name__ == "__main__":
    main()
