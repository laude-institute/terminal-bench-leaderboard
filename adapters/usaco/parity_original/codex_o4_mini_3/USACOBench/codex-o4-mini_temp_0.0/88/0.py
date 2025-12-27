#!/usr/bin/env python3
"""
Solution to USACO Silver 'Cow Beauty Pageant' problem.
Find minimum number of new 'X's to paint to connect three spots.
"""
import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    # Label the three components
    comp_id = [[-1]*M for _ in range(N)]
    comps = []  # list of lists of (i,j)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'X' and comp_id[i][j] == -1:
                cid = len(comps)
                comps.append([])
                # BFS/DFS to label
                dq = deque([(i, j)])
                comp_id[i][j] = cid
                while dq:
                    x, y = dq.popleft()
                    comps[cid].append((x, y))
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if grid[nx][ny] == 'X' and comp_id[nx][ny] == -1:
                                comp_id[nx][ny] = cid
                                dq.append((nx, ny))
    # We expect exactly 3 components
    # Compute distance grids from each component
    INF = 10**9
    dists = []
    for cid in range(3):
        dist = [[INF]*M for _ in range(N)]
        dq = deque()
        # initialize
        for x, y in comps[cid]:
            dist[x][y] = 0
            dq.append((x, y))
        # BFS
        while dq:
            x, y = dq.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M:
                    if dist[nx][ny] == INF:
                        dist[nx][ny] = dist[x][y] + 1
                        dq.append((nx, ny))
        dists.append(dist)
    # Find minimal sum of distances - 2
    ans = INF
    for i in range(N):
        for j in range(M):
            # all must be reachable
            d0 = dists[0][i][j]
            d1 = dists[1][i][j]
            d2 = dists[2][i][j]
            if d0 < INF and d1 < INF and d2 < INF:
                # subtract 2 because the meeting cell counted thrice
                total = d0 + d1 + d2 - 2
                if total < ans:
                    ans = total
    print(ans)


if __name__ == '__main__':
    main()
