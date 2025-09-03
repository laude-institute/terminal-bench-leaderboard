#!/usr/bin/env python3
"""
Problem: Count permutations of point insertion so that each new point connects
exactly to three previous points by non-crossing segments.
Solution: Dynamic programming on triangles. For each oriented triangle (i,j,k),
compute f[i][j][k] = number of ways to insert all points inside this triangle
by recursively choosing a point to insert last, splitting the triangle into three.
Answer is sum over all initial triangles of 6 * f[i][j][k] modulo 1e9+7.
"""
import sys
sys.setrecursionlimit(10000)
mod = 10**9+7

def main():
    input = sys.stdin.readline
    N = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(N)]

    # orientation test
    def orient(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

    # Precompute which points lie strictly inside each oriented triangle
    inside = [[ [ [] for _ in range(N) ] for __ in range(N) ] for ___ in range(N)]
    for i in range(N):
        for j in range(N):
            if j==i: continue
            for k in range(N):
                if k==i or k==j: continue
                if orient(pts[i], pts[j], pts[k]) <= 0:
                    continue
                lst = []
                for p in range(N):
                    if p==i or p==j or p==k: continue
                    # point p is inside triangle i,j,k if it is on same side of all edges
                    if orient(pts[i], pts[j], pts[p]) > 0 and \
                       orient(pts[j], pts[k], pts[p]) > 0 and \
                       orient(pts[k], pts[i], pts[p]) > 0:
                        lst.append(p)
                inside[i][j][k] = lst

    # factorials for combinations
    fact = [1]*(N+1)
    inv = [1]*(N+1)
    for i in range(1, N+1): fact[i] = fact[i-1]*i % mod
    inv[N] = pow(fact[N], mod-2, mod)
    for i in range(N, 0, -1): inv[i-1] = inv[i]*i % mod
    def comb(n, k):
        if k<0 or k>n: return 0
        return fact[n]*inv[k]%mod*inv[n-k]%mod

    # DP memo
    dp = {}
    def dfs(i, j, k):
        key = (i,j,k)
        if key in dp:
            return dp[key]
        pts_inside = inside[i][j][k]
        m = len(pts_inside)
        if m == 0:
            dp[key] = 1
            return 1
        total = 0
        # choose last insertion point p among pts_inside
        for idx, p in enumerate(pts_inside):
            # compute subtriangle counts
            a = dfs(i, j, p)
            b = dfs(j, k, p)
            c = dfs(k, i, p)
            # partition remaining points among subtriangles
            s1 = s2 = s3 = 0
            for q in pts_inside:
                if q == p: continue
                if orient(pts[i], pts[j], pts[q]) > 0 and orient(pts[j], pts[p], pts[q]) > 0 and orient(pts[p], pts[i], pts[q]) > 0:
                    s1 += 1
                elif orient(pts[j], pts[k], pts[q]) > 0 and orient(pts[k], pts[p], pts[q]) > 0 and orient(pts[p], pts[j], pts[q]) > 0:
                    s2 += 1
                else:
                    s3 += 1
            # multinomial: choose positions for s1, s2, s3 in any order
            ways = comb(m-1, s1) * comb(m-1-s1, s2) % mod
            total = (total + a * b % mod * c % mod * ways) % mod
        dp[key] = total
        return total

    # sum over all initial oriented triangles
    ans = 0
    for i in range(N):
        for j in range(N):
            if j==i: continue
            for k in range(N):
                if k==i or k==j: continue
                if orient(pts[i], pts[j], pts[k]) > 0:
                    ans = (ans + dfs(i, j, k)) % mod
    # multiply by 6 for permutations of first three
    ans = ans * 6 % mod
    print(ans)

if __name__ == '__main__':
    main()
