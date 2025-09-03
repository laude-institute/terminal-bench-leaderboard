#!/usr/bin/env python3
"""
Solution to Haybale Stacking problem (USACO 2012).
Efficiently applies range increments via a difference array,
then counts heights to find the median without full sorting.
"""
import sys

def main():
    data = sys.stdin
    # Read number of stacks N and number of operations K
    N, K = map(int, data.readline().split())
    # Difference array for range updates
    diff = [0] * (N + 2)
    for _ in range(K):
        a, b = map(int, data.readline().split())
        diff[a] += 1
        diff[b + 1] -= 1

    # Frequency of heights (0..K)
    freq = [0] * (K + 1)
    curr = 0
    for i in range(1, N + 1):
        curr += diff[i]
        freq[curr] += 1

    # Find median height: the (N+1)//2-th in sorted order
    target = (N + 1) // 2
    cum = 0
    for h, count in enumerate(freq):
        cum += count
        if cum >= target:
            print(h)
            return

if __name__ == "__main__":
    main()
