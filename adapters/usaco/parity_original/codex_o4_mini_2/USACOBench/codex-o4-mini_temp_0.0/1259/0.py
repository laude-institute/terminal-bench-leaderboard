#!/usr/bin/env python3
import sys

def main():
    import sys
    input = sys.stdin.readline
    # Read input
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    deg = [0] * N
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1

    # Core decomposition to compute coreness of each node
    max_deg = max(deg)
    buckets = [[] for _ in range(max_deg + 1)]
    for i, d in enumerate(deg):
        buckets[d].append(i)
    coreness = [0] * N
    cur_deg = deg[:]  # mutable copy of degrees
    bd = 0
    for _ in range(N):
        # find next non-empty bucket
        while bd <= max_deg and not buckets[bd]:
            bd += 1
        u = buckets[bd].pop()
        coreness[u] = bd
        # remove u and decrease neighbors' degrees
        for v in adj[u]:
            if cur_deg[v] > 0:
                old = cur_deg[v]
                cur_deg[v] -= 1
                buckets[old - 1].append(v)
        cur_deg[u] = 0

    # Prepare nodes sorted by decreasing coreness
    nodes = list(range(N))
    nodes.sort(key=lambda x: coreness[x], reverse=True)

    # DSU for tracking connected components among active nodes
    parent = list(range(N))
    size = [1] * N

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u = find(u); v = find(v)
        if u == v:
            return 0
        if size[u] < size[v]:
            u, v = v, u
        parent[v] = u
        size[u] += size[v]
        return size[u]

    active = [False] * N
    ans = 0
    max_comp = 0
    i = 0
    # Activate nodes by descending coreness and update answer
    while i < N:
        d = coreness[nodes[i]]
        j = i
        while j < N and coreness[nodes[j]] == d:
            u = nodes[j]
            active[u] = True
            # union with already active neighbors
            for v in adj[u]:
                if active[v]:
                    new_size = union(u, v)
                    if new_size > max_comp:
                        max_comp = new_size
            # standalone node check
            ru = find(u)
            if size[ru] > max_comp:
                max_comp = size[ru]
            j += 1
        # update maximum strength
        ans = max(ans, d * max_comp)
        i = j

    print(ans)

if __name__ == '__main__':
    main()
