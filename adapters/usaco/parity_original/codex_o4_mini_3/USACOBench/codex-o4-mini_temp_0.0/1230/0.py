#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    n = int(data.readline().strip())
    a = [0] * n
    v = [0] * n
    for i in range(n):
        ai, vi = map(int, data.readline().split())
        a[i] = ai - 1
        v[i] = vi
    # visited marker: 0 = unvisited, >0 = visited with marker of start+1
    vis = [0] * n
    in_cycle = [False] * n
    cycles = []
    for i in range(n):
        if vis[i] != 0:
            continue
        marker = i + 1
        path = []
        node = i
        while vis[node] == 0:
            vis[node] = marker
            path.append(node)
            node = a[node]
        # if encountered a node visited in this run, we found a cycle
        if vis[node] == marker:
            # cycle nodes are from first occurrence of node in path
            idx = path.index(node)
            cycle = path[idx:]
            for u in cycle:
                in_cycle[u] = True
            cycles.append(cycle)
        # else: hit a node from another run, not our cycle
    # sum all values
    total = sum(v)
    # subtract minimal v in each cycle
    remove = 0
    for cycle in cycles:
        # for each i->a_i in cycle, we subtract v[i]
        minv = min(v[u] for u in cycle)
        remove += minv
    result = total - remove
    print(result)

if __name__ == '__main__':
    main()
