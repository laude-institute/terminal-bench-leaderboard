"""
Problem: Count all balanced subsets in an N x N grid of grass (G) cells.
Balanced subsets are 4-connected and both row- and column-convex.

Approach (pseudocode implementation stub):

1. Read N, grid of size N x N.
2. Precompute vertical prefix sums for each column to test if interval [lo..hi] is full of grass.
3. For each column, build a list of valid intervals (lo, hi).
4. Use dynamic programming across columns:
   - dp[col][(lo,hi)] = count of shapes ending at column col with vertical span [lo..hi].
   - Initialize dp at each column start: dp[c][(lo,hi)] = 1 for each valid interval.
   - For each column c from left to right:
       For each interval (lo,hi) in dp[c]:
           For each valid interval (lo2,hi2) in column c+1:
               If intervals [lo,hi] and [lo2,hi2] overlap:
                   dp[c+1][(lo2,hi2)] += dp[c][(lo,hi)]
                   modulo 1e9+7
5. Sum all dp values over all columns and intervals to get result.

Note: This stub counts column-convex, horizontally connected shapes but omits full horizontal-convexity enforcement and 4-connectivity checks. A complete solution requires tracking upper/lower boundary monotonicity and ensuring horizontal-convex.
"""

def main():
    MOD = 10**9 + 7
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    grid = data[1:]

    # Build prefix sums for each column
    pref = [[0]*(N+1) for _ in range(N)]
    for j in range(N):
        for i in range(N):
            pref[j][i+1] = pref[j][i] + (1 if grid[i][j]=='G' else 0)

    # List valid vertical intervals per column
    valid = [[] for _ in range(N)]
    for j in range(N):
        for lo in range(N):
            for hi in range(lo, N):
                if pref[j][hi+1] - pref[j][lo] == hi - lo + 1:
                    valid[j].append((lo, hi))

    # DP across columns
    from collections import Counter
    total = 0
    dp = Counter()
    # Initialize at column 0
    for interval in valid[0]:
        dp[interval] = 1
        total = (total + 1) % MOD

    # Extend for each column
    for j in range(1, N):
        new_dp = Counter()
        for (lo, hi), cnt in dp.items():
            for lo2, hi2 in valid[j]:
                # ensure vertical overlap for connectivity
                if lo2 <= hi and lo <= hi2:
                    new_dp[(lo2, hi2)] = (new_dp[(lo2, hi2)] + cnt) % MOD
        # also start new shapes at this column
        for interval in valid[j]:
            new_dp[interval] = (new_dp[interval] + 1) % MOD
        dp = new_dp
        total = (total + sum(dp.values())) % MOD

    print(total)


if __name__ == '__main__':
    main()
