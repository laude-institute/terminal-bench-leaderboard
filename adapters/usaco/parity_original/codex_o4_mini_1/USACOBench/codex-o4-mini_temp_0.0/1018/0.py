#!/usr/bin/env python3
"""
Compute sum of complexities (number of union segments) over all subsets of given segments.
"""
import sys

def main():
    input = sys.stdin.readline
    mod = 10**9 + 7
    N = int(input())
    segs = []
    coords = []
    for _ in range(N):
        l, r = map(int, input().split())
        segs.append((l, r))
        coords.append(l)
        coords.append(r)
    # Coordinate compression
    coords.sort()
    comp = {v: i for i, v in enumerate(coords)}
    M = len(coords)
    # Number of atomic blocks is M-1
    B = M - 1
    # Difference arrays for cover counts and overlaps
    cover_diff = [0] * (M + 1)
    overlap_diff = [0] * (M + 1)
    for l, r in segs:
        li = comp[l]
        ri = comp[r]
        # segment covers blocks [li, ri-1]
        cover_diff[li] += 1
        cover_diff[ri] -= 1
        # segment covers both j-1 and j for j in [li+1..ri-1]
        if ri - li >= 2:
            overlap_diff[li + 1] += 1
            overlap_diff[ri] -= 1
    # Build prefix sums
    cover = [0] * B
    overlap = [0] * (M + 1)
    cur = 0
    for i in range(M):
        cur += cover_diff[i]
        if i < B:
            cover[i] = cur
    cur = 0
    for i in range(M):
        cur += overlap_diff[i]
        overlap[i] = cur
    # Precompute powers of two
    pow2 = [1] * (N + 1)
    for i in range(1, N + 1):
        pow2[i] = pow2[i - 1] * 2 % mod
    # Sum contributions
    ans = 0
    # For first block j=0
    c0 = cover[0] if B > 0 else 0
    if c0 > 0:
        ans = (ans + pow2[N] - pow2[N - c0]) % mod
    # For other blocks j=1..B-1
    for j in range(1, B):
        cj = cover[j]
        cjm1 = cover[j - 1]
        ov = overlap[j]
        # union size of A_j and A_{j-1}
        union = cj + cjm1 - ov
        # add subsets avoiding A_{j-1} but picking ≥1 from A_j
        ans = (ans + (pow2[N - cjm1] - pow2[N - union])) % mod
    print(ans)

if __name__ == '__main__':
    main()
