#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    A = float(next(it))
    B = float(next(it))
    positions = [float(next(it)) for _ in range(n)]
    positions.sort()

    # dp[j] = min cost to cover first j cows (1-indexed)
    dp = [0.0] + [float('inf')] * n
    # Use 1-based indexing for convenience
    pos = [0.0] + positions

    for j in range(1, n+1):
        # consider covering cows i..j with one base station
        for i in range(1, j+1):
            # minimal required radius is half distance from pos[i] to pos[j]
            r = (pos[j] - pos[i]) / 2.0
            cost = A + B * r
            dp[j] = min(dp[j], dp[i-1] + cost)

    # output result
    # prints as float, retains .5 if needed
    res = dp[n]
    # Remove trailing zeros for nicer formatting
    if res.is_integer():
        print(f"{int(res)}")
    else:
        print(res)

if __name__ == '__main__':
    main()
