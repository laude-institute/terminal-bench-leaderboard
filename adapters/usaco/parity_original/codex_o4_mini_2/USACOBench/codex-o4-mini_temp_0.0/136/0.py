#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N, L, C = map(int, data[:3])
    speeds = list(map(int, data[3:3+N]))
    vmax = max(speeds)
    speeds.sort()

    # Compute ai = floor(si * L / vmax) and bi = (si * L) % vmax
    ai = [(s * L) // vmax for s in speeds]
    bi = [(s * L) % vmax for s in speeds]

    # Sum over pairs of (ai - aj)
    # sum1 = sum_i ai * (# js < i) - sum_j aj * (# is > j)
    # Leads to sum1 = sum_i ai * (2*i - N + 1)
    sum1 = 0
    for i, a in enumerate(ai):
        sum1 += a * (2 * i - N + 1)

    # Count inversions in bi (pairs j < i with bi[j] > bi[i])
    # Coordinate-compress bi values
    unique_b = sorted(set(bi))
    comp = {v: idx+1 for idx, v in enumerate(unique_b)}
    M = len(unique_b)
    # Fenwick tree for prefix sums
    BIT = [0] * (M + 1)

    def bit_add(idx, val):
        while idx <= M:
            BIT[idx] += val
            idx += idx & -idx

    def bit_sum(idx):
        s = 0
        while idx > 0:
            s += BIT[idx]
            idx -= idx & -idx
        return s

    inv_count = 0
    for i, b in enumerate(bi):
        r = comp[b]
        # number of previous with value <= b
        leq = bit_sum(r)
        # previous count is i
        inv_count += i - leq
        bit_add(r, 1)

    # Total crossing events
    result = sum1 - inv_count
    print(result)

if __name__ == '__main__':
    main()
