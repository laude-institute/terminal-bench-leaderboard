#!/usr/bin/env python3
"""
Compute number of non-decreasing subsequences for subarray queries.
Segment tree over transition matrices of size (K+1)x(K+1).
"""
import sys

def main():
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    A = [0] + [int(next(it)) for _ in range(N)]
    Q = int(next(it))
    MOD = 10**9 + 7

    # Build transition matrix for value x
    def make_M(x):
        # M is (K+1)x(K+1)
        M = [[0] * (K+1) for _ in range(K+1)]
        # dp[0] stays constant
        M[0][0] = 1
        # for all other j!=x, carry over
        for j in range(1, K+1):
            if j != x:
                M[j][j] = 1
        # for x, dp'[x] = dp[x] + sum(dp[0..x])
        # sum(dp[0..x]) = sum of dp[u] for u in 0..x
        for u in range(0, x+1):
            M[x][u] = (M[x][u] + 1) % MOD
        # add carry of old dp[x]
        M[x][x] = (M[x][x] + 1) % MOD
        return M

    # Matrix multiplication
    def mat_mul(A_mat, B_mat):
        # (K+1)x(K+1) times (K+1)x(K+1)
        C = [[0] * (K+1) for _ in range(K+1)]
        for i in range(K+1):
            Ai = A_mat[i]
            Ci = C[i]
            for k in range(K+1):
                v = Ai[k]
                if v:
                    Bk = B_mat[k]
                    for j in range(K+1):
                        Ci[j] = (Ci[j] + v * Bk[j]) % MOD
        return C

    # Build segment tree
    size = 1
    while size < N:
        size <<= 1
    tree = [None] * (2 * size)
    # leaves
    for i in range(N):
        tree[size + i] = make_M(A[i+1])
    for i in range(N, size):
        # identity matrix
        I = [[0] * (K+1) for _ in range(K+1)]
        for j in range(K+1): I[j][j] = 1
        tree[size + i] = I
    # internal nodes
    for i in range(size - 1, 0, -1):
        # right child times left child
        tree[i] = mat_mul(tree[2*i+1], tree[2*i])

    out = []
    # process queries
    for _ in range(Q):
        l = int(next(it))-1
        r = int(next(it))-1
        # query segment tree for [l, r]
        # initialize left and right accumulators as identity
        left_mat = [[0] * (K+1) for _ in range(K+1)]
        right_mat = [[0] * (K+1) for _ in range(K+1)]
        for j in range(K+1):
            left_mat[j][j] = 1
            right_mat[j][j] = 1
        l += size; r += size
        while l <= r:
            if l & 1:
                left_mat = mat_mul(tree[l], left_mat)
                l += 1
            if not r & 1:
                right_mat = mat_mul(right_mat, tree[r])
                r -= 1
            l >>= 1; r >>= 1
        M = mat_mul(right_mat, left_mat)
        # result is sum of first column
        ans = 0
        for i in range(K+1): ans = (ans + M[i][0]) % MOD
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
