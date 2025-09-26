#!/usr/bin/env python3
"""
Solution for dynamic connectivity with node removals (reverse via DSU additions).
"""
import sys

def main():
    import sys
    input = sys.stdin.readline
    # Read number of barns and paths
    N, M = map(int, input().split())
    # Build adjacency list
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    # Read closing order
    order = [int(input()) for _ in range(N)]

    # Disjoint-set (Union-Find) with path compression and union by size
    parent = list(range(N + 1))
    size = [1] * (N + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return False
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        return True

    # Track which barns are currently opened (in reverse process)
    opened = [False] * (N + 1)
    ans = [None] * N
    components = 0

    # Process additions in reverse closing order
    for i in range(N - 1, -1, -1):
        node = order[i]
        opened[node] = True
        components += 1
        # Union with already opened neighbors
        for nei in adj[node]:
            if opened[nei] and union(node, nei):
                components -= 1
        # If exactly one component, it's fully connected
        ans[i] = "YES" if components == 1 else "NO"

    # Output answers: initial and after each closure
    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()
