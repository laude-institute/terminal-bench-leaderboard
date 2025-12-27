#!/usr/bin/env python3
"""
Python 3 solution for USACO 'odometer' problem.
Counts 'interesting' odometer readings between X and Y.
"""
import sys

def count_interesting_leq(N):
    # Count interesting numbers <= N
    if N <= 9:
        return 0
    S = str(N)
    K = len(S)
    total = 0
    # Count all interesting for lengths less than K
    for L in range(2, K):
        total += 81 * L - 9
    # Count for length exactly K
    for d1 in map(str, range(1, 10)):
        for d2 in map(str, range(0, 10)):
            if d2 == d1:
                continue
            for pos in range(K):
                # Leading zero not allowed
                if pos == 0 and d2 == '0':
                    continue
                # Build candidate with one d2 and rest d1
                candidate = list(d1 * K)
                candidate[pos] = d2
                cand_str = ''.join(candidate)
                if cand_str <= S:
                    total += 1
    return total

def main():
    data = sys.stdin.read().strip().split()
    X, Y = map(int, data)
    # Number of interesting readings in [X, Y]
    result = count_interesting_leq(Y) - count_interesting_leq(X - 1)
    print(result)

if __name__ == '__main__':
    main()
