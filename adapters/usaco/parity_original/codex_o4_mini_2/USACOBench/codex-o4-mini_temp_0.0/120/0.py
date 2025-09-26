#!/usr/bin/env python3
import sys
sys.setrecursionlimit(200000)

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        adj[u].append(v)
        adj[v].append(u)
    C = [int(input()) for _ in range(N)]
    # dp_sub[u][d]: sum of cows in subtree of u at distance d from u
    dp_sub = [[0] * (K+1) for _ in range(N)]
    # post-order DFS to fill dp_sub
    def dfs1(u, p):
        dp_sub[u][0] = C[u]
        for v in adj[u]:
            if v == p: continue
            dfs1(v, u)
            for d in range(1, K+1):
                dp_sub[u][d] += dp_sub[v][d-1]
    
    dfs1(0, -1)
    # dp_up[u][d]: sum of cows not in subtree of u at distance d from u
    dp_up = [[0] * (K+1) for _ in range(N)]
    # pre-order DFS to fill dp_up
    def dfs2(u, p):
        for v in adj[u]:
            if v == p: continue
            # distance 1: parent itself
            dp_up[v][1] = C[u]
            for d in range(2, K+1):
                # from above u and siblings
                val = dp_up[u][d-1] + dp_sub[u][d-1]
                # subtract contribution from v's subtree
                val -= dp_sub[v][d-2]
                dp_up[v][d] = val
            dfs2(v, u)
    
    dfs2(0, -1)
    # compute and output results
    out = []
    for u in range(N):
        total = 0
        for d in range(0, K+1):
            total += dp_sub[u][d] + dp_up[u][d]
        out.append(str(total))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
