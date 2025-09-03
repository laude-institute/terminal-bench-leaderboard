#!/usr/bin/env python3

def main():
    import sys
    sys.setrecursionlimit(10000)
    input = sys.stdin.readline
    N = int(input().strip())
    grid = [list(input().strip()) for _ in range(N)]
    # We perform a meet-in-the-middle: generate all prefixes and suffixes of length N
    target_len = N
    from collections import defaultdict

    # prefix[(i,j)] = set of strings of length N reaching (i,j) from (0,0)
    prefix = defaultdict(set)
    # suffix[(i,j)] = set of strings of length N reaching (i,j) from (N-1,N-1)
    suffix = defaultdict(set)

    def dfs_prefix(i, j, s):
        if len(s) == target_len:
            prefix[(i, j)].add(s)
            return
        # move down
        if i + 1 < N:
            dfs_prefix(i + 1, j, s + grid[i + 1][j])
        # move right
        if j + 1 < N:
            dfs_prefix(i, j + 1, s + grid[i][j + 1])

    def dfs_suffix(i, j, s):
        if len(s) == target_len:
            suffix[(i, j)].add(s)
            return
        # move up
        if i - 1 >= 0:
            dfs_suffix(i - 1, j, s + grid[i - 1][j])
        # move left
        if j - 1 >= 0:
            dfs_suffix(i, j - 1, s + grid[i][j - 1])

    # build prefix and suffix sets
    dfs_prefix(0, 0, grid[0][0])
    dfs_suffix(N - 1, N - 1, grid[N - 1][N - 1])

    # count distinct palindromes by intersecting at midpoint cells
    result = 0
    for cell, pre_set in prefix.items():
        suf_set = suffix.get(cell)
        if suf_set:
            # only strings appearing in both sets form valid palindromes
            result += len(pre_set & suf_set)

    print(result)

if __name__ == '__main__':
    main()
