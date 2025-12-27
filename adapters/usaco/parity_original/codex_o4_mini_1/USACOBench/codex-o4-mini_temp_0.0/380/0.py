#!/usr/bin/env python3
"""
Solution to the Cross Country Skiing problem (ccski).
Compute the minimum difficulty D such that all waypoints are connected
in the grid when moves are allowed between adjacent cells with
elevation difference <= D.
"""
import sys

def main():
    input = sys.stdin.readline
    M, N = map(int, input().split())
    elev = [list(map(int, input().split())) for _ in range(M)]
    way = [list(map(int, input().split())) for _ in range(M)]
    # Flatten index
    def idx(i, j): return i * N + j

    # Count total waypoints
    total_way = sum(sum(row) for row in way)
    if total_way <= 1:
        print(0)
        return

    # Union-Find with waypoint counts
    parent = list(range(M * N))
    size = [1] * (M * N)
    wp_count = [0] * (M * N)
    for i in range(M):
        for j in range(N):
            if way[i][j] == 1:
                wp_count[idx(i, j)] = 1

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return rx
        # union by size
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        size[rx] += size[ry]
        wp_count[rx] += wp_count[ry]
        return rx

    # Build edges: (weight, u, v)
    edges = []
    for i in range(M):
        for j in range(N):
            u = idx(i, j)
            if j + 1 < N:
                v = idx(i, j+1)
                w = abs(elev[i][j] - elev[i][j+1])
                edges.append((w, u, v))
            if i + 1 < M:
                v = idx(i+1, j)
                w = abs(elev[i][j] - elev[i+1][j])
                edges.append((w, u, v))

    edges.sort(key=lambda x: x[0])

    # Kruskal until all waypoints connected
    for w, u, v in edges:
        r = union(u, v)
        if wp_count[r] == total_way:
            print(w)
            return

if __name__ == '__main__':
    main()
