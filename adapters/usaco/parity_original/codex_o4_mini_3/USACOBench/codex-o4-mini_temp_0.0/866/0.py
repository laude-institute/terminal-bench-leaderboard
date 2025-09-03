#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(3000000)
    data = sys.stdin
    line = data.readline().split()
    if not line:
        return
    N = int(line[0]); M = int(line[1])
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v = map(int, data.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    cons = []
    indeg = [0]*(N+1)
    g = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, data.readline().split())
        cons.append((a,b))
        g[a].append(b)
        indeg[b] += 1
    # Kahn to detect cycle in constraint graph
    from collections import deque
    dq = deque()
    cnt = 0
    for i in range(1, N+1):
        if indeg[i] == 0:
            dq.append(i)
    while dq:
        u = dq.popleft()
        cnt += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                dq.append(v)
    if cnt < N:
        # cycle in constraints, no solution
        out = sys.stdout
        for _ in range(N): out.write('0\n')
        return
    # root tree at 1, compute parent, depth, tin, tout
    parent = [0]*(N+1)
    depth = [0]*(N+1)
    tin = [0]*(N+1)
    tout = [0]*(N+1)
    LOG = (N+1).bit_length()
    up = [[0]*(N+1) for _ in range(LOG)]
    t = 0
    # iterative dfs
    stack = [(1, 0, 0)]  # node, parent, next child idx
    while stack:
        node, par, idx = stack.pop()
        if idx == 0:
            # entry
            parent[node] = par
            up[0][node] = par
            depth[node] = depth[par] + 1 if par else 0
            t += 1
            tin[node] = t
        if idx < len(adj[node]):
            nei = adj[node][idx]
            stack.append((node, par, idx+1))
            if nei == par: continue
            stack.append((nei, node, 0))
        else:
            # exit
            tout[node] = t
    # binary lifting
    for k in range(1, LOG):
        uplevel = up[k-1]
        upk = up[k]
        for v in range(1, N+1):
            upk[v] = uplevel[uplevel[v]]
    # helper to get k-th ancestor
    def climb(u, k):
        i = 0
        while k and u:
            if k & 1:
                u = up[i][u]
            k >>= 1; i += 1
        return u
    # diff array on Euler order [1..N]
    diff = [0] * (N+3)
    for a,b in cons:
        # find neighbor c of a on path to b
        if tin[a] <= tin[b] and tout[b] <= tout[a]:
            # a ancestor of b
            # need child c of a on path
            # b is deeper
            d = depth[b] - (depth[a] + 1)
            c = climb(b, d)
        else:
            c = parent[a]
        # determine relation in original tree
        if parent[a] == c:
            # c is parent of a -> forbid subtree of a
            l = tin[a]; r = tout[a]
            diff[l] += 1; diff[r+1] -= 1
        else:
            # c is child of a -> forbid everything except subtree of c
            # interval [1, tin[c]-1]
            l1 = 1; r1 = tin[c] - 1
            if r1 >= l1:
                diff[l1] += 1; diff[r1+1] -= 1
            # interval [tout[c]+1, N]
            l2 = tout[c] + 1; r2 = N
            if l2 <= r2:
                diff[l2] += 1; diff[r2+1] -= 1
    # accumulate
    arr = [0] * (N+1)
    cur = 0
    # euler index to node: we need a mapping: node_by_tin
    node_by_tin = [0] * (N+1)
    for v in range(1, N+1):
        node_by_tin[tin[v]] = v
    for i in range(1, N+1):
        cur += diff[i]
        arr[i] = cur
    out = sys.stdout
    # output for nodes 1..N
    for v in range(1, N+1):
        out.write('0\n' if arr[tin[v]] > 0 else '1\n')

if __name__ == '__main__':
    main()
