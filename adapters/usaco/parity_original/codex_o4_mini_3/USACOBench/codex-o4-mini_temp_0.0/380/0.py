#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    M, N = map(int, input().split())
    elev = [list(map(int, input().split())) for _ in range(M)]
    way = [list(map(int, input().split())) for _ in range(M)]
    # Count total waypoints
    total_wp = sum(sum(row) for row in way)
    # If 0 or 1 waypoint, difficulty is 0
    if total_wp <= 1:
        print(0)
        return

    # Disjoint-set union (DSU) with waypoint counts
    n = M * N
    parent = list(range(n))
    rank = [0] * n
    wp_count = [0] * n
    # Initialize waypoint counts
    for r in range(M):
        for c in range(N):
            if way[r][c] == 1:
                wp_count[r * N + c] = 1

    def find(u):
        # Path compression
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        ru = find(u)
        rv = find(v)
        if ru == rv:
            return ru
        # Union by rank
        if rank[ru] < rank[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        if rank[ru] == rank[rv]:
            rank[ru] += 1
        wp_count[ru] += wp_count[rv]
        return ru

    # Build all edges between adjacent cells
    edges = []  # list of (diff, u, v)
    for r in range(M):
        for c in range(N):
            u = r * N + c
            if r + 1 < M:
                v = (r + 1) * N + c
                d = abs(elev[r][c] - elev[r+1][c])
                edges.append((d, u, v))
            if c + 1 < N:
                v = r * N + (c + 1)
                d = abs(elev[r][c] - elev[r][c+1])
                edges.append((d, u, v))

    # Sort edges by difficulty
    edges.sort(key=lambda x: x[0])

    # Kruskal-like union until all waypoints connected
    for diff, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            root = union(ru, rv)
            if wp_count[root] == total_wp:
                print(diff)
                return

if __name__ == '__main__':
    main()
