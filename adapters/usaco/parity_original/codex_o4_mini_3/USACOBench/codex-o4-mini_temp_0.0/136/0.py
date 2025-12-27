#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    L = int(data[1])
    # C is unused in computation (cancels out)
    speeds = list(map(int, data[3:]))
    vmax = max(speeds)
    # Compute q and r for each cow
    qr = []  # list of (q, r)
    for v in speeds:
        total = v * L
        q = total // vmax
        r = total % vmax
        qr.append((q, r, v))
    # Sort by speed
    qr.sort(key=lambda x: x[2])
    # Separate lists
    Q = [x[0] for x in qr]
    R = [x[1] for x in qr]
    # Compute sum1 = sum_{i}(i*Q[i] - sum_Q_before)
    total1 = 0
    sum_q = 0
    for i, q in enumerate(Q):
        total1 += i * q - sum_q
        sum_q += q
    # Count inversions in R using Fenwick Tree
    size = vmax + 2
    fenw = [0] * size
    def fenw_add(i, v):
        while i < size:
            fenw[i] += v
            i += i & -i
    def fenw_sum(i):
        s = 0
        while i > 0:
            s += fenw[i]
            i -= i & -i
        return s
    inv = 0
    for i, r in enumerate(R):
        idx = r + 1
        # number of previous with r_j > r_i
        inv += i - fenw_sum(idx)
        fenw_add(idx, 1)
    result = total1 - inv
    print(result)

if __name__ == '__main__':
    main()
