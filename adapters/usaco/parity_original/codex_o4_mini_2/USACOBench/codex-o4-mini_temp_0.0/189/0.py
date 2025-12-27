#!/usr/bin/env python3
import sys

def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    grid = [list(next(it).strip()) for _ in range(N)]
    # If starting char is ')', no balanced string possible
    if grid[0][0] == ')':
        print(0)
        return
    visited = [[False] * N for _ in range(N)]
    best = 0
    # Directions: up, down, left, right
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c, op, cl):
        nonlocal best
        # Invalid if more closes than opens
        if cl > op:
            return
        # Update best when perfectly balanced so far
        if op == cl:
            best = max(best, op + cl)
        # Explore neighbors
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                ch = grid[nr][nc]
                # Can pick '(' only before picking any ')'
                if ch == '(' and cl == 0:
                    visited[nr][nc] = True
                    dfs(nr, nc, op + 1, cl)
                    visited[nr][nc] = False
                # Can pick ')' only if it won't exceed opens
                elif ch == ')' and cl < op:
                    visited[nr][nc] = True
                    dfs(nr, nc, op, cl + 1)
                    visited[nr][nc] = False

    # Start DFS from (0,0)
    visited[0][0] = True
    dfs(0, 0, 1, 0)
    print(best)

if __name__ == '__main__':
    main()
