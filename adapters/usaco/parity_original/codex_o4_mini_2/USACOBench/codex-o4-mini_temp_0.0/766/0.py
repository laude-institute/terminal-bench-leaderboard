#!/usr/bin/env python3
import sys
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().split()
    it = iter(data)
    mod = 10**9 + 7
    N = int(next(it))
    K = int(next(it))
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    color = [0] * (N + 1)
    for _ in range(K):
        b = int(next(it))
        c = int(next(it))
        color[b] = c
    dp = [[0] * 4 for _ in range(N + 1)]
    stack = [(1, 0, False)]
    # iterative post-order DFS
    while stack:
        u, p, visited = stack.pop()
        if not visited:
            stack.append((u, p, True))
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, False))
        else:
            for c in (1, 2, 3):
                if color[u] != 0 and c != color[u]:
                    dp[u][c] = 0
                    continue
                ways = 1
                for v in adj[u]:
                    if v == p:
                        continue
                    total = 0
                    for cv in (1, 2, 3):
                        if cv != c:
                            total = (total + dp[v][cv]) % mod
                    ways = (ways * total) % mod
                dp[u][c] = ways
    result = sum(dp[1][1:4]) % mod
    print(result)

if __name__ == '__main__':
    main()
