#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    C = int(next(it))
    m = [0] * (N + 1)
    for i in range(1, N + 1):
        m[i] = int(next(it))
    # build incoming edges list
    incoming = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(next(it)); v = int(next(it))
        incoming[v].append(u)

    # DP over days: dp_prev[u] = max reward to be at u after t-1 days
    # Initialize
    NEG_INF = -10**18
    dp_prev = [NEG_INF] * (N + 1)
    dp_prev[1] = 0  # start at city 1 at day 0
    best = 0
    # bound on days
    T_MAX = 2000
    for t in range(1, T_MAX + 1):
        dp_curr = [NEG_INF] * (N + 1)
        for v in range(1, N + 1):
            # compute dp_curr[v]
            best_prev = NEG_INF
            for u in incoming[v]:
                val = dp_prev[u]
                if val > best_prev:
                    best_prev = val
            if best_prev != NEG_INF:
                dp_curr[v] = best_prev + m[v]
        # if can return to city 1
        if dp_curr[1] > NEG_INF:
            profit = dp_curr[1] - C * t * t
            if profit > best:
                best = profit
        dp_prev = dp_curr
    print(best)

if __name__ == '__main__':
    main()
