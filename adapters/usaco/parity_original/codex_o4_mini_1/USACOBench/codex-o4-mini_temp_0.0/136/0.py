#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    L = int(next(it))
    C = int(next(it))  # unused after cancellation
    speeds = [int(next(it)) for _ in range(n)]
    # sort speeds
    speeds.sort()
    vmax = speeds[-1]
    # compute Qi and Ri for each speed
    # Bi = speed * L, Qi = Bi // vmax, Ri = Bi % vmax
    B = [s * L for s in speeds]
    Q = [b // vmax for b in B]
    R = [b % vmax for b in B]
    # coordinate compress R values
    unique_R = sorted(set(R))
    comp = {v: i for i, v in enumerate(unique_R)}
    m = len(unique_R)
    # Fenwick tree for counts of R
    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.fw = [0] * (n+1)
        def add(self, i, v):
            i += 1
            while i <= self.n:
                self.fw[i] += v
                i += i & -i
        def sum(self, i):
            # sum of [0..i)
            s = 0
            while i > 0:
                s += self.fw[i]
                i -= i & -i
            return s
        def range_sum(self, l, r):
            return self.sum(r) - self.sum(l)

    bit = Fenwick(m)
    ans = 0
    prefix_Q = 0
    # iterate through sorted speeds
    for i in range(n):
        qi = Q[i]
        ri = R[i]
        idx = comp[ri]
        # count of previous j is i
        # count of Rj <= ri is bit.sum(idx+1)
        le = bit.sum(idx+1)
        gt = i - le
        ans += i * qi - prefix_Q - gt
        # update
        prefix_Q += qi
        bit.add(idx, 1)
    # output result
    print(ans)

if __name__ == '__main__':
    main()
