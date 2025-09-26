#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]
    # Label islands
    island_id = [[-1] * C for _ in range(R)]
    islands = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(si, sj, cid):
        stack = [(si, sj)]
        island_id[si][sj] = cid
        cells = []
        while stack:
            x, y = stack.pop()
            cells.append((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 'X' and island_id[nx][ny] == -1:
                    island_id[nx][ny] = cid
                    stack.append((nx, ny))
        return cells
    cid = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'X' and island_id[i][j] == -1:
                islands.append(dfs(i, j, cid))
                cid += 1
    N = cid

    # Compute pairwise distances with 0-1 BFS
    INF = 10**9
    dist_mat = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist = [[INF] * C for _ in range(R)]
        dq = deque()
        # Multi-source from island i
        for x, y in islands[i]:
            dist[x][y] = 0
            dq.appendleft((x, y))
        while dq:
            x, y = dq.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '.':
                    w = 1 if grid[nx][ny] == 'S' else 0
                    nd = dist[x][y] + w
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if w == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        # Record distances to other islands
        for j in range(N):
            if i == j:
                dist_mat[i][j] = 0
            else:
                best = INF
                for x, y in islands[j]:
                    best = min(best, dist[x][y])
                dist_mat[i][j] = best

    # Minimum spanning tree (Prim's algorithm)
    used = [False] * N
    min_e = [INF] * N
    min_e[0] = 0
    result = 0
    for _ in range(N):
        v = -1
        for k in range(N):
            if not used[k] and (v == -1 or min_e[k] < min_e[v]):
                v = k
        used[v] = True
        result += min_e[v]
        for to in range(N):
            if not used[to] and dist_mat[v][to] < min_e[to]:
                min_e[to] = dist_mat[v][to]

    print(result)

if __name__ == '__main__':
    main()
