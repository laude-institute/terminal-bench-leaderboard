#!/usr/bin/env python3
"""
Solution for goat kart racing problem.
"""
import sys

MOD = 10**9 + 7

def modinv(a):
    return pow(a, MOD-2, MOD)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); M = int(next(it))
    X = int(next(it)); Y = int(next(it))
    # build graph
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u = int(next(it))-1; v = int(next(it))-1; d = int(next(it))
        adj[u].append((v,d))
        adj[v].append((u,d))
    # find components (farms)
    seen = [False]*N
    farms = []  # list of list of nodes
    for i in range(N):
        if not seen[i]:
            # BFS
            stack = [i]; seen[i]=True; comp=[i]
            while stack:
                u = stack.pop()
                for v,_ in adj[u]:
                    if not seen[v]:
                        seen[v] = True; stack.append(v); comp.append(v)
            # only consider components with >=2 nodes
            if len(comp)>=2:
                farms.append(comp)
    K = len(farms)
    # helper: compute all pair distances in tree
    def dist_counts(nodes):
        # returns dict: distance -> count of unordered node pairs with that distance
        dcnt = {}
        for u in nodes:
            # BFS from u
            dist = {u:0}
            stack = [u]
            while stack:
                x = stack.pop()
                for y,w in adj[x]:
                    if y not in dist:
                        dist[y] = dist[x] + w
                        stack.append(y)
            # record for v>u
            for v in nodes:
                if v>u:
                    d = dist[v]
                    dcnt[d] = dcnt.get(d,0) + 1
        return dcnt

    # compute per-farm distance counts
    farm_dcs = [dist_counts(comp) for comp in farms]
    # special case K==1: single farm cycle
    if K == 1:
        dc = farm_dcs[0]
        ans = 0
        for d,c in dc.items():
            L = d + X
            if L >= Y:
                ans = (ans + c * L) % MOD
        print(ans)
        return

    # DP to combine farms: dp[s] = ways
    maxS = max(Y - K*X, 0)
    dp = {0: 1}
    for dc in farm_dcs:
        newdp = {}
        for s, cnt1 in dp.items():
            for d, cnt2 in dc.items():
                ns = s + d
                if ns > maxS: continue
                newdp[ns] = (newdp.get(ns,0) + cnt1 * cnt2) % MOD
        dp = newdp

    # precompute factorials
    fact = [1] * (K+1)
    for i in range(1, K+1): fact[i] = fact[i-1] * i % MOD
    # number of distinct cycles on K labeled items: (K-1)!/2
    cyc = fact[K-1] * modinv(2) % MOD

    ans = 0
    for s, cnt in dp.items():
        total = s + K*X
        if total >= Y:
            # number of tracks for this sum: cnt * cyc
            ways = cnt * cyc % MOD
            ans = (ans + ways * total) % MOD
    print(ans)

if __name__ == '__main__':
    main()
