#!/usr/bin/env python3
"""
Count palindromic paths in an N x N letter grid.
DP with two pointers from start and end meeting in middle.
"""
import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    n = int(input().strip())
    grid = [input().strip() for _ in range(n)]

    # prev[i1][i2]: number of ways for k-1 steps, walkers at (i1, k-1-i1) and (i2, (2n-2-(k-1))-i2)
    prev = [[0] * n for _ in range(n)]
    # Initial k = 0
    if grid[0][0] == grid[n-1][n-1]:
        prev[0][n-1] = 1

    for k in range(1, n):
        cur = [[0] * n for _ in range(n)]
        for i1 in range(n):
            j1 = k - i1
            if j1 < 0 or j1 >= n:
                continue
            for i2 in range(n):
                j2 = (2*n - 2 - k) - i2
                if j2 < 0 or j2 >= n:
                    continue
                # match characters
                if grid[i1][j1] != grid[i2][j2]:
                    continue
                ways = 0
                # two moves for each walker
                for di1, dj1 in ((-1, 0), (0, -1)):
                    pi1, pj1 = i1 + di1, j1 + dj1
                    if pi1 < 0 or pj1 < 0:
                        continue
                    for di2, dj2 in ((1, 0), (0, 1)):
                        pi2, pj2 = i2 + di2, j2 + dj2
                        if pi2 >= n or pj2 >= n:
                            continue
                        ways += prev[pi1][pi2]
                cur[i1][i2] = ways % MOD
        prev = cur

    # Sum ways where pointers meet at same cell
    result = 0
    # at k = n-1, j1 = n-1-i1, j2 = n-1-i2, meeting requires i1 == i2
    for i in range(n):
        result = (result + prev[i][i]) % MOD
    print(result)


if __name__ == '__main__':
    main()
