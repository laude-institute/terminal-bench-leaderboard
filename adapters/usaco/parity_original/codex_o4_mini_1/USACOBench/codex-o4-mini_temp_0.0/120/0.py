#!/usr/bin/env python3
import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    K = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    C = [int(next(it)) for _ in range(n)]

    # dp_down[v][d]: sum of cows in subtree of v at distance d
    dp_down = [[0]*(K+1) for _ in range(n)]
    parent = [-1]*n
    # Post-order DFS to fill dp_down
    stack = [(0, -1, False)]
    while stack:
        v, p, visited = stack.pop()
        if not visited:
            parent[v] = p
            stack.append((v, p, True))
            for u in adj[v]:
                if u == p: continue
                stack.append((u, v, False))
        else:
            dp_down[v][0] = C[v]
            for u in adj[v]:
                if u == p: continue
                for d in range(1, K+1):
                    dp_down[v][d] += dp_down[u][d-1]

    # dp_up[v][d]: sum of cows outside subtree of v at distance d
    dp_up = [[0]*(K+1) for _ in range(n)]
    # Pre-order to fill dp_up
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if u == parent[v]: continue
            # compute dp_up for child u
            for d in range(1, K+1):
                val = dp_up[v][d-1] + dp_down[v][d-1]
                if d-2 >= 0:
                    val -= dp_down[u][d-2]
                dp_up[u][d] = val
            stack.append(u)

    out = []
    for v in range(n):
        total = sum(dp_down[v]) + sum(dp_up[v])
        out.append(str(total))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
