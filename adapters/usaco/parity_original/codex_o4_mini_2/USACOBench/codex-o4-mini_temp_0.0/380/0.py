#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    M = int(next(it))
    N = int(next(it))
    grid = [[int(next(it)) for _ in range(N)] for _ in range(M)]
    way = [[int(next(it)) for _ in range(N)] for _ in range(M)]
    total_wp = sum(sum(row) for row in way)
    # If 0 or 1 waypoint, difficulty is 0
    if total_wp <= 1:
        print(0)
        return
    # Build edges between adjacent cells
    edges = []  # (weight, u, v)
    for i in range(M):
        for j in range(N):
            u = i * N + j
            if j + 1 < N:
                v = u + 1
                w = abs(grid[i][j] - grid[i][j+1])
                edges.append((w, u, v))
            if i + 1 < M:
                v = (i+1) * N + j
                w = abs(grid[i][j] - grid[i+1][j])
                edges.append((w, u, v))
    # Sort edges by weight
    edges.sort(key=lambda x: x[0])
    # Union-find setup
    parent = list(range(M * N))
    rank = [0] * (M * N)
    wp_count = [0] * (M * N)
    # Initialize waypoint counts
    for i in range(M):
        for j in range(N):
            if way[i][j] == 1:
                wp_count[i * N + j] = 1

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return rx
        # union by rank
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        # merge waypoint counts
        wp_count[rx] += wp_count[ry]
        return rx

    # Kruskal: add edges until all waypoints are connected
    for w, u, v in edges:
        r = union(u, v)
        if wp_count[r] == total_wp:
            print(w)
            return

if __name__ == '__main__':
    main()
