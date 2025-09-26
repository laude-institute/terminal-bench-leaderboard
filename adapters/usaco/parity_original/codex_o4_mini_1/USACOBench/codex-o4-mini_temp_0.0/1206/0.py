#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    # Read preference lists
    pref = []  # pref[c] = list of gifts (1-based)
    pos = [dict() for _ in range(n)]
    for c in range(n):
        row = [int(next(it)) for _ in range(n)]
        pref.append(row)
        for idx, g in enumerate(row):
            pos[c][g] = idx
    # Build acceptable edges: cow c accepts gifts up to her original gift c+1
    accept = [[] for _ in range(n)]
    for c in range(n):
        cutoff = pos[c][c+1]
        for idx in range(cutoff+1):
            # convert gift to 0-based
            accept[c].append(pref[c][idx] - 1)

    # Maximum bipartite matching: cows -> gifts
    match_cow = [-1] * n  # matched gift for each cow
    match_gift = [-1] * n  # matched cow for each gift

    def dfs(u, seen):
        for v in accept[u]:
            if seen[v]:
                continue
            seen[v] = True
            # if gift v free or can reassign its current cow
            w = match_gift[v]
            if w == -1 or dfs(w, seen):
                match_cow[u] = v
                match_gift[v] = u
                return True
        return False

    # find any perfect matching (original assignment guarantees existence)
    for c in range(n):
        seen = [False] * n
        if not dfs(c, seen):
            # should not happen
            print("No perfect matching", file=sys.stderr)
            sys.exit(1)

    # Build directed graph for SCC: nodes 0..n-1 cows, n..2n-1 gifts
    N2 = 2 * n
    adj = [[] for _ in range(N2)]
    for c in range(n):
        for v in accept[c]:
            if match_cow[c] == v:
                # matching edge: gift->cow
                adj[n + v].append(c)
            else:
                # non-matching: cow->gift
                adj[c].append(n + v)

    # Tarjan's algorithm for SCC
    index = 0
    indices = [-1] * N2
    lowlink = [0] * N2
    onstack = [False] * N2
    stack = []
    comp = [-1] * N2
    comp_id = 0

    def strongconnect(u):
        nonlocal index, comp_id
        indices[u] = index
        lowlink[u] = index
        index += 1
        stack.append(u)
        onstack[u] = True
        for v in adj[u]:
            if indices[v] == -1:
                strongconnect(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif onstack[v]:
                lowlink[u] = min(lowlink[u], indices[v])
        # if u is root of SCC
        if lowlink[u] == indices[u]:
            while True:
                v = stack.pop()
                onstack[v] = False
                comp[v] = comp_id
                if v == u:
                    break
            comp_id += 1

    for u in range(N2):
        if indices[u] == -1:
            strongconnect(u)

    # For each cow, find best gift in her list up to original that is in same SCC or matched
    out = []
    for c in range(n):
        cutoff = pos[c][c+1]
        ans = c + 1  # default original gift
        for idx in range(cutoff+1):
            g = pref[c][idx] - 1
            # check if edge (c,g) can be in some perfect matching
            if match_cow[c] == g or comp[c] == comp[n + g]:
                ans = g + 1
                break
        out.append(str(ans))

    sys.stdout.write("\n".join(out))


if __name__ == '__main__':
    main()
