"""
Problem Restatement:
We have N vertices, each with 4 portals connecting to other vertices via unique portal IDs. A location is (vertex, portal).
We can move between vertices via portals, and at each vertex, switch between paired portals. The default pairing is the first two and last two in the list.
We may pay cost c_v to arbitrarily permute the portal list at vertex v, thus choosing any pairing. We need the entire graph of 4N locations to be connected, minimizing total cost.

Conceptual Solution:
1. Model each location as a node. There are 4N nodes.
2. Portal connections form 2N edges between vertices—union these in a DSU.
3. Default local pairings give 2 edges per vertex—union these, counting how many new connections they add (R0).
4. To connect all 4N nodes, we need exactly 4N-1 unions. Portal unions give 2N merges; local default give K = sum R0.
   We need D = (4N-1) - (2N + K) additional merges by changing pairings at some vertices.
5. At each vertex, if we pay, we can choose the pairing (among 3 matchings) that yields the maximum merges against the DSU state after portal unions.
   Let Rpaid be that maximum merges (0..2), so the gain is delta = Rpaid - R0.
6. We need to select a subset of vertices with sum(delta) >= D at minimal sum(c_v). This is a small-weight knapsack (weights 1 or 2), solvable by DP in O(ND).

Pseudocode:
read N
for each vertex v:
    read c[v], portals p[v][0..3]
# DSU over 4N nodes, numbered (v,i)
init DSU of size 4*N
# Union portal edges
for each portal ID:
    find its two (v,i) occurrences, union them
# Compute R0 for default pairings
R0_list = []
K = 0
for v in 1..N:
    reps = find reps of the 4 nodes
    pairs = [(0,1),(2,3)]
    r0 = 0
    for (i,j) in pairs:
        if rep[i] != rep[j]: union and r0 += 1
    K += r0
    # Evaluate best Rpaid by testing the 3 matchings on the DSU snapshot after portals
    best = max over matchings of count(rep[a]!=rep[b])
    delta = best - r0
    if delta > 0: record item (weight=delta, cost=c[v])
# compute D = (4N-1)-(2N+K)
if D <= 0: print 0; exit
# DP for knapsack to reach weight >= D
dp = [INF]*(D+2)
dp[0] = 0
for each item (w, cost):
    for x from D down to 0:
        if dp[x] != INF:
            dp[min(D, x+w)] = min(dp[min(D, x+w)], dp[x]+cost)
answer = dp[D]
print(answer)
"""

import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    N = int(input())
    c = [0]*N
    p = [None]*N
    portal_map = {}
    for v in range(N):
        data = list(map(int, input().split()))
        c[v] = data[0]
        p[v] = data[1:]
        for i, pid in enumerate(p[v]):
            portal_map.setdefault(pid, []).append((v, i))

    # DSU
    parent = list(range(4*N))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb: return False
        parent[rb] = ra
        return True

    # Union portal edges
    for pid, occ in portal_map.items():
        (v1,i1),(v2,i2) = occ
        union(v1*4 + i1, v2*4 + i2)

    # Default pairings
    K = 0
    items = []  # (delta, cost)
    for v in range(N):
        # snapshot reps after portal unions
        reps = [find(v*4 + i) for i in range(4)]
        # default pairs
        pairs = [(0,1),(2,3)]
        r0 = 0
        for i,j in pairs:
            if union(v*4 + i, v*4 + j): r0 += 1
        K += r0
        # compute best Rpaid
        best = 0
        # test all 3 matchings
        matches = [[(0,1),(2,3)], [(0,2),(1,3)], [(0,3),(1,2)]]
        for m in matches:
            cnt = 0
            for i,j in m:
                if reps[i] != reps[j]: cnt += 1
            best = max(best, cnt)
        delta = best - r0
        if delta > 0:
            items.append((delta, c[v]))

    D = (4*N - 1) - (2*N + K)
    if D <= 0:
        print(0)
        return

    INF = 10**18
    dp = [INF] * (D+1)
    dp[0] = 0
    for w, cost in items:
        for x in range(D, -1, -1):
            if dp[x] < INF:
                nx = min(D, x + w)
                dp[nx] = min(dp[nx], dp[x] + cost)
    ans = dp[D]
    print(ans)

if __name__ == '__main__':
    main()
