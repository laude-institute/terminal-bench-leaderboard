#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
def main():
    MOD = 10**9+7
    input = sys.stdin.readline
    N = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(N)]

    # orientation: cross product of (j-i) x (k-i)
    def orient(i, j, k):
        x1, y1 = pts[i]
        x2, y2 = pts[j]
        x3, y3 = pts[k]
        return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

    # Precompute inside sets and counts for oriented triangles with area > 0
    inside = [[[[] for _ in range(N)] for __ in range(N)] for ___ in range(N)]
    cnt = [[[0]*N for _ in range(N)] for __ in range(N)]
    tris = []
    for i in range(N):
        for j in range(N):
            if j == i: continue
            for k in range(N):
                if k == i or k == j: continue
                if orient(i, j, k) <= 0: continue
                lst = []
                for m in range(N):
                    if m in (i, j, k): continue
                    # m inside triangle i,j,k if orient signs positive
                    if orient(i, j, m) > 0 and orient(j, k, m) > 0 and orient(k, i, m) > 0:
                        lst.append(m)
                inside[i][j][k] = lst
                cnt[i][j][k] = len(lst)
                tris.append((cnt[i][j][k], i, j, k))
    # factorials
    fact = [1]*(N+1)
    invfact = [1]*(N+1)
    for i in range(1, N+1): fact[i] = fact[i-1]*i % MOD
    invfact[N] = pow(fact[N], MOD-2, MOD)
    for i in range(N, 0, -1): invfact[i-1] = invfact[i]*i % MOD

    # DP over triangles
    dp = [[[0]*N for _ in range(N)] for __ in range(N)]
    # sort by increasing interior count
    tris.sort()
    for c, i, j, k in tris:
        if c == 0:
            dp[i][j][k] = 1
        else:
            total = 0
            for m in inside[i][j][k]:
                c1 = cnt[i][j][m]
                c2 = cnt[j][k][m]
                c3 = cnt[k][i][m]
                ways = dp[i][j][m] * dp[j][k][m] % MOD * dp[k][i][m] % MOD
                # interleave other c-1 points among 3 regions
                ways = ways * fact[c-1] % MOD
                ways = ways * invfact[c1] % MOD * invfact[c2] % MOD * invfact[c3] % MOD
                total = (total + ways) % MOD
            dp[i][j][k] = total

    # sum over all initial oriented triangles
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i != j and j != k and i != k and orient(i, j, k) > 0:
                    ans = (ans + dp[i][j][k]) % MOD
    # multiply by 6 for permutations of initial triple
    ans = ans * 6 % MOD
    print(ans)

if __name__ == '__main__':
    main()
