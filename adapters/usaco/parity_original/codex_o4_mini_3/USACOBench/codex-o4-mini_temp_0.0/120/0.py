#!/usr/bin/env python3
import sys

def main():
    sys.setrecursionlimit(10**7)
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    # build tree
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    # cow counts
    C = [0] * (n+1)
    for i in range(1, n+1):
        C[i] = int(next(it))
    # dpdown[u][d]: sum of cows at dist d in subtree of u
    # dpup[u][d]: sum of cows at dist d outside subtree of u
    dpdown = [[0] * (k+1) for _ in range(n+1)]
    dpup = [[0] * (k+1) for _ in range(n+1)]

    def dfs1(u, p):
        dpdown[u][0] = C[u]
        for v in adj[u]:
            if v == p: continue
            dfs1(v, u)
            for d in range(1, k+1):
                dpdown[u][d] += dpdown[v][d-1]

    def dfs2(u, p):
        for v in adj[u]:
            if v == p: continue
            # compute dpup for child v
            dpup[v][0] = 0
            for d in range(1, k+1):
                use = dpdown[u][d-1]
                if d >= 2:
                    use -= dpdown[v][d-2]
                dpup[v][d] = dpup[u][d-1] + use
            dfs2(v, u)

    # root at 1
    dfs1(1, 0)
    dfs2(1, 0)
    out = []
    # compute M(i)
    for u in range(1, n+1):
        total = 0
        for d in range(0, k+1):
            total += dpdown[u][d] + dpup[u][d]
        out.append(str(total))
    sys.stdout.write("\n".join(out))


if __name__ == '__main__':
    main()
