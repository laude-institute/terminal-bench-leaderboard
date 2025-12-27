#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    d = int(next(it))
    # Read initial machine outputs (1-indexed)
    M = [0] * (n + 1)
    for i in range(1, n + 1):
        M[i] = int(next(it))

    # Segment tree setup for max-plus semiring matrices
    # Matrix is [[-inf, 0], [M[i], 0]] for each machine i
    INF_NEG = -10**30

    # Matrix multiplication in max-plus semiring
    def mat_mult(A, B):
        # C = A * B
        return [
            [max(A[0][0] + B[0][0], A[0][1] + B[1][0]),
             max(A[0][0] + B[0][1], A[0][1] + B[1][1])],
            [max(A[1][0] + B[0][0], A[1][1] + B[1][0]),
             max(A[1][0] + B[0][1], A[1][1] + B[1][1])]
        ]

    # Build segment tree
    size = 1
    while size < n:
        size <<= 1
    # Initialize all nodes to identity-like for max-plus
    # Identity matrix for max-plus: [[0, INF_NEG], [INF_NEG, 0]] maps v->v
    identity = [[0, INF_NEG], [INF_NEG, 0]]
    tree = [identity for _ in range(2 * size)]

    def make_mat(val):
        return [[INF_NEG, 0], [val, 0]]

    # Set leaves
    for i in range(1, n + 1):
        tree[size + i - 1] = make_mat(M[i])
    # Build internal nodes
    for i in range(size - 1, 0, -1):
        tree[i] = mat_mult(tree[2 * i], tree[2 * i + 1])

    # Function to update position i to value val
    def update(i, val):
        pos = size + i - 1
        tree[pos] = make_mat(val)
        pos //= 2
        while pos:
            tree[pos] = mat_mult(tree[2 * pos], tree[2 * pos + 1])
            pos //= 2

    # Function to query current maximum dp[n]
    def query():
        root = tree[1]
        # Applying to initial vector [0,0] gives dp[n] = max(root[1][0], root[1][1])
        return max(root[1][0], root[1][1])

    # Process daily updates and accumulate total milk
    total = 0
    for _ in range(d):
        idx = int(next(it))
        val = int(next(it))
        update(idx, val)
        total += query()

    # Output result
    print(total)

if __name__ == '__main__':
    main()
