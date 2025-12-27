#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)
MOD = 10**9+7

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    color = [0] * (N+1)
    for _ in range(K):
        b, c = map(int, input().split())
        color[b] = c
    # Check for adjacent precolor conflicts
    for u in range(1, N+1):
        if color[u]:
            for v in adj[u]:
                if color[v] == color[u]:
                    print(0)
                    return

    def dfs(u, p):
        # dp[c]: ways if node u is colored c
        if color[u] == 0:
            dp = [0, 1, 1, 1]
        else:
            dp = [0, 0, 0, 0]
            dp[color[u]] = 1
        for v in adj[u]:
            if v == p:
                continue
            dp_child = dfs(v, u)
            total = (dp_child[1] + dp_child[2] + dp_child[3]) % MOD
            new_dp = [0, 0, 0, 0]
            for c in range(1, 4):
                if dp[c]:
                    ways = (total - dp_child[c]) % MOD
                    new_dp[c] = dp[c] * ways % MOD
            dp = new_dp
        return dp

    res_dp = dfs(1, 0)
    print((res_dp[1] + res_dp[2] + res_dp[3]) % MOD)

if __name__ == '__main__':
    main()
