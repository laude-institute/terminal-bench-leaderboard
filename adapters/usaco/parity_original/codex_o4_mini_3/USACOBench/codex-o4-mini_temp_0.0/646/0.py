#!/usr/bin/env python3
import sys

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    close = [int(input()) for _ in range(N)]
    order = close[::-1]
    parent = list(range(N+1))
    size = [1] * (N+1)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u = find(u)
        v = find(v)
        if u == v:
            return False
        if size[u] < size[v]:
            u, v = v, u
        parent[v] = u
        size[u] += size[v]
        return True

    open_node = [False] * (N+1)
    comps = 0
    ans = []
    for node in order:
        open_node[node] = True
        comps += 1
        for nei in adj[node]:
            if open_node[nei] and union(node, nei):
                comps -= 1
        ans.append(comps == 1)

    out = []
    for res in reversed(ans):
        out.append("YES\n" if res else "NO\n")
    sys.stdout.write(''.join(out))

if __name__ == '__main__':
    main()
