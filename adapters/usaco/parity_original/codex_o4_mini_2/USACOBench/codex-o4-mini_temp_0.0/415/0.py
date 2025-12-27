#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, C = map(int, input().split())
    pts = [tuple(map(int, input().split())) for _ in range(N)]
    # Prim's algorithm with threshold C
    visited = [False] * N
    dist = [float('inf')] * N
    visited[0] = True
    # Initialize distances from node 0
    for i in range(1, N):
        dx = pts[0][0] - pts[i][0]
        dy = pts[0][1] - pts[i][1]
        w = dx * dx + dy * dy
        if w >= C:
            dist[i] = w
    total = 0
    for _ in range(N - 1):
        # pick the next field with minimum valid distance
        u = -1
        min_d = float('inf')
        for i in range(N):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        # if no reachable field remains, impossible
        if u == -1 or min_d == float('inf'):
            print(-1)
            return
        visited[u] = True
        total += min_d
        # update distances using the newly added field
        ux, uy = pts[u]
        for v in range(N):
            if not visited[v]:
                dx = ux - pts[v][0]
                dy = uy - pts[v][1]
                w = dx * dx + dy * dy
                if w >= C and w < dist[v]:
                    dist[v] = w
    print(total)

if __name__ == '__main__':
    main()
