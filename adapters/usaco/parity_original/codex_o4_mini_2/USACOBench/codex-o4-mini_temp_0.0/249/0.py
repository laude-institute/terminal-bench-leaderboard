#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    r = int(next(it))
    L = [0] * (n + 1)
    R = [0] * (m + 1)
    for i in range(1, n + 1):
        L[i] = int(next(it))
    for j in range(1, m + 1):
        R[j] = int(next(it))
    edges = []
    for _ in range(r):
        i = int(next(it))
        j = int(next(it))
        edges.append((i, j))
    # Sort edges by left index then right index
    edges.sort()
    # best_l[i]: max DP_l for left node i
    # best_r[j]: max DP_r for right node j
    best_l = [0] * (n + 1)
    best_r = [0] * (m + 1)
    ans = 0
    # DP over edges
    for i, j in edges:
        # DP_r: end at R[j], last move L->R
        dp_r = L[i] + R[j]
        if best_l[i] > 0:
            dp_r = max(dp_r, best_l[i] + R[j])
        # DP_l: end at L[i], last move R->L
        dp_l = L[i] + R[j]
        if best_r[j] > 0:
            dp_l = max(dp_l, best_r[j] + L[i])
        # update best and answer
        best_l[i] = max(best_l[i], dp_l)
        best_r[j] = max(best_r[j], dp_r)
        ans = max(ans, dp_r, dp_l)
    # If no routes, take best single site
    if r == 0:
        ans = max(max(L[1:]), max(R[1:]))
    print(ans)

if __name__ == '__main__':
    main()
