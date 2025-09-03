#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    b = list(map(int, data[1:]))
    # compute previous occurrence
    prev = [-1] * n
    last = {}
    for i in range(n):
        prev[i] = last.get(b[i], -1)
        last[b[i]] = i
    # compute next occurrence
    next_occ = [n] * n
    last.clear()
    for i in range(n-1, -1, -1):
        next_occ[i] = last.get(b[i], n)
        last[b[i]] = i

    # buckets for prev values: bucket[p+1] holds indices i with prev[i] == p
    buckets = [[] for _ in range(n+1)]
    for i in range(n):
        buckets[prev[i] + 1].append(i)

    # Fenwick Tree (1-indexed)
    class BIT:
        def __init__(self, size):
            self.n = size
            self.fw = [0] * (size + 1)
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

    bit = BIT(n)
    ans = 0
    # sweep l from 0 to n-1
    for l in range(n):
        # activate positions r with prev[r] == l-1
        for r in buckets[l]:
            # BIT is 1-indexed
            bit.add(r+1, 1)
        # count r in (l, next_occ[l])
        right = next_occ[l] - 1
        if right > l:
            total = bit.sum(right+1) - bit.sum(l+1)
            ans += total
    # output result
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
