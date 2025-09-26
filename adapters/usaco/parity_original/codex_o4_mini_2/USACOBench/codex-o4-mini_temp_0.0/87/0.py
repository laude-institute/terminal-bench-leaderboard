#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    components = []

    def bfs(si, sj):
        from collections import deque
        q = deque()
        q.append((si, sj))
        visited[si][sj] = True
        cells = [(si, sj)]
        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and grid[ni][nj] == 'X':
                    visited[ni][nj] = True
                    q.append((ni, nj))
                    cells.append((ni, nj))
        return cells

    # find the two spot components
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'X' and not visited[i][j]:
                comp = bfs(i, j)
                components.append(comp)
                if len(components) == 2:
                    break
        if len(components) == 2:
            break

    comp1, comp2 = components
    # compute minimal painting needed
    ans = float('inf')
    for x1, y1 in comp1:
        for x2, y2 in comp2:
            # number of cells between minus 1
            d = abs(x1 - x2) + abs(y1 - y2) - 1
            if d < ans:
                ans = d
    print(ans)

if __name__ == '__main__':
    main()
