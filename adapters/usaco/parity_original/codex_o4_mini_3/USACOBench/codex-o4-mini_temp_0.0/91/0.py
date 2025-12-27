#!/usr/bin/env python3
"""
Solution to 'Above the Median'.
Transforms heights to +1/-1 and counts subarrays with non-negative sum
using prefix sums and a Fenwick Tree (BIT).
"""

import sys

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.fw = [0] * (size + 1)

    def update(self, i, v=1):
        # add v at index i (1-based)
        while i <= self.n:
            self.fw[i] += v
            i += i & -i

    def query(self, i):
        # sum from 1 to i (inclusive)
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

def main():
    data = sys.stdin.read().split()
    n, x = map(int, data[:2])
    h = list(map(int, data[2:]))

    # Transform heights: >= x -> +1, else -1
    a = [1 if hi >= x else -1 for hi in h]

    # Build prefix sums
    ps = [0] * (n + 1)
    for i in range(1, n + 1):
        ps[i] = ps[i - 1] + a[i - 1]

    # Coordinate compress prefix sums
    vals = sorted(set(ps))
    comp = {v: i + 1 for i, v in enumerate(vals)}  # 1-based

    # Fenwick tree over compressed coords
    ft = FenwickTree(len(vals))
    result = 0

    # Iterate prefixes: for each ps[i], count how many ps[j] <= ps[i]
    for s in ps:
        idx = comp[s]
        result += ft.query(idx)
        ft.update(idx, 1)

    # Output result
    print(result)

if __name__ == '__main__':
    main()
