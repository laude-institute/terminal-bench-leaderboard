#!/usr/bin/env python3
"""
Sleepy Cow Sorting solution.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    p = list(map(int, input().split()))
    # find longest increasing suffix
    m = N - 1
    while m > 0 and p[m-1] < p[m]:
        m -= 1
    K = m
    # output number of moves
    print(K)
    if K == 0:
        return
    # Fenwick tree for counting suffix elements
    class BIT:
        def __init__(self, n):
            self.n = n
            self.fw = [0] * (n + 1)
        def add(self, i, v):
            while i <= self.n:
                self.fw[i] += v
                i += i & -i
        def sum(self, i):
            s = 0
            while i > 0:
                s += self.fw[i]
                i -= i & -i
            return s
    bit = BIT(N)
    # initialize with suffix elements
    for i in range(m, N):
        bit.add(p[i], 1)
    res = []
    # process prefix cows
    for i in range(K):
        x = p[i]
        # count suffix elements less than x
        idx = bit.sum(x - 1)
        # skip unprocessed prefix (K-i-1) and idx suffix
        k_i = (K - (i + 1)) + idx
        res.append(str(k_i))
        bit.add(x, 1)
    print(" ".join(res))

if __name__ == '__main__':
    main()
