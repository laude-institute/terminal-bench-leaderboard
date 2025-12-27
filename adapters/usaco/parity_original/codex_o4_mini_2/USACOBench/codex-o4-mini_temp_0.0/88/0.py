#!/usr/bin/env python3
"""
Solution to Cow Beauty Pageant (pageant).
Computes minimal additional 'X's needed to merge three spots.
"""
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(input().rstrip('\n')) for _ in range(N)]

    # Identify the three spot components
    visited = [[False] * M for _ in range(N)]
    components = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'X' and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                comp_cells = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if not visited[nx][ny] and grid[nx][ny] == 'X':
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                comp_cells.append((nx, ny))
                components.append(comp_cells)

    # Perform 0-1 BFS from each component to compute painting costs
    INF = 10**9
    dists = []
    for comp in components:
        dist = [[INF] * M for _ in range(N)]
        dq = deque()
        # Initialize BFS with component cells at cost 0
        for x, y in comp:
            dist[x][y] = 0
            dq.appendleft((x, y))
        # 0-1 BFS
        while dq:
            x, y = dq.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    w = 0 if grid[nx][ny] == 'X' else 1
                    nd = dist[x][y] + w
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if w == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        dists.append(dist)

    # Combine distances to find minimal paints to merge all three
    ans = INF
    for i in range(N):
        for j in range(M):
            d0, d1, d2 = dists[0][i][j], dists[1][i][j], dists[2][i][j]
            if d0 < INF and d1 < INF and d2 < INF:
                total = d0 + d1 + d2
                # Overcounting the meeting cell if it was '.'
                if grid[i][j] == '.':
                    total -= 2
                ans = min(ans, total)
    print(ans)

if __name__ == '__main__':
    main()
