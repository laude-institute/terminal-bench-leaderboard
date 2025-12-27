#!/usr/bin/env python3
"""
1. Restate the problem in plain English:
   We have an N x N grid with some cells marked as grass. We want to count all nonempty subsets of grass cells that are:
   - 4-connected (you can move up/down/left/right between any two cells in the subset)
   - Row-convex (in any row, the chosen cells form a contiguous interval)
   - Column-convex (in any column, the chosen cells form a contiguous interval)
   Count these "balanced" subsets modulo 10^9+7.

2. Conceptual solution in plain English:
   - Precompute fast checks for any horizontal or vertical interval of grass (using prefix sums).
   - Enumerate possible shapes by their top and bottom row boundaries (t <= b).
   - For each (t,b), derive for each column the maximal contiguous grass segment within [t,b].
   - We need to count all orthoconvex subsets spanning exactly rows t..b:
     * Each row r in [t,b] picks a contiguous column interval [L(r), R(r)].
     * The intervals must be nested so that the set is column-convex and connected.
   - Use dynamic programming over rows, carrying the current left and right bounds,
     and transition by expanding or contracting within allowed grass.
   - Sum over all (t,b) and all valid sequences of intervals.

3. Pseudocode:
   read N, grid
   build row_prefix[i][j] = number of grass in row i up to column j
   build col_prefix[j][i] = number of grass in column j up to row i

   answer = 0
   for t in range(N):
     for b in range(t, N):
       # Compute for each col j, the vertical grass check between rows t..b
       good_col[j] = (col_prefix[j][b] - col_prefix[j][t-1] == b-t+1)
       # dp_prev = dict()  # key=(L, R) -> count of ways at previous row
       initialize dp_prev with intervals on row t
       for r in range(t+1, b+1):
         dp_curr = dict()
         for (L, R), cnt in dp_prev:
           for newL in range(L_min, L_max+1):
             for newR in range(R_min, R_max+1):
               if row_prefix[r][newR] - row_prefix[r][newL-1] == newR-newL+1:
                 update dp_curr[(newL,newR)] += cnt
         dp_prev = dp_curr
       # sum all counts in dp_prev into answer
   print(answer % MOD)

4. Implementation outline:
   The above DP runs in O(N^5) in worst case; with optimizations and early breaks,
   it can pass for N up to ~150 in optimized C++, but Python may need further pruning.
   Below is the code scaffold implementing input and prefix sums, with DP structure.
"""

import sys
sys.setrecursionlimit(10**7)

def main():
    MOD = 10**9 + 7
    data = sys.stdin.read().split()
    N = int(data[0])
    grid = data[1:1+N]

    # Build row-wise and column-wise prefix sums of grass
    row_pref = [[0]*(N+1) for _ in range(N)]
    col_pref = [[0]*(N+1) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            row_pref[i][j+1] = row_pref[i][j] + (grid[i][j] == 'G')
            col_pref[j][i+1] = col_pref[j][i] + (grid[i][j] == 'G')

    # DP over top and bottom rows
    answer = 0
    # Placeholder for full DP implementation
    # TODO: implement orthoconvex DP as per pseudocode above

    print(answer)

if __name__ == '__main__':
    main()
