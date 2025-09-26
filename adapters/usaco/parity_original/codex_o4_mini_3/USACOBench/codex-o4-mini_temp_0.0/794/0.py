#!/usr/bin/env python3
import sys
def main():
    import sys
    data = sys.stdin
    M = 10**9 + 7
    inv2 = (M + 1) // 2
    N = int(data.readline())
    a = [0] * N
    for _ in range(N):
        i, j = map(int, data.readline().split())
        a[i] = j

    # Precompute W and F
    W = [0] * N
    F = [0] * N
    W[0] = a[0]
    for i in range(1, N):
        W[i] = min(W[i-1], a[i])
    F[N-1] = a[N-1]
    for i in range(N-2, -1, -1):
        F[i] = max(F[i+1], a[i])

    # Fenwick trees for count, sum, sum of squares
    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.f = [0] * (n+1)
        def add(self, i, v):
            i += 1
            while i <= self.n:
                self.f[i] = (self.f[i] + v) % M
                i += i & -i
        def sum(self, i):
            # sum [0..i]
            i += 1
            s = 0
            while i > 0:
                s = (s + self.f[i]) % M
                i -= i & -i
            return s
        def range_sum(self, l, r):
            if r < l:
                return 0
            res = self.sum(r) - (self.sum(l-1) if l>0 else 0)
            return res % M

    # initialize Fenwicks
    cnt = Fenwick(N)
    s1 = Fenwick(N)
    s2 = Fenwick(N)

    ans = 0
    # iterate r, adding W[r-1] then computing contribution for F[r]
    for r in range(1, N):
        wv = W[r-1]
        cnt.add(wv, 1)
        s1.add(wv, wv)
        s2.add(wv, wv * wv % M)
        v = F[r]
        if v > 0:
            m = cnt.range_sum(0, v-1)
            sum_w = s1.range_sum(0, v-1)
            sum_w2 = s2.range_sum(0, v-1)
            # compute numerator = m*v*(v+1) - sum_w*(2*v+1) + sum_w2
            term = (m * v % M * (v+1) % M - sum_w * (2*v+1) % M + sum_w2) % M
            ans = (ans + term * inv2) % M
    print(ans)

if __name__ == '__main__':
    main()
