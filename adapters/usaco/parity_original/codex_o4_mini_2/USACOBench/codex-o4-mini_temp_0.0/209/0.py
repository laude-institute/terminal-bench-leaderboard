#!/usr/bin/env python3
"""
Solution to the Wifi Setup problem.
Dynamic programming: dp[i] = min cost to cover first i cows.
For each i, consider a station covering cows j..i-1 with radius (pos[i-1]-pos[j])/2.
Cost = A + B * radius.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N, A, B = map(int, data[:3])
    positions = list(map(int, data[3:3+N]))
    positions.sort()
    # dp[i]: min cost to cover first i cows (positions[0..i-1])
    dp = [float('inf')] * (N+1)
    dp[0] = 0.0
    for i in range(1, N+1):
        # try last station covering cows j..i-1
        for j in range(i):
            radius = (positions[i-1] - positions[j]) / 2.0
            cost = A + B * radius
            total = dp[j] + cost
            if total < dp[i]:
                dp[i] = total
    # output result
    result = dp[N]
    # print as integer if whole, else float
    if abs(result - round(result)) < 1e-9:
        print(int(round(result)))
    else:
        print(result)

if __name__ == '__main__':
    main()
