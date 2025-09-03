#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(N)]
    # label the three spots with flood-fill
    comp = [[-1]*M for _ in range(N)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    components = []
    cid = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'X' and comp[i][j] == -1:
                q = deque([(i, j)])
                comp[i][j] = cid
                cells = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if grid[nx][ny] == 'X' and comp[nx][ny] == -1:
                                comp[nx][ny] = cid
                                q.append((nx, ny))
                                cells.append((nx, ny))
                components.append(cells)
                cid += 1
    # compute 0-1 BFS distances from each spot to every cell
    INF = 10**9
    dist = [[[INF]*M for _ in range(N)] for _ in range(3)]
    for k in range(3):
        dq = deque()
        for x, y in components[k]:
            dist[k][x][y] = 0
            dq.append((x, y))
        while dq:
            x, y = dq.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M:
                    cost = 0 if grid[nx][ny] == 'X' else 1
                    nd = dist[k][x][y] + cost
                    if nd < dist[k][nx][ny]:
                        dist[k][nx][ny] = nd
                        if cost == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
    # find minimal combined cost, adjusting for shared painting
    ans = INF
    for i in range(N):
        for j in range(M):
            d0, d1, d2 = dist[0][i][j], dist[1][i][j], dist[2][i][j]
            if d0 < INF and d1 < INF and d2 < INF:
                total = d0 + d1 + d2
                if grid[i][j] == '.':
                    total -= 2
                ans = min(ans, total)
    print(ans)

if __name__ == '__main__':
    main()
