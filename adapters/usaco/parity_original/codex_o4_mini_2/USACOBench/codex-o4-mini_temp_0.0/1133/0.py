#!/usr/bin/env python3
"""
Solve maximum cow friendships via grass cells.
"""
import sys

def hopcroft_karp(adj, n_left, n_right):
    # adj: list of lists of right node ids for each left node
    INF = 1e9
    dist = [0] * n_left
    pair_u = [-1] * n_left
    pair_v = [-1] * n_right

    from collections import deque

    def bfs():  # build layers
        queue = deque()
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        d = INF
        while queue:
            u = queue.popleft()
            if dist[u] < d:
                for v in adj[u]:
                    if pair_v[v] == -1:
                        d = dist[u] + 1
                    else:
                        if dist[pair_v[v]] == INF:
                            dist[pair_v[v]] = dist[u] + 1
                            queue.append(pair_v[v])
        return d != INF

    def dfs(u):
        for v in adj[u]:
            pv = pair_v[v]
            if pair_v[v] == -1 or (dist[pv] == dist[u] + 1 and dfs(pv)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    result = 0
    while bfs():
        for u in range(n_left):
            if pair_u[u] == -1 and dfs(u):
                result += 1
    return result

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    # map cows to indices
    cow_idx = {}
    idx = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'C':
                cow_idx[(i,j)] = idx
                idx += 1
    # collect grass cells and potential pairs
    cell_pairs = []
    pair2cells = {}
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 'G': continue
            pairs = []
            # vertical
            if (i-1,j) in cow_idx and (i+1,j) in cow_idx:
                u = cow_idx[(i-1,j)]
                v = cow_idx[(i+1,j)]
                p = (u,v) if u<v else (v,u)
                pairs.append(p)
            # horizontal
            if (i,j-1) in cow_idx and (i,j+1) in cow_idx:
                u = cow_idx[(i,j-1)]
                v = cow_idx[(i,j+1)]
                p = (u,v) if u<v else (v,u)
                pairs.append(p)
            if pairs:
                ci = len(cell_pairs)
                cell_pairs.append(pairs)
                for p in pairs:
                    pair2cells.setdefault(p, []).append(ci)
    C = len(cell_pairs)
    alive = [True]*C
    from collections import deque
    queue = deque([i for i,p in enumerate(cell_pairs) if len(p)==1])
    pair_used = {}
    ans = 0
    # prune single-pair cells
    while queue:
        ci = queue.popleft()
        if not alive[ci] or len(cell_pairs[ci])!=1: continue
        p = cell_pairs[ci][0]
        if pair_used.get(p, False): continue
        # use this pair
        pair_used[p] = True
        ans += 1
        alive[ci] = False
        # update neighbors
        for oj in pair2cells.get(p, []):
            if alive[oj]:
                lst = cell_pairs[oj]
                # remove p
                cell_pairs[oj] = [x for x in lst if x!=p]
                if len(cell_pairs[oj])==1:
                    queue.append(oj)
    # remaining cells have 2 pairs
    left_map = {}
    right_map = {}
    lidx = 0; ridx = 0
    # assign mappings
    for i,pairs in enumerate(cell_pairs):
        if not alive[i]: continue
        # both unused
        ulist = [p for p in pairs if not pair_used.get(p,False)]
        if len(ulist)!=2: continue
        left_map[i] = lidx; lidx+=1
        for p in ulist:
            if p not in right_map:
                right_map[p] = ridx; ridx+=1
    # build adjacency
    adj = [[] for _ in range(lidx)]
    for i,pairs in enumerate(cell_pairs):
        if i not in left_map: continue
        ulist = [p for p in pairs if not pair_used.get(p,False)]
        u = left_map[i]
        for p in ulist:
            adj[u].append(right_map[p])
    # matching
    match = hopcroft_karp(adj, lidx, ridx)
    print(ans + match)

if __name__ == '__main__':
    main()
