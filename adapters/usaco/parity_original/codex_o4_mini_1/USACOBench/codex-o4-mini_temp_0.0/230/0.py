#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(R)]

    # Label islands via DFS
    island_id = [[-1]*C for _ in range(R)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    nid = 0
    def dfs(i, j, id_):
        stack = [(i,j)]
        island_id[i][j] = id_
        while stack:
            x, y = stack.pop()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 'X' and island_id[nx][ny] < 0:
                    island_id[nx][ny] = id_
                    stack.append((nx, ny))

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'X' and island_id[i][j] < 0:
                dfs(i, j, nid)
                nid += 1

    # Compute pairwise swim costs with 0-1 BFS
    INF = 10**9
    dist = [[INF]*nid for _ in range(nid)]
    for src in range(nid):
        # dist grid
        dgrid = [[INF]*C for _ in range(R)]
        dq = deque()
        # initialize from island src cells
        for i in range(R):
            for j in range(C):
                if island_id[i][j] == src:
                    dgrid[i][j] = 0
                    dq.append((i, j))
        # 0-1 BFS
        while dq:
            x, y = dq.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < R and 0 <= ny < C): continue
                if grid[nx][ny] == '.': continue
                cost = dgrid[x][y] + (1 if grid[nx][ny] == 'S' else 0)
                if cost < dgrid[nx][ny]:
                    dgrid[nx][ny] = cost
                    if grid[nx][ny] == 'S': dq.append((nx, ny))
                    else: dq.appendleft((nx, ny))
        # record distances
        for i in range(R):
            for j in range(C):
                id2 = island_id[i][j]
                if id2 >= 0 and id2 != src:
                    dist[src][id2] = min(dist[src][id2], dgrid[i][j])

    # TSP DP over subsets
    ALL = 1 << nid
    dp = [[INF]*nid for _ in range(ALL)]
    for i in range(nid):
        dp[1<<i][i] = 0
    for mask in range(ALL):
        for u in range(nid):
            if not (mask & (1<<u)): continue
            if dp[mask][u] >= INF: continue
            for v in range(nid):
                if mask & (1<<v): continue
                nd = dp[mask][u] + dist[u][v]
                nm = mask | (1<<v)
                if nd < dp[nm][v]: dp[nm][v] = nd
    # answer is min over full mask
    full = ALL - 1
    ans = min(dp[full][i] for i in range(nid))
    print(ans)

if __name__ == '__main__':
    main()
