#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    K = int(input())
    # Initialize 5x5 field: 1 for grass, 0 for barren
    grid = [[1] * 5 for _ in range(5)]
    for _ in range(K):
        i, j = map(int, input().split())
        grid[i-1][j-1] = 0
    # Count total grassy squares
    total_grass = sum(grid[r][c] for r in range(5) for c in range(5))
    # Total simultaneous move steps before meeting
    total_steps = (total_grass - 1) // 2
    # Visited cells tracker
    visited = [[False] * 5 for _ in range(5)]
    # Starting positions
    visited[0][0] = True  # Bessie starts at (1,1)
    visited[4][4] = True  # Mildred starts at (5,5)

    # Directions: N, S, W, E
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    sys.setrecursionlimit(10000)

    def dfs(bx, by, mx, my, step):
        # Final move: cows must meet on last remaining grass
        if step == total_steps - 1:
            ways = 0
            # Bessie's move to meeting cell
            for dx, dy in dirs:
                nbx, nby = bx + dx, by + dy
                if not (0 <= nbx < 5 and 0 <= nby < 5):
                    continue
                if grid[nbx][nby] == 0 or visited[nbx][nby]:
                    continue
                # Mildred must also reach this cell
                if abs(nbx - mx) + abs(nby - my) != 1:
                    continue
                ways += 1
            return ways

        total = 0
        # Intermediate moves: both cows move to distinct new grass
        for dx1, dy1 in dirs:
            nbx, nby = bx + dx1, by + dy1
            if not (0 <= nbx < 5 and 0 <= nby < 5):
                continue
            if grid[nbx][nby] == 0 or visited[nbx][nby]:
                continue
            visited[nbx][nby] = True
            for dx2, dy2 in dirs:
                nmx, nmy = mx + dx2, my + dy2
                if not (0 <= nmx < 5 and 0 <= nmy < 5):
                    continue
                if grid[nmx][nmy] == 0 or visited[nmx][nmy]:
                    continue
                # Prevent premature meeting
                if nbx == nmx and nby == nmy:
                    continue
                visited[nmx][nmy] = True
                total += dfs(nbx, nby, nmx, nmy, step + 1)
                visited[nmx][nmy] = False
            visited[nbx][nby] = False
        return total

    result = dfs(0, 0, 4, 4, 0)
    print(result)

if __name__ == '__main__':
    main()
