#!/usr/bin/env python3
"""
Solution to count paths from top-left to bottom-right on an N x N grid
with at most K direction changes, avoiding haybales.
Moves allowed: down (D) and right (R).
"""
import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        grid = [input().strip() for _ in range(N)]

        # dp[i][j][k][d]: ways to reach (i,j) with k changes, last move d (0=down,1=right)
        dp = [[[[0]*2 for _ in range(K+1)] for _ in range(N)] for __ in range(N)]

        # Initialize first moves from (0,0)
        if grid[0][1] == '.':
            dp[0][1][0][1] = 1
        if grid[1][0] == '.':
            dp[1][0][0][0] = 1

        # Fill dp table
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 'H' or (i == 0 and j == 0):
                    continue
                for k in range(K+1):
                    for d in (0, 1):
                        cnt = dp[i][j][k][d]
                        if cnt == 0:
                            continue
                        # Move down
                        ni, nj = i+1, j
                        if ni < N and grid[ni][nj] == '.':
                            nk = k + (d != 0)
                            if nk <= K:
                                dp[ni][nj][nk][0] += cnt
                        # Move right
                        ni, nj = i, j+1
                        if nj < N and grid[ni][nj] == '.':
                            nk = k + (d != 1)
                            if nk <= K:
                                dp[ni][nj][nk][1] += cnt

        # Sum ways at destination over all k and both directions
        total = 0
        for k in range(K+1):
            total += dp[N-1][N-1][k][0] + dp[N-1][N-1][k][1]
        print(total)

if __name__ == '__main__':
    main()
