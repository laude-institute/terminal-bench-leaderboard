#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    T = int(next(it))
    A = [int(next(it)) for _ in range(K)]
    # Build function f: u -> f(u)
    # Default: u -> (u-1) mod N
    f = [(i-1) % N for i in range(N)]
    # Active overrides: for each A[i] -> (A[i+1]-1) mod N
    for i in range(K):
        cur = A[i]
        nxt = A[(i+1) % K]
        f[cur] = (nxt - 1) % N

    # Binary lifting via doubling without full table
    # cur_f holds f^{2^k}
    cur_f = f[:]  # f^{1}
    # u[j] will be f^T(j)
    u = list(range(N))
    t = T
    while t > 0:
        if t & 1:
            # apply cur_f to all u
            u = [cur_f[x] for x in u]
        # square cur_f: f^{2^{k+1}}(x) = cur_f[cur_f[x]]
        cur_f = [cur_f[cur_f[x]] for x in range(N)]
        t >>= 1

    # Compute final positions: pos = (u + T) mod N
    Tmod = T % N
    res = [0] * N
    for j in range(N):
        pos = u[j] + Tmod
        if pos >= N:
            pos %= N
        res[pos] = j
    # Output
    out = ' '.join(str(res[i]) for i in range(N))
    sys.stdout.write(out)

if __name__ == '__main__':
    main()
