#!/usr/bin/env python3
"""
Problem: Fair Photography
Given N cows at distinct positions on a line, each white (W) or spotted (S).
We may paint any white cows to spotted to achieve equal counts of white and spotted
in a contiguous photo. Find the maximum position span of such a photo.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cows = []
    # parse positions and types
    for i in range(n):
        x = int(data[1 + 2*i])
        t = data[2 + 2*i]
        cows.append((x, t))
    # sort by position
    cows.sort(key=lambda c: c[0])
    xs = [cows[i][0] for i in range(n)]
    # build prefix sum P: P[0]=0, P[i]=sum of deltas up to cow i-1
    P = [0] * (n + 1)
    for i in range(1, n+1):
        delta = 1 if cows[i-1][1] == 'W' else -1
        P[i] = P[i-1] + delta

    ans = 0
    # process both parity classes separately
    for parity in (0, 1):
        stack = []  # will hold candidate start indices i (0 <= i < n)
        # build decreasing stack of P[i]
        for i in range(n):
            if P[i] % 2 == parity:
                if not stack or P[i] < P[stack[-1]]:
                    stack.append(i)
        # scan end indices j from n down to 1
        for j in range(n, 0, -1):
            if P[j] % 2 == parity:
                # while any start i with P[j] >= P[i]
                while stack and P[j] >= P[stack[-1]]:
                    i = stack.pop()
                    # interval from i..j-1
                    # ensure valid interval
                    if j-1 >= i:
                        span = xs[j-1] - xs[i]
                        if span > ans:
                            ans = span
    # output result
    print(ans)

if __name__ == '__main__':
    main()
