#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m_edges = int(next(it))
    C = int(next(it))
    m_vals = [int(next(it)) for _ in range(n)]
    # read edges, zero-indexed
    edges = []
    for _ in range(m_edges):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
    # maximum steps to consider
    # max reward per step <= max(m_vals) <= 1000
    # profit = R*t - C*t^2 > 0 => t < max(m_vals)/C
    max_m = max(m_vals)
    # ensure at least consider t=1
    t_max = max_m // C if C > 0 else n
    if t_max <= 0:
        print(0)
        return
    # dp arrays: prev[t-1], curr[t]
    neg_inf = -10**30
    prev = [neg_inf] * n
    prev[0] = 0
    ans = 0
    # iterate over path lengths
    for t in range(1, t_max + 1):
        curr = [neg_inf] * n
        for u, v in edges:
            if prev[u] != neg_inf:
                val = prev[u] + m_vals[v]
                if val > curr[v]:
                    curr[v] = val
        if curr[0] != neg_inf:
            profit = curr[0] - C * t * t
            if profit > ans:
                ans = profit
        prev = curr
    print(ans)

if __name__ == "__main__":
    main()
