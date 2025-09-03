#!/usr/bin/env python3
"""
1. Restate:
   Given N checkpoints and K tickets, each ticket i purchasable at c_i with price p_i grants access to interval [a_i,b_i].
   Starting with only checkpoint i accessible, find minimum total cost to access both checkpoint 1 and N, or -1 if impossible.
2. Solution concept:
   Model ticket purchases as directed edges: buying ticket j gives coverage [a_j,b_j] plus its purchase point, enabling buying any ticket whose c_k is in that coverage.
   Compute for each ticket j the minimum cost d1[j] to reach a ticket covering checkpoint 1, and dN[j] to reach one covering N, both including p_j.
   For a start i, the answer is min over tickets j with c_j=i of (d1[j] + dN[j] - p_j), or -1 if none finite.
3. Pseudocode:
   Read N, K and ticket arrays c,p,a,b
   For each ticket j, set a_j = min(a_j, c_j), b_j = max(b_j, c_j)
   Define compute_dist(target):
     Build segment tree over [1..N], storing each ticket j in nodes covering [a_j..b_j]
     Initialize d[j]=INF; for tickets covering target, set d[j]=p_j and push to heap
     While heap nonempty:
       pop (dist,j); if dist>d[j]: continue
       x = c_j; query segtree at x: for each k in nodes:
         if d[k]>dist+p_k: update and push
         clear list at node to avoid repeats
     return d
   Compute d1 = compute_dist(1), dN = compute_dist(N)
   For i in 1..N:
     ans = min(d1[j]+dN[j]-p_j for j with c_j=i)
     print(ans if <INF else -1)
4. Implementation below.
"""
import sys
import threading

def main():
    import sys
    import heapq

    data = sys.stdin
    N, K = map(int, data.readline().split())
    c = [0]*K; p = [0]*K; a = [0]*K; b = [0]*K
    by_c = [[] for _ in range(N+1)]
    for i in range(K):
        ci, pi, ai, bi = map(int, data.readline().split())
        c[i], p[i] = ci, pi
        ai2, bi2 = ai, bi
        # include purchase point in interval
        a[i] = ai2 if ai2 <= ci else ci
        b[i] = bi2 if bi2 >= ci else ci
        by_c[ci].append(i)

    INF = 10**30
    # segment-tree-based reversed Dijkstra
    def compute_dist(target):
        # build segment tree
        size = 1
        while size < N:
            size <<= 1
        seg = [[] for _ in range(2*size)]
        for j in range(K):
            l = a[j] - 1 + size
            r = b[j] - 1 + size
            while l <= r:
                if l & 1:
                    seg[l].append(j)
                    l += 1
                if not r & 1:
                    seg[r].append(j)
                    r -= 1
                l >>= 1; r >>= 1
        # init distances
        dist = [INF]*K
        hq = []
        for j in range(K):
            if a[j] <= target <= b[j]:
                dist[j] = p[j]
                heapq.heappush(hq, (dist[j], j))
        # dijkstra
        while hq:
            d_j, j = heapq.heappop(hq)
            if d_j != dist[j]:
                continue
            x = c[j] - 1 + size
            # traverse upwards
            pos = x
            while pos:
                lst = seg[pos]
                for k in lst:
                    nd = d_j + p[k]
                    if nd < dist[k]:
                        dist[k] = nd
                        heapq.heappush(hq, (nd, k))
                seg[pos] = []
                pos >>= 1
        return dist

    d1 = compute_dist(1)
    dN = compute_dist(N)
    out = []
    for i in range(1, N+1):
        best = INF
        for j in by_c[i]:
            dj1 = d1[j]; djn = dN[j]
            if dj1 < INF and djn < INF:
                cost = dj1 + djn - p[j]
                if cost < best:
                    best = cost
        out.append(str(best if best < INF else -1))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
