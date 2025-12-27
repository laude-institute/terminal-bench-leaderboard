#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    cows = []
    for _ in range(N):
        x, y = map(int, input().split())
        cows.append((x, y))
    # Sort by x-coordinate
    cows.sort(key=lambda p: p[0])
    # Extract y-values and rank them 1..N
    ys = [y for _, y in cows]
    sorted_ys = sorted(ys)
    rank = {v: i+1 for i, v in enumerate(sorted_ys)}
    A = [rank[y] for y in ys]

    # Fenwick/BIT for prefix counts
    class BIT:
        __slots__ = ('n', 't')
        def __init__(self, n):
            self.n = n
            self.t = [0] * (n+1)
        def add(self, i, v):
            while i <= self.n:
                self.t[i] += v
                i += i & -i
        def sum(self, i):
            s = 0
            while i > 0:
                s += self.t[i]
                i -= i & -i
            return s

    result = 0
    # Enumerate strips [i..j] by x-order
    for j in range(N):
        bit = BIT(N)
        # Expand strip backwards from j to 0
        for i in range(j, -1, -1):
            ai = A[i]
            bit.add(ai, 1)
            aj = A[j]
            # position of ai among A[i..j]
            pos_i = bit.sum(ai - 1) + 1
            # position of aj among A[i..j]
            pos_j = bit.sum(aj - 1) + 1
            m = j - i + 1
            low = pos_i if pos_i < pos_j else pos_j
            high = pos_j if pos_i < pos_j else pos_i
            # number of y-intervals covering both ends
            result += low * (m - high + 1)
    # include empty subset
    result += 1
    print(result)

if __name__ == '__main__':
    main()
