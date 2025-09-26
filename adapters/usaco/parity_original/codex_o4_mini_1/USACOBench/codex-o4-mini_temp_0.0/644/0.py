#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    close_order = [int(input()) for _ in range(N)]

    # DSU implementation
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

    active = [False] * (N+1)
    comp_count = 0
    ans_add = [False] * (N+1)

    # Add barns back in reverse closing order
    for i in range(N):
        x = close_order[N-1-i]
        active[x] = True
        comp_count += 1
        # union with active neighbors
        for y in adj[x]:
            if active[y] and union(x, y):
                comp_count -= 1
        # connected if only one component among active barns
        ans_add[i+1] = (comp_count == 1)

    # Output answers: initial, after each of first N-1 closures
    # ans_add[N] is initial, ans_add[1] is after N-1 closures
    out = []
    for k in range(N, 0, -1):
        # skip the final state when no barns remain
        out.append("YES" if ans_add[k] else "NO")
    # Print only first N lines (ignore state after all removed)
    # That is exactly N lines already
    sys.stdout.write("\n".join(out[:N]))

if __name__ == '__main__':
    main()
