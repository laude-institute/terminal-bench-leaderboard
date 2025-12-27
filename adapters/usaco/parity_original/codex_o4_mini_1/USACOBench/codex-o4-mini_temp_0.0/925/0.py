#!/usr/bin/env python3
import sys
from collections import defaultdict, deque

def main():
    MOD = 10**9 + 7
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    X = int(next(it))
    Y = int(next(it))
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        d = int(next(it))
        adj[u].append((v, d))
        adj[v].append((u, d))
    # find components (farms)
    seen = [False]*N
    farms = []  # list of lists of nodes
    for i in range(N):
        if not seen[i]:
            # BFS/DFS
            stack = [i]
            seen[i] = True
            comp = [i]
            while stack:
                u = stack.pop()
                for v, _ in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
                        comp.append(v)
            farms.append(comp)
    K = len(farms)
    # threshold for internal sums
    T = Y - K*X
    if T < 0:
        T = 0

    # per farm: M_i, S_i, and fi(d) map for d < T
    Mi = []  # sum of fi
    Si = []  # sum of fi(d)*d
    fi_list = []  # list of (d, fi_d) for small d

    # compute distances per farm
    for comp in farms:
        n = len(comp)
        # count unordered pair distances
        dist_count = defaultdict(int)
        # for each node, BFS distances
        for u in comp:
            # BFS from u
            dq = deque([(u, 0)])
            vis = {u}
            while dq:
                v, dist = dq.popleft()
                for w, wlen in adj[v]:
                    if w not in vis:
                        vis.add(w)
                        nd = dist + wlen
                        if w > u:
                            dist_count[nd] += 1
                        dq.append((w, nd))
        # compute fi map
        pairs = n*(n-1)//2
        # fi(d) = dist_count[d] * 2
        total_fi = 0
        sum_fi_d = 0
        small = []
        for d, cnt in dist_count.items():
            fi = (cnt * 2) % MOD
            total_fi = (total_fi + fi) % MOD
            sum_fi_d = (sum_fi_d + fi * d) % MOD
            if d < T:
                small.append((d, fi))
        Mi.append(total_fi)
        Si.append(sum_fi_d)
        fi_list.append(small)

    # total_count P and total_sum
    P = 1
    for x in Mi:
        P = P * x % MOD
    # precompute inv of Mi
    inv = [pow(x, MOD-2, MOD) for x in Mi]
    total_sum = 0
    for i in range(K):
        ex = P * inv[i] % MOD
        total_sum = (total_sum + ex * Si[i]) % MOD

    # DP for small sums < T
    small_count = 0
    small_sum = 0
    if T > 0:
        dp_count = [0] * T
        dp_sum = [0] * T
        dp_count[0] = 1
        for small in fi_list:
            new_count = [0] * T
            new_sum = [0] * T
            for s in range(T):
                c = dp_count[s]
                if c:
                    sm = dp_sum[s]
                    for d, fi in small:
                        ns = s + d
                        if ns < T:
                            new_count[ns] = (new_count[ns] + c * fi) % MOD
                            new_sum[ns] = (new_sum[ns] + sm * fi + c * fi * d) % MOD
            dp_count, dp_sum = new_count, new_sum
        small_count = sum(dp_count) % MOD
        small_sum = sum(dp_sum) % MOD
    else:
        # all sums >= 0 covered, none small
        small_count = 0
        small_sum = 0

    # compute counts >= T
    total_count = P
    count_ge = (total_count - small_count) % MOD
    sum_ge = (total_sum - small_sum) % MOD

    # permutations factor: (K-1)! * 2^(K-1)
    fac = 1
    for i in range(1, max(1, K)):
        fac = fac * i % MOD
    pow2 = pow(2, max(0, K-1), MOD)
    perms = fac * pow2 % MOD

    inner = (sum_ge + count_ge * (K * X % MOD)) % MOD
    ans = perms * inner % MOD
    print(ans)

if __name__ == '__main__':
    main()
