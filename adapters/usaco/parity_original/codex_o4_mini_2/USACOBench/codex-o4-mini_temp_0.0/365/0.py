#!/usr/bin/env python3
import sys

def main():
    import sys
    data = sys.stdin
    # read N and D
    N, D = map(int, data.readline().split())
    # read initial machine outputs
    M = [int(data.readline()) for _ in range(N)]
    # build segment tree size
    S = 1
    while S < N:
        S <<= 1
    # define negative infinity for max-plus
    NEG_INF = -10**30
    # function to create leaf matrix for a machine
    def make_matrix(m):
        # rows: prev state 0/1, cols: curr state 0/1
        return [[0, m], [0, NEG_INF]]
    # identity matrix in max-plus
    ID = [[0, NEG_INF], [NEG_INF, 0]]
    # initialize tree with identity
    tree = [ID[:] for _ in range(2 * S)]
    # set leaves
    for i in range(S):
        idx = S + i
        if i < N:
            tree[idx] = make_matrix(M[i])
        else:
            tree[idx] = [row[:] for row in ID]
    # matrix multiplication in max-plus semiring
    def mul(A, B):
        return [
            [max(A[0][0] + B[0][0], A[0][1] + B[1][0]),
             max(A[0][0] + B[0][1], A[0][1] + B[1][1])],
            [max(A[1][0] + B[0][0], A[1][1] + B[1][0]),
             max(A[1][0] + B[0][1], A[1][1] + B[1][1])]
        ]
    # build internal nodes
    for i in range(S - 1, 0, -1):
        tree[i] = mul(tree[2 * i], tree[2 * i + 1])
    total = 0
    # process each day: update and query
    for _ in range(D):
        line = data.readline().split()
        if not line:
            break
        p, m = map(int, line)
        p -= 1  # zero-index
        # update leaf
        idx = S + p
        tree[idx] = make_matrix(m)
        # update ancestors
        idx //= 2
        while idx:
            tree[idx] = mul(tree[2 * idx], tree[2 * idx + 1])
            idx //= 2
        # query root matrix
        root = tree[1]
        # final state is initial [0,-inf] * root => take row 0
        day_max = max(root[0][0], root[0][1])
        total += day_max
    # output total milk
    print(total)

if __name__ == '__main__':
    main()
