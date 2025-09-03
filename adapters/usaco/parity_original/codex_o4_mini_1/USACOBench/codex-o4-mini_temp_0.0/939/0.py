#!/usr/bin/env python3
from collections import deque

def main():
    # Read the grid and locate barn (B) and lake (L)
    grid = [input().strip() for _ in range(10)]
    barn = lake = None
    for r in range(10):
        for c in range(10):
            if grid[r][c] == 'B':
                barn = (r, c)
            elif grid[r][c] == 'L':
                lake = (r, c)

    # BFS from barn to lake, avoiding rock (R)
    dist = [[-1] * 10 for _ in range(10)]
    q = deque()
    br, bc = barn
    lr, lc = lake
    dist[br][bc] = 0
    q.append((br, bc))
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        r, c = q.popleft()
        if (r, c) == (lr, lc):
            break
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 10 and 0 <= nc < 10:
                if dist[nr][nc] == -1 and grid[nr][nc] != 'R':
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    # Number of cows is distance minus 1 (exclude barn-to-lake endpoints)
    result = dist[lr][lc] - 1
    print(result)

if __name__ == '__main__':
    main()
