#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    b = [int(next(it)) - 1 for _ in range(N)]
    S = [list(next(it).strip()) for _ in range(K)]
    # positions of each breed
    pos = [[] for _ in range(K)]
    for i, bi in enumerate(b):
        pos[bi].append(i)
    # neighbor breeds
    nbr = [[] for _ in range(K)]
    for u in range(K):
        for v in range(K):
            if S[u][v] == '1':
                nbr[u].append(v)
    import heapq
    INF = 10**30
    dist = [INF] * N
    dist[0] = 0
    # intercepts for each target breed
    intercept1 = [INF] * K  # dist[i] + i
    intercept2 = [INF] * K  # dist[i] - i
    dirty = [False] * K
    hq = [(0, 0)]  # (dist, index)
    while hq:
        d, i = heapq.heappop(hq)
        if d != dist[i]:
            continue
        u = b[i]
        changed = []
        # update intercepts for reachable breeds
        for v in nbr[u]:
            old1 = intercept1[v]
            old2 = intercept2[v]
            val1 = d + i
            if val1 < old1:
                intercept1[v] = val1
            val2 = d - i
            if val2 < old2:
                intercept2[v] = val2
            if (intercept1[v] < old1 or intercept2[v] < old2) and not dirty[v]:
                dirty[v] = True
                changed.append(v)
        # process breeds with updated intercepts
        for v in changed:
            for j in pos[v]:
                nd = min(intercept1[v] - j, intercept2[v] + j)
                if nd < dist[j]:
                    dist[j] = nd
                    heapq.heappush(hq, (nd, j))
            dirty[v] = False
    ans = dist[N-1]
    if ans >= INF:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
