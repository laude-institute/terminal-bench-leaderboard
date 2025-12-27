#!/usr/bin/env python3
import sys

def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    grid = [list(next(it).strip()) for _ in range(n)]
    # If starting cell is ')', no valid string
    if grid[0][0] == ')':
        print(0)
        return

    # Directions: up, down, left, right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    best = 0

    def dfs(i, j, visited, opens, closes):
        nonlocal best
        # Can't have more closing than opening
        if closes > opens:
            return
        # Update best when perfectly balanced
        if opens == closes:
            best = max(best, opens + closes)
        # Explore neighbors
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                idx = ni * n + nj
                mask = 1 << idx
                if visited & mask:
                    continue
                c = grid[ni][nj]
                # Can pick '(' only before any ')' is picked
                if c == '(' and closes == 0:
                    dfs(ni, nj, visited | mask, opens + 1, closes)
                # Can pick ')' only if there's unmatched '('
                elif c == ')' and opens > closes:
                    dfs(ni, nj, visited | mask, opens, closes + 1)

    # Start DFS from (0,0)
    start_mask = 1 << 0
    # First char is '('
    dfs(0, 0, start_mask, 1, 0)
    print(best)

if __name__ == '__main__':
    main()
