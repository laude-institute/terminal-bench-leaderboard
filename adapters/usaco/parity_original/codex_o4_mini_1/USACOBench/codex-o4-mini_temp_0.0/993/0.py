#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m_edges = int(next(it))
    C = int(next(it))
    m_vals = [0] + [int(next(it)) for _ in range(n)]
    edges = []
    for _ in range(m_edges):
        u = int(next(it)); v = int(next(it))
        edges.append((u, v))

    max_m = max(m_vals)
    # bound on trips: positive net only if t*max_m - C*t^2 > 0 => t <= max_m//C
    t_limit = max_m // C if C > 0 else 0
    if t_limit <= 0:
        print(0)
        return

    INF = 10**18
    dp_prev = [-INF] * (n + 1)
    dp_prev[1] = 0
    dp_curr = [-INF] * (n + 1)

    ans = 0
    for t in range(1, t_limit + 1):
        # reset current dp
        for i in range(1, n + 1):
            dp_curr[i] = -INF
        # transition
        for u, v in edges:
            val = dp_prev[u] + m_vals[v]
            if val > dp_curr[v]:
                dp_curr[v] = val
        # consider return to city 1
        if dp_curr[1] > -INF:
            net = dp_curr[1] - C * t * t
            if net > ans:
                ans = net
        # swap dp arrays
        dp_prev, dp_curr = dp_curr, dp_prev

    print(ans)

if __name__ == "__main__":
    main()
