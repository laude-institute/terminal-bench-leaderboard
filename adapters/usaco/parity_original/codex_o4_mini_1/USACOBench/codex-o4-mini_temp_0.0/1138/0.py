#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    c = [0]*N
    p = [None]*N
    # occurrence IDs: for vertex v (0-index), portals p[v][i] at occurrence id = 4*v + i
    portal_occ = {}  # portal_id -> list of occurrence ids
    for v in range(N):
        parts = list(map(int, input().split()))
        c[v] = parts[0]
        pv = parts[1:]
        p[v] = pv
        for i, pid in enumerate(pv):
            occ = 4*v + i
            portal_occ.setdefault(pid, []).append(occ)
    # DSU over 4N occurrences
    parent = list(range(4*N))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx = find(x); ry = find(y)
        if rx == ry: return False
        parent[ry] = rx
        return True
    # initial unions: portal edges
    comp = 4*N
    for occs in portal_occ.values():
        if len(occs) == 2:
            if union(occs[0], occs[1]): comp -= 1
    # initial default switch edges
    for v in range(N):
        # default pairs: (0,1), (2,3)
        a = 4*v; b = 4*v+1; c1 = 4*v+2; d = 4*v+3
        if union(a, b): comp -= 1
        if union(c1, d): comp -= 1
    # process vertices by cost
    verts = list(range(N))
    verts.sort(key=lambda v: c[v])
    total = 0
    for v in verts:
        if comp <= 1: break
        # current roots of 4 occ
        occs = [4*v+i for i in range(4)]
        roots = [find(o) for o in occs]
        # group by root
        groups = {}
        for idx, r in enumerate(roots):
            groups.setdefault(r, []).append(idx)
        distinct = list(groups.keys())
        # compute possible merges
        cnt = len(distinct)
        pairs = []
        if cnt >= 3:
            # find largest group
            # groups sorted by size desc
            items = sorted(groups.items(), key=lambda x: -len(x[1]))
            g0, g1, g2 = items[0][1], items[1][1], items[2][1]
            # pair g0[0] with g1[0], g0[1] with g2[0]
            pairs.append((occs[g0[0]], occs[g1[0]]))
            pairs.append((occs[g0[1]], occs[g2[0]]))
        elif cnt == 2:
            g1 = groups[distinct[0]]
            g2 = groups[distinct[1]]
            if len(g1) == 2 and len(g2) == 2:
                pairs.append((occs[g1[0]], occs[g2[0]]))
                pairs.append((occs[g1[1]], occs[g2[1]]))
            else:
                # only one useful pair
                # find the singleton
                if len(g1) == 1:
                    pairs.append((occs[g1[0]], occs[g2[0]]))
                else:
                    pairs.append((occs[g2[0]], occs[g1[0]]))
        # else cnt <=1: no pairs
        # apply unions for these pairs
        merged = False
        merges_done = 0
        for x, y in pairs:
            if comp <= 1: break
            if union(x, y):
                comp -= 1
                merges_done += 1
                merged = True
        if merged:
            total += c[v]
    print(total)

if __name__ == '__main__':
    main()
