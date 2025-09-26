#!/usr/bin/env python3
"""
Solution for "Haybale Stacking" problem.
Reads N stacks and K range-adding instructions, computes median stack height.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    # difference array to accumulate range updates
    diff = [0] * (N + 2)
    idx = 2
    for _ in range(K):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        diff[a] += 1
        diff[b+1] -= 1
    # counts of heights (max height <= K)
    counts = [0] * (K + 1)
    curr = 0
    for i in range(1, N+1):
        curr += diff[i]
        # curr is the height of stack i
        counts[curr] += 1
    # target position for median (1-based)
    target = (N + 1) // 2
    cum = 0
    # iterate possible heights from 0..K
    for h in range(K + 1):
        cum += counts[h]
        if cum >= target:
            sys.stdout.write(str(h))
            return

if __name__ == '__main__':
    main()
