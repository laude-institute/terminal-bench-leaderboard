#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    # Read edges
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        # convert to 0-based index
        edges.append((w, u - 1, v - 1))
    # Read queries
    queries = []  # (threshold k, node v, original index)
    for idx in range(Q):
        k, v = map(int, input().split())
        queries.append((k, v - 1, idx))
    # Sort edges by weight descending and queries by k descending
    edges.sort(key=lambda x: x[0], reverse=True)
    queries.sort(key=lambda x: x[0], reverse=True)

    # Disjoint set union (DSU) with size tracking
    parent = list(range(N))
    size = [1] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        # union by size
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    # Process queries
    res = [0] * Q
    ei = 0  # edge index
    for k, v, qi in queries:
        # add all edges with weight >= k
        while ei < len(edges) and edges[ei][0] >= k:
            _, u1, v1 = edges[ei]
            union(u1, v1)
            ei += 1
        # result is component size minus one (exclude the node itself)
        res[qi] = size[find(v)] - 1

    # Output results in original order
    print("\n".join(map(str, res)))

if __name__ == '__main__':
    main()
