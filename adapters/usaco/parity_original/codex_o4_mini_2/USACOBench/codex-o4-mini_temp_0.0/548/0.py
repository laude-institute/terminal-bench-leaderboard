#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    grid = [input().rstrip() for _ in range(N)]
    # The path length is 2*N-1; if start and end letters differ, no palindrome is possible
    if grid[0][0] != grid[N-1][N-1]:
        print(0)
        return
    K = N - 1
    # Build all prefix strings of length N to mid-layer (i+j == K)
    prefix_dp = {(0, 0): {grid[0][0]}}
    for _ in range(K):
        next_dp = {}
        for (i, j), ss in prefix_dp.items():
            for s in ss:
                if i + 1 < N:
                    pos = (i + 1, j)
                    next_dp.setdefault(pos, set()).add(s + grid[i+1][j])
                if j + 1 < N:
                    pos = (i, j + 1)
                    next_dp.setdefault(pos, set()).add(s + grid[i][j+1])
        prefix_dp = next_dp
    # Build all reversed suffix strings of length N from end to mid-layer
    suffix_dp = {(N-1, N-1): {grid[N-1][N-1]}}
    for _ in range(K):
        next_dp = {}
        for (i, j), ss in suffix_dp.items():
            for rev in ss:
                if i - 1 >= 0:
                    pos = (i - 1, j)
                    next_dp.setdefault(pos, set()).add(grid[i-1][j] + rev)
                if j - 1 >= 0:
                    pos = (i, j - 1)
                    next_dp.setdefault(pos, set()).add(grid[i][j-1] + rev)
        suffix_dp = next_dp
    # Count distinct palindromes by intersecting prefix and suffix_rev sets at mid cells
    result = 0
    for pos, ps in prefix_dp.items():
        ss = suffix_dp.get(pos)
        if ss:
            result += len(ps & ss)
    print(result)

if __name__ == "__main__":
    main()
