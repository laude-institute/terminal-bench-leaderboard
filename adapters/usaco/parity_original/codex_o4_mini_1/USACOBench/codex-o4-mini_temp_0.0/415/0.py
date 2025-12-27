#!/usr/bin/env python3
"""
Solution for 'Watering the Fields':
Compute MST using Prim's algorithm, only allowing edges with cost >= C.
"""
import sys

def main():
    input = sys.stdin.readline
    N, C = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    INF = float('inf')
    min_cost = [INF] * N
    visited = [False] * N

    # Start from node 0
    min_cost[0] = 0
    total_cost = 0

    for _ in range(N):
        # Find unvisited node with smallest cost
        u = -1
        u_cost = INF
        for i in range(N):
            if not visited[i] and min_cost[i] < u_cost:
                u = i
                u_cost = min_cost[i]
        # If no reachable node, impossible
        if u == -1 or u_cost == INF:
            print(-1)
            return

        visited[u] = True
        total_cost += u_cost

        # Update costs for remaining nodes
        ux, uy = points[u]
        for v in range(N):
            if not visited[v]:
                vx, vy = points[v]
                dx = ux - vx
                dy = uy - vy
                dist = dx*dx + dy*dy
                if dist >= C and dist < min_cost[v]:
                    min_cost[v] = dist

    print(total_cost)

if __name__ == '__main__':
    main()
