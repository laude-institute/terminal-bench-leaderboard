#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    grid = []
    for _ in range(N):
        grid.append(list(next(it).strip()))

    # Direction indices: 0=up,1=right,2=down,3=left
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    # Mirror reflections
    slash = {0:1, 1:0, 2:3, 3:2}
    back = {0:3, 3:0, 2:1, 1:2}

    total_states = N * M * 4
    dp = [0] * total_states  # 0=uncomputed, >0 steps, -1 infinite
    visited = [False] * total_states

    def dfs(s):  # returns steps or -1
        if dp[s] != 0:
            return dp[s]
        if visited[s]:
            return -1
        visited[s] = True
        cell = s >> 2
        dir = s & 3
        i = cell // M
        j = cell % M
        # reflect
        m = grid[i][j]
        if m == '/':
            nd = slash[dir]
        else:
            nd = back[dir]
        ni = i + di[nd]
        nj = j + dj[nd]
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            ans = 1
        else:
            ns = ((ni * M + nj) << 2) | nd
            res = dfs(ns)
            ans = -1 if res == -1 else res + 1
        dp[s] = ans
        visited[s] = False
        return ans

    results = 0
    # Entry points
    # Top edge: row -1, columns 0..M-1, dir down(2)
    for j in range(M):
        s = ((0 * M + j) << 2) | 2
        r = dfs(s)
        if r == -1:
            print(-1)
            return
        results = max(results, r)
    # Bottom edge: row N, dir up(0)
    for j in range(M):
        s = (((N-1) * M + j) << 2) | 0
        r = dfs(s)
        if r == -1:
            print(-1)
            return
        results = max(results, r)
    # Left edge: col -1, rows 0..N-1, dir right(1)
    for i in range(N):
        s = ((i * M + 0) << 2) | 1
        r = dfs(s)
        if r == -1:
            print(-1)
            return
        results = max(results, r)
    # Right edge: col M, dir left(3)
    for i in range(N):
        s = ((i * M + (M-1)) << 2) | 3
        r = dfs(s)
        if r == -1:
            print(-1)
            return
        results = max(results, r)

    print(results)

if __name__ == '__main__':
    main()
