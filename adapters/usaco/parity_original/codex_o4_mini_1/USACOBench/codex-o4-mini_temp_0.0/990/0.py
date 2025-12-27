#!/usr/bin/env python3
"""
Berries problem: maximize berries Bessie can collect
after Elsie takes the K/2 largest baskets.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    B = list(map(int, data[2:]))
    max_b = max(B)
    answer = 0
    # Try every possible basket size b
    for b in range(1, max_b + 1):
        full = []
        leftovers = []
        # Split each tree into as many baskets of size b
        for berries in B:
            cnt = berries // b
            # Only need up to K baskets
            full.extend([b] * min(cnt, K))
            leftovers.append(berries % b)
        # If not enough full baskets, fill with leftovers
        if len(full) < K:
            leftovers.sort(reverse=True)
            full.extend(leftovers[:K - len(full)])
        # Sort baskets descending
        full.sort(reverse=True)
        # Elsie takes first K/2, Bessie takes next K/2
        bessie = sum(full[K//2:K])
        if bessie > answer:
            answer = bessie
    print(answer)

if __name__ == '__main__':
    main()
