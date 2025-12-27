#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pts = []
    idx = 1
    for _ in range(n):
        x = int(data[idx]); p = int(data[idx+1])
        pts.append((x, p))
        idx += 2
    # sort targets by position
    pts.sort(key=lambda t: t[0])
    x = [t[0] for t in pts]
    p = [t[1] for t in pts]
    # dp[j][i]: max points ending with a hop from j->i (j < i)
    dp = [ [0]*n for _ in range(n) ]
    # base max is single target
    max_score = max(p)
    # initialize length-2 hops
    for j in range(n):
        for i in range(j+1, n):
            dp[j][i] = p[j] + p[i]
            if dp[j][i] > max_score:
                max_score = dp[j][i]
    # extend to longer sequences
    for j in range(n):
        # build reverse prefix max of dp[k][j] for k < j
        if j == 0:
            continue
        rev_max = [0] * j
        rev_max[j-1] = dp[j-1][j]
        for k in range(j-2, -1, -1):
            rev_max[k] = dp[k][j] if dp[k][j] > rev_max[k+1] else rev_max[k+1]
        # for each possible next i
        for i in range(j+1, n):
            # require x[i] - x[j] >= x[j] - x[k]
            # => x[k] >= 2*x[j] - x[i]
            need = 2 * x[j] - x[i]
            left = bisect.bisect_left(x, need, 0, j)
            if left < j:
                best = rev_max[left]
                val = best + p[i]
                if val > dp[j][i]:
                    dp[j][i] = val
                    if val > max_score:
                        max_score = val
    # output result
    print(max_score)

if __name__ == '__main__':
    main()
