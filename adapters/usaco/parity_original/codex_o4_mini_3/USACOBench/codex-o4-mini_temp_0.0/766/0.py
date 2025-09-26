#!/usr/bin/env python3
import sys
sys.setrecursionlimit(200000)

def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    MOD = 10**9 + 7
    n = int(next(it))
    k = int(next(it))
    # build adjacency
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    # colors: 0 if uncolored, else 1..3
    colors = [0] * (n+1)
    for _ in range(k):
        b = int(next(it)); c = int(next(it))
        colors[b] = c

    # dp[v][c]: number of ways to color subtree v if v has color c
    def dfs(v, p):
        # dp for this node
        dp = [0, 0, 0, 0]
        # allowed colors at v
        if colors[v] != 0:
            allowed = [colors[v]]
        else:
            allowed = [1, 2, 3]
        for c in allowed:
            total = 1
            for u in adj[v]:
                if u == p:
                    continue
                dp_u = dfs(u, v)
                # sum ways for child u with color != c
                s = 0
                for cc in (1, 2, 3):
                    if cc != c:
                        s = (s + dp_u[cc])
                total = total * (s % MOD) % MOD
                if total == 0:
                    break
            dp[c] = total
        return dp

    # compute from root = 1
    res_dp = dfs(1, 0)
    # sum over root colors
    ans = (res_dp[1] + res_dp[2] + res_dp[3]) % MOD
    print(ans)

if __name__ == '__main__':
    main()
