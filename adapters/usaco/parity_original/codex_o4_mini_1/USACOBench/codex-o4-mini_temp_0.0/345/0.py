#!/usr/bin/env python3
import sys
import bisect

def main():
    # Read input
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    targets = []
    for _ in range(N):
        x_i = int(next(it))
        p_i = int(next(it))
        targets.append((x_i, p_i))
    # Sort targets by position
    targets.sort(key=lambda t: t[0])
    x = [t[0] for t in targets]
    p = [t[1] for t in targets]
    # Base answer: best single target
    ans = max(p) if N > 0 else 0
    # dp[i][j]: max points for path with last hop i->j (i<j)
    dp = [[0] * N for _ in range(N)]
    # prefix_max[j][k]: for fixed j, max(dp[t][j] for t in k..j-1)
    prefix_max = [None] * N
    # Fill dp iteratively
    for j in range(N):
        for i in range(j):
            # Initial hop from i to j
            dp[i][j] = p[i] + p[j]
            # Extend from any k->i->j if feasible
            pm = prefix_max[i]
            if pm is not None:
                # required: x[j]-x[i] >= x[i]-x[k]  => x[k] >= 2*x[i]-x[j]
                low_val = 2 * x[i] - x[j]
                # find first k in [0..i-1] with x[k] >= low_val
                low = bisect.bisect_left(x, low_val, 0, i)
                if low < i:
                    best_prev = pm[low]
                    dp[i][j] = max(dp[i][j], best_prev + p[j])
            # Update global answer
            if dp[i][j] > ans:
                ans = dp[i][j]
        # Build prefix_max for column j
        if j > 0:
            pm = [0] * j
            # start from the end
            pm[j-1] = dp[j-1][j]
            for k in range(j-2, -1, -1):
                pm[k] = dp[k][j] if dp[k][j] > pm[k+1] else pm[k+1]
            prefix_max[j] = pm
    # Output result
    print(ans)

if __name__ == '__main__':
    main()
