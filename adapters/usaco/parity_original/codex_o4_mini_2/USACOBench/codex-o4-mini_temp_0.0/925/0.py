#!/usr/bin/env python3
import sys
from collections import deque, defaultdict
MOD = 10**9+7

def main():
    input = sys.stdin.readline
    N, M, X, Y = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b, d = map(int, input().split())
        a -= 1; b -= 1
        adj[a].append((b, d))
        adj[b].append((a, d))
    # find components
    vis = [False]*N
    comps = []
    for i in range(N):
        if not vis[i]:
            q = [i]; vis[i]=True; comp=[i]
            for u in q:
                for v,_ in adj[u]:
                    if not vis[v]: vis[v]=True; q.append(v); comp.append(v)
            comps.append(comp)
    K = len(comps)
    # for each comp, get distance freq f_i
    dist_lists = []
    for comp in comps:
        f = defaultdict(int)
        for u in comp:
            # BFS from u
            dist = {u:0}
            dq = deque([u])
            while dq:
                x = dq.popleft()
                for v,w in adj[x]:
                    if v not in dist:
                        dist[v] = dist[x]+w
                        dq.append(v)
            for v, d in dist.items():
                if v!=u:
                    f[d] += 1
        dist_lists.append(f)
    # DP over components
    # dp_count[s], dp_sum[s]
    dp_count = {0:1}
    dp_sum = {0:0}
    for f in dist_lists:
        new_count = defaultdict(int)
        new_sum = defaultdict(int)
        for s,c in dp_count.items():
            sd = dp_sum[s]
            for d,fc in f.items():
                ns = s + d
                ways = c * fc % MOD
                new_count[ns] = (new_count[ns] + ways) % MOD
                # sum of dists: previous distances sum + new d added per way
                new_sum[ns] = (new_sum[ns] + sd * fc + c * fc % MOD * d) % MOD
        dp_count, dp_sum = new_count, new_sum
    # accumulate totals for internal sum >= Y-KX
    threshold = Y - K*X
    total_cnt = 0
    total_dsum = 0
    for s, c in dp_count.items():
        if s >= threshold:
            total_cnt = (total_cnt + c) % MOD
            total_dsum = (total_dsum + dp_sum[s]) % MOD
    # add K*X per configuration
    total = (total_dsum + total_cnt * (K*X % MOD)) % MOD
    # number of cycles on K components
    if K == 1:
        cyc = 1
    else:
        # (K-1)!/2
        fact = 1
        for i in range(1, K): fact = fact * i % MOD
        inv2 = (MOD+1)//2
        cyc = fact * inv2 % MOD
    ans = total * cyc % MOD
    print(ans)

if __name__=='__main__':
    main()
