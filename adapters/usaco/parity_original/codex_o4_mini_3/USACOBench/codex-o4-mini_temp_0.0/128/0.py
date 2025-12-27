#!/usr/bin/env python3
"""
Solution to Haybale Restacking problem (circular arrangement).
Computes minimal work to transform current piles A into target piles B.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    # Compute differences A_i - B_i
    diffs = [0] * n
    for i in range(n):
        a = int(next(it))
        b = int(next(it))
        diffs[i] = a - b

    # Build prefix sums of differences
    prefix_sums = [0] * n
    cum = 0
    for i, d in enumerate(diffs):
        cum += d
        prefix_sums[i] = cum

    # On a circle, optimal origin shift is median of prefix sums
    prefix_sums.sort()
    median = prefix_sums[n // 2]

    # Total work is sum of absolute deviations from median
    total_work = sum(abs(x - median) for x in prefix_sums)
    print(total_work)

if __name__ == '__main__':
    main()
