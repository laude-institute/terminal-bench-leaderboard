#!/usr/bin/env python3
import sys
from collections import deque

def main():
    sys.setrecursionlimit(10000)
    input = sys.stdin.readline
    R, C = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]

    # Label islands with ids and record their cells
    label = [[-1]*C for _ in range(R)]
    islands = []  # list of lists of (r,c)
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def dfs(r, c, id):
        stack = [(r, c)]
        label[r][c] = id
        cells = [(r, c)]
        while stack:
            x, y = stack.pop()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == 'X' and label[nx][ny] == -1:
                        label[nx][ny] = id
                        cells.append((nx, ny))
                        stack.append((nx, ny))
        return cells

    nid = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'X' and label[i][j] == -1:
                cells = dfs(i, j, nid)
                islands.append(cells)
                nid += 1
    n = nid

    # Compute pairwise swimming distances via 0-1 BFS
    INF = 10**9
    dist_mat = [[INF]*n for _ in range(n)]
    for i in range(n):
        # 0-1 BFS from island i
        dist = [[INF]*C for _ in range(R)]
        dq = deque()
        for (r, c) in islands[i]:
            dist[r][c] = 0
            dq.appendleft((r, c))
        while dq:
            x, y = dq.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == '.':
                        continue
                    w = 1 if grid[nx][ny] == 'S' else 0
                    nd = dist[x][y] + w
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if w == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        # fill distances
        for j in range(n):
            if i == j: continue
            best = INF
            for (r, c) in islands[j]:
                if dist[r][c] < best:
                    best = dist[r][c]
            dist_mat[i][j] = best

    # Minimum spanning tree via Prim's algorithm
    visited = [False]*n
    min_edge = [INF]*n
    min_edge[0] = 0
    total = 0
    for _ in range(n):
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        visited[u] = True
        total += min_edge[u]
        for v in range(n):
            if not visited[v] and dist_mat[u][v] < min_edge[v]:
                min_edge[v] = dist_mat[u][v]

    print(total)

if __name__ == '__main__':
    main()
