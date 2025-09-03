#!/usr/bin/env python3
import sys
import threading

# Solve the simplify problem: compute MST weight and count of MSTs modulo 1e9+7
def main():
    import sys
    import itertools
    input = sys.stdin.readline
    MOD = 10**9 + 7

    # Read input
    N, M = map(int, input().split())
    edges = []  # list of (weight, u, v)
    for _ in range(M):
        a, b, w = map(int, input().split())
        edges.append((w, a-1, b-1))

    # Sort edges by weight
    edges.sort(key=lambda x: x[0])

    # Disjoint set union (union-find)
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.r = [0] * n
        def find(self, x):
            while self.p[x] != x:
                self.p[x] = self.p[self.p[x]]
                x = self.p[x]
            return x
        def union(self, x, y):
            x = self.find(x); y = self.find(y)
            if x == y:
                return False
            if self.r[x] < self.r[y]:
                x, y = y, x
            self.p[y] = x
            if self.r[x] == self.r[y]:
                self.r[x] += 1
            return True

    dsu = DSU(N)
    total_weight = 0
    total_ways = 1
    i = 0
    # Process edges in groups of equal weight
    while i < M:
        w = edges[i][0]
        j = i
        # Collect edges of this weight that connect different DSU components
        group = []  # list of (ru, rv)
        while j < M and edges[j][0] == w:
            _, u, v = edges[j]
            ru = dsu.find(u)
            rv = dsu.find(v)
            if ru != rv:
                group.append((ru, rv))
            j += 1

        # If there are candidate edges, count ways for each small component
        if group:
            # Map involved DSU components to small indices
            nodes = set()
            for u, v in group:
                nodes.add(u); nodes.add(v)
            node_list = list(nodes)
            idx = {node_list[k]: k for k in range(len(node_list))}
            # Build small graph edges
            ge = [(idx[u], idx[v]) for u, v in group]
            n_small = len(node_list)
            # Adjacency: map node to incident edge indices
            adj = [[] for _ in range(n_small)]
            for ei, (u, v) in enumerate(ge):
                adj[u].append(ei)
                adj[v].append(ei)

            visited = [False] * n_small
            # Explore each connected component in small graph
            for u in range(n_small):
                if visited[u]:
                    continue
                # BFS/DFS to collect nodes and edges in this component
                stack = [u]
                comp_nodes = set()
                comp_edges = set()
                while stack:
                    x = stack.pop()
                    if visited[x]:
                        continue
                    visited[x] = True
                    comp_nodes.add(x)
                    for ei in adj[x]:
                        comp_edges.add(ei)
                        a, b = ge[ei]
                        y = b if x == a else a
                        if not visited[y]:
                            stack.append(y)

                cn = len(comp_nodes)
                if cn <= 1:
                    # No edges needed
                    continue
                # Count spanning trees: choose cn-1 edges among comp_edges
                ce_list = list(comp_edges)
                ways = 0
                for subset in itertools.combinations(ce_list, cn-1):
                    # Check connectivity among comp_nodes
                    tmp_dsu = DSU(cn)
                    for ei in subset:
                        a, b = ge[ei]
                        tmp_dsu.union(a, b)
                    # Verify single component
                    roots = {tmp_dsu.find(x) for x in comp_nodes}
                    if len(roots) == 1:
                        ways += 1
                # Update global counts
                total_ways = (total_ways * ways) % MOD
                total_weight += w * (cn - 1)

        # Union all candidate edges in the global DSU
        for u, v in group:
            dsu.union(u, v)
        i = j

    # Output result
    print(total_weight, total_ways)

if __name__ == '__main__':
    main()
