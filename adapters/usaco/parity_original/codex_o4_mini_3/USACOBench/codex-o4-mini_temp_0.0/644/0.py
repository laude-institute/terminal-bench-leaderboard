#!/usr/bin/env python3
"""
Check connectivity after successive barn closures.
"""
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    # Build adjacency list
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    # Closure order
    closings = [int(input()) for _ in range(N)]

    # Union-find setup
    parent = list(range(N+1))
    size = [1] * (N+1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    # Track open barns and component count
    open_barn = [False] * (N+1)
    comp_count = 0
    status = []

    # Add barns in reverse closing order
    for x in reversed(closings):
        open_barn[x] = True
        comp_count += 1
        # Union with open neighbors
        for y in adj[x]:
            if open_barn[y] and union(x, y):
                comp_count -= 1
        # Connected if single component
        status.append("YES" if comp_count == 1 else "NO")

    # Reverse to match original closure steps
    status.reverse()

    # Output first N connectivity statuses
    out = sys.stdout
    for ans in status:
        out.write(ans + "\n")

if __name__ == "__main__":
    main()
