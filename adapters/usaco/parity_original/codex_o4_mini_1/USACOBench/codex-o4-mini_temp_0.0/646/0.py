#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    # build adjacency list
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    # read closing order
    close_order = [int(input()) for _ in range(N)]

    # DSU setup
    parent = list(range(N+1))
    size = [1] * (N+1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    # track open barns and component count
    open_barn = [False] * (N+1)
    comp_count = 0
    ans_rev = []

    # process openings in reverse of closings
    for barn in reversed(close_order):
        comp_count += 1
        open_barn[barn] = True
        # connect to already open neighbors
        for nb in adj[barn]:
            if open_barn[nb] and union(barn, nb):
                comp_count -= 1
        # connected if exactly one component
        ans_rev.append("YES" if comp_count == 1 else "NO")

    # reverse answers to correspond to initial and subsequent closures
    ans = list(reversed(ans_rev))
    # output first N answers (initial + after N-1 closings)
    print("\n".join(ans[:N]))

if __name__ == "__main__":
    main()
