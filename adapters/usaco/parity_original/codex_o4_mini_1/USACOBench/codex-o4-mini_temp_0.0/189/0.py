#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10000)

def main():
    N = int(sys.stdin.readline().strip())
    grid = [sys.stdin.readline().strip() for _ in range(N)]
    # If starting at upper-left is ')', no valid string
    if grid[0][0] != '(':
        print(0)
        return

    visited = [[False] * N for _ in range(N)]
    max_len = 0

    # DFS to explore paths
    def dfs(r, c, open_count, close_count, phase):
        nonlocal max_len
        # If counts equal, update max length
        if open_count == close_count:
            max_len = max(max_len, open_count * 2)
        # Explore neighbors
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                ch = grid[nr][nc]
                # Open phase: can take '(' or start closing with ')'
                if phase == 'open':
                    if ch == '(':  # continue opening
                        visited[nr][nc] = True
                        dfs(nr, nc, open_count + 1, close_count, 'open')
                        visited[nr][nc] = False
                    elif ch == ')' and close_count < open_count:  # switch to closing
                        visited[nr][nc] = True
                        dfs(nr, nc, open_count, close_count + 1, 'close')
                        visited[nr][nc] = False
                else:  # Closing phase: only take ')' if possible
                    if ch == ')' and close_count < open_count:
                        visited[nr][nc] = True
                        dfs(nr, nc, open_count, close_count + 1, 'close')
                        visited[nr][nc] = False

    # Initialize
    visited[0][0] = True
    dfs(0, 0, 1, 0, 'open')
    print(max_len)

if __name__ == '__main__':
    main()
