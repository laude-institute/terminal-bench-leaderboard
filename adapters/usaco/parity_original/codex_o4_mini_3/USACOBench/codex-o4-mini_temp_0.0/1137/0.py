#!/usr/bin/env python3
"""
Solution for UCFJ delegation selection problem.
"""
import sys

def main():
    input = sys.stdin.readline
    N_line = input()
    if not N_line:
        return
    N = int(N_line)
    b = list(map(int, input().split()))
    # Compute previous occurrence for each position
    prev = [0] * N
    last_occ = {}
    for i in range(N):
        prev[i] = last_occ.get(b[i], -1)
        last_occ[b[i]] = i
    # Compute next occurrence for each position
    next_pos = [0] * N
    last_occ.clear()
    for i in range(N - 1, -1, -1):
        next_pos[i] = last_occ.get(b[i], N)
        last_occ[b[i]] = i

    # Prepare removal events when r reaches next_pos[l]
    events = [[] for _ in range(N)]
    for l in range(N):
        t = next_pos[l]
        if t < N:
            events[t].append(l)

    # Fenwick tree for active l positions
    class Fenwick:
        def __init__(self, size):
            self.n = size
            self.f = [0] * (size + 1)

        def add(self, idx, val):  # idx: 0-based
            i = idx + 1
            while i <= self.n:
                self.f[i] += val
                i += i & -i

        def prefix_sum(self, i):  # sum of [0..i-1]
            s = 0
            while i > 0:
                s += self.f[i]
                i -= i & -i
            return s

        def range_sum(self, l, r):  # inclusive l..r
            return self.prefix_sum(r + 1) - self.prefix_sum(l)

    bit = Fenwick(N)
    # Initially all positions l are active
    for i in range(N):
        bit.add(i, 1)

    result = 0
    # Sweep r from 0 to N-1
    for r in range(N):
        # Remove l where next_pos[l] == r
        for l in events[r]:
            bit.add(l, -1)
        if r == 0:
            continue
        lo = prev[r] + 1
        hi = r - 1
        if lo <= hi:
            result += bit.range_sum(lo, hi)

    print(result)

if __name__ == '__main__':
    main()
