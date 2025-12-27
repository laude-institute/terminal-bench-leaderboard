#!/usr/bin/env python3
"""
Count the number of palindromic paths from the top-left to
bottom-right of an N x N grid, moving only right or down.
Use a two-pointer DP meeting in the middle to ensure palindrome property.
"""
import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    # If start/end chars differ, no palindromes exist
    if grid[0][0] != grid[N-1][N-1]:
        print(0)
        return

    # dp[r1][r2]: ways where first pointer at (r1, c1) and
    # second pointer at (r2, c2) after k steps, matching so far
    dp = [[0] * N for _ in range(N)]
    dp[0][N-1] = 1

    # iterate over steps k from 1 to N-1 (half the path length)
    for k in range(1, N):
        ndp = [[0] * N for _ in range(N)]
        # r1 + c1 = k; r2 + c2 = 2*(N-1) - k
        for r1 in range(max(0, k-(N-1)), min(N-1, k) + 1):
            c1 = k - r1
            for r2 in range(max(0, (N-1)-k), min(N-1, 2*(N-1)-k) + 1):
                c2 = (2*(N-1) - k) - r2
                ways = dp[r1][r2]
                if ways == 0:
                    continue
                # move first pointer: down or right
                for dr1, dc1 in ((1, 0), (0, 1)):
                    nr1, nc1 = r1 + dr1, c1 + dc1
                    if not (0 <= nr1 < N and 0 <= nc1 < N):
                        continue
                    # move second pointer: up or left
                    for dr2, dc2 in ((-1, 0), (0, -1)):
                        nr2, nc2 = r2 + dr2, c2 + dc2
                        if not (0 <= nr2 < N and 0 <= nc2 < N):
                            continue
                        if grid[nr1][nc1] != grid[nr2][nc2]:
                            continue
                        ndp[nr1][nr2] = (ndp[nr1][nr2] + ways) % MOD
        dp = ndp

    # At k = N-1, both pointers meet on the same cell (odd-length path)
    result = 0
    for r in range(N):
        result = (result + dp[r][r]) % MOD
    print(result)

if __name__ == '__main__':
    main()
