#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    segs = []
    # read segments
    for _ in range(n):
        l = int(next(it))
        r = int(next(it))
        segs.append((l, r))
    # sort by left endpoint
    segs.sort(key=lambda x: x[0])
    # BIT over right endpoints (1..2n)
    size = 2 * n + 5
    bit = [0] * (size)

    def bit_add(i, v):  # add v at position i
        while i < size:
            bit[i] += v
            i += i & -i

    def bit_sum(i):  # sum from 1 to i
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    MOD = 10**9 + 7
    # precompute powers of 2
    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow2[i] = pow2[i-1] * 2 % MOD

    ans = 0
    # process segments
    for l, r in segs:
        # count prior segments with r_j >= l
        total_prior = bit_sum(size - 1)
        less = bit_sum(l - 1)
        c = total_prior - less
        exp = n - 1 - c
        ans = (ans + pow2[exp]) % MOD
        # include this segment
        bit_add(r, 1)

    print(ans)


if __name__ == '__main__':
    main()
