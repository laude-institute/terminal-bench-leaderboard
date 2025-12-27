#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    grid = [list(next(it).strip()) for _ in range(n)]
    MOD = 10**9 + 7
    # Total steps from start to end
    total = 2 * n - 2
    # dp[i1][i2]: number of ways for two walkers at (i1, t-i1) and (i2, total-t-i2)
    dp = [[0] * n for _ in range(n)]
    # Initial positions (0,0) and (n-1,n-1)
    if grid[0][0] == grid[n-1][n-1]:
        dp[0][n-1] = 1
    # Iterate over steps t from 1 to n-1 (half path)
    for t in range(1, n):
        new_dp = [[0] * n for _ in range(n)]
        # i1 range where j1 = t - i1 is valid
        i1_lo = max(0, t - (n-1))
        i1_hi = min(n-1, t)
        # For walker2, j2 = total - t - i2
        rem = total - t
        i2_lo = max(0, rem - (n-1))
        i2_hi = min(n-1, rem)
        for i1 in range(i1_lo, i1_hi + 1):
            j1 = t - i1
            # ensure j1 in bounds
            # for each i2
            for i2 in range(i2_lo, i2_hi + 1):
                j2 = rem - i2
                if grid[i1][j1] != grid[i2][j2]:
                    continue
                val = 0
                # previous moves: walker1 from up or left; walker2 from down or right
                # up: (i1-1, j1), left: (i1, j1-1)
                # down: (i2+1, j2), right: (i2, j2+1)
                # combine all
                if i1 > 0 and i2 < n-1:
                    val += dp[i1-1][i2+1]
                if i1 > 0 and j2 < n-1:
                    val += dp[i1-1][i2]
                if j1 > 0 and i2 < n-1:
                    val += dp[i1][i2+1]
                if j1 > 0 and j2 < n-1:
                    val += dp[i1][i2]
                new_dp[i1][i2] = val % MOD
        dp = new_dp
    # After n-1 steps, walkers meet at same cell: i1 == i2
    ans = 0
    for i in range(n):
        ans = (ans + dp[i][i]) % MOD
    print(ans)

if __name__ == '__main__':
    main()
