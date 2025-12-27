#!/usr/bin/env python3
"""
Problem: Given a complete directed weighted graph with N nodes and N^2 edges (including self-loops),
we remove edges one by one and after each removal need to compute the shortest path
from node 1 to node N using exactly K edges (allowing repeated vertices and edges).
If no such path exists, output -1.
"""

import sys
def main():
    input = sys.stdin.readline
    INF = 10**30
    # Read N and K
    N, K = map(int, input().split())
    # Read weight matrix
    W = [None] + [list(map(int, input().split())) for _ in range(N)]
    # Prepare removals list
    removals = [tuple(map(int, input().split())) for _ in range(N*N)]
    # Process removals one by one
    for u, v in removals:
        # Remove edge by setting its weight to INF
        W[u][v] = INF
        # DP for exactly K steps
        dp_prev = [INF] * (N + 1)
        dp_prev[1] = 0
        for _ in range(K):
            dp_cur = [INF] * (N + 1)
            for x in range(1, N + 1):
                cost_x = dp_prev[x]
                if cost_x >= INF:
                    continue
                row = W[x]
                # Relax edges from x
                for y in range(1, N + 1):
                    w_xy = row[y-1]
                    if w_xy < INF:
                        new_cost = cost_x + w_xy
                        if new_cost < dp_cur[y]:
                            dp_cur[y] = new_cost
            dp_prev = dp_cur
        # Output answer for node N
        ans = dp_prev[N]
        print(ans if ans < INF else -1)

if __name__ == '__main__':
    main()
