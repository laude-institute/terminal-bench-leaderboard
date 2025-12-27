#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, C = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    # Prim's algorithm for MST with edge cost threshold
    INF = 10**30
    visited = [False] * N
    dist = [INF] * N
    dist[0] = 0
    total_cost = 0

    for _ in range(N):
        # pick unvisited node with minimum dist
        u = -1
        min_d = INF
        for i in range(N):
            if not visited[i] and dist[i] < min_d:
                u = i
                min_d = dist[i]
        # if no reachable node remains, impossible to connect all
        if u == -1 or min_d == INF:
            print(-1)
            return

        visited[u] = True
        total_cost += min_d

        # update distances for remaining nodes
        ux, uy = points[u]
        for v in range(N):
            if not visited[v]:
                vx, vy = points[v]
                d = (ux - vx) * (ux - vx) + (uy - vy) * (uy - vy)
                if d >= C and d < dist[v]:
                    dist[v] = d

    print(total_cost)

if __name__ == '__main__':
    main()
