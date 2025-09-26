#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    p = [int(next(it)) for _ in range(n)]
    # find longest strictly increasing suffix
    m = n - 1
    while m > 0 and p[m-1] < p[m]:
        m -= 1
    # m is start index of suffix (0-based)
    K = m
    # Binary Indexed Tree for frequencies of values 1..n
    size = n + 2
    bit = [0] * size

    def bit_add(i, v=1):
        # add v at index i
        while i < size:
            bit[i] += v
            i += i & -i

    def bit_sum(i):
        # sum from 1 to i
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    # initialize BIT with suffix elements
    for x in p[m:]:
        bit_add(x, 1)

    res = []
    # process prefix elements
    for i in range(K):
        x = p[i]
        # count of suffix elements less than x
        j = bit_sum(x - 1)
        # number of remaining prefix elements after removing current = K - i - 1
        k = (K - i - 1) + j
        res.append(str(k))
        bit_add(x, 1)

    # output
    out = []
    out.append(str(K))
    if K > 0:
        out.append(" ".join(res))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
