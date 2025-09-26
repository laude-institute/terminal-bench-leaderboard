#!/usr/bin/env python3
"""
Solution for counting ordered pairs of intervals whose sum ranges cover each k.
Approach: use convolution on interval endpoints counts.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    # Frequency of interval start and end points
    f = [0] * (M + 1)
    g = [0] * (M + 1)
    idx = 2
    for _ in range(N):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        f[a] += 1
        g[b] += 1
    size = 2 * M + 1
    # Convolution arrays: counts of sums exactly equal to s
    h_a = [0] * size
    h_b = [0] * size
    # Compute convolution for starts
    for i in range(M + 1):
        fi = f[i]
        if fi:
            for j in range(M + 1):
                h_a[i + j] += fi * f[j]
    # Compute convolution for ends
    for i in range(M + 1):
        gi = g[i]
        if gi:
            for j in range(M + 1):
                h_b[i + j] += gi * g[j]
    # Prefix sums
    for k in range(1, size):
        h_a[k] += h_a[k-1]
        h_b[k] += h_b[k-1]
    # Compute results: pairs with a_sum <= k minus pairs with b_sum < k
    out = []
    for k in range(size):
        less_b = h_b[k-1] if k > 0 else 0
        out.append(str(h_a[k] - less_b))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
