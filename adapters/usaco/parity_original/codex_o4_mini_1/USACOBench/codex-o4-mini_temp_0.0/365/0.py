#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    d = int(next(it))
    M = [int(next(it)) for _ in range(n)]
    # Segment tree for max-plus 2x2 matrices
    NEG_INF = -10**30
    # matrix represented as tuple (m00, m01, m10, m11)
    def make_mat(v):
        # T[prev][next]
        return (0, 0, v, NEG_INF)
    def make_id():
        # identity matrix
        return (0, NEG_INF, NEG_INF, 0)
    def combine(a, b):
        a00, a01, a10, a11 = a
        b00, b01, b10, b11 = b
        return (
            max(a00 + b00, a01 + b10),
            max(a00 + b01, a01 + b11),
            max(a10 + b00, a11 + b10),
            max(a10 + b01, a11 + b11),
        )
    # build tree
    size = 1
    while size < n:
        size <<= 1
    tree = [make_id() for _ in range(2 * size)]
    for i in range(n):
        tree[size + i] = make_mat(M[i])
    for i in range(size - 1, 0, -1):
        tree[i] = combine(tree[2*i], tree[2*i + 1])

    total = 0
    # process updates and compute daily max
    for _ in range(d):
        idx = int(next(it)) - 1
        val = int(next(it))
        # update leaf
        pos = size + idx
        tree[pos] = make_mat(val)
        # bubble up
        pos //= 2
        while pos:
            tree[pos] = combine(tree[2*pos], tree[2*pos + 1])
            pos //= 2
        # result is max over initial dp [0, -inf] * full matrix => row 0
        m00, m01, _, _ = tree[1]
        day_best = max(m00, m01)
        total += day_best
    sys.stdout.write(str(total))

if __name__ == '__main__':
    main()
