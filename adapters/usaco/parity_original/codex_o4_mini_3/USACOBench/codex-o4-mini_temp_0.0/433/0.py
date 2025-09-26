#!/usr/bin/env python3
import sys
from bisect import bisect_right

def main():
    input = sys.stdin.readline
    N = int(input())
    cows = []
    for _ in range(N):
        x, c = input().split()
        cows.append((int(x), c))
    # sort by position
    cows.sort()
    X = [pos for pos, _ in cows]
    # white=1, spotted=-1
    A = [1 if c == 'W' else -1 for _, c in cows]
    # prefix sums
    P = [0] * (N + 1)
    for i in range(1, N + 1):
        P[i] = P[i - 1] + A[i - 1]

    # for each parity, keep candidates with strictly decreasing P[k]
    S_par = {0: [], 1: []}
    V_par = {0: [], 1: []}
    # include prefixes k = 0..N-1
    for k in range(N):
        par = P[k] & 1
        if not V_par[par] or P[k] < V_par[par][-1]:
            S_par[par].append(k)
            V_par[par].append(P[k])

    ans = 0
    # for each end prefix r, find earliest k with same parity and P[k] <= P[r]
    for r in range(1, N + 1):
        par = P[r] & 1
        S = S_par[par]
        V = V_par[par]
        # only consider k <= r-1
        hi_idx = bisect_right(S, r - 1) - 1
        if hi_idx < 0:
            continue
        target = P[r]
        # binary search first index i in [0..hi_idx] with V[i] <= target
        lo, hi2 = 0, hi_idx
        idx = -1
        while lo <= hi2:
            mid = (lo + hi2) // 2
            if V[mid] <= target:
                idx = mid
                hi2 = mid - 1
            else:
                lo = mid + 1
        if idx != -1:
            k = S[idx]
            # interval from cow k to cow r-1
            size = X[r - 1] - X[k]
            if size > ans:
                ans = size

    print(ans)

if __name__ == "__main__":
    main()
