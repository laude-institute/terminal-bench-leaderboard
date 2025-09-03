#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    colors = [int(next(it)) for _ in range(n)]
    # remove consecutive duplicates
    seq = []
    for c in colors:
        if not seq or seq[-1] != c:
            seq.append(c)
    m = len(seq)
    # dp[i][j]: min strokes to paint seq[i..j]
    dp = [[0] * m for _ in range(m)]
    for i in range(m):
        dp[i][i] = 1
    for length in range(2, m+1):
        for i in range(0, m-length+1):
            j = i + length - 1
            # default: paint j separately
            dp[i][j] = dp[i][j-1] + 1
            # try to merge with same color
            for k in range(i, j):
                if seq[k] == seq[j]:
                    cost = dp[i][k] + (dp[k+1][j-1] if k+1 <= j-1 else 0)
                    if cost < dp[i][j]:
                        dp[i][j] = cost
    # result
    print(dp[0][m-1])

if __name__ == '__main__':
    main()
