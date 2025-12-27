#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        try:
            a[i] = int(next(it))
        except StopIteration:
            break

    # visited: 0 = unvisited, 1 = visiting, 2 = done
    visited = [0] * (n + 1)
    in_cycle = [False] * (n + 1)

    for i in range(1, n + 1):
        if visited[i] != 0:
            continue
        path = []
        u = i
        # traverse until we hit a visited node
        while visited[u] == 0:
            visited[u] = 1
            path.append(u)
            u = a[u]
        # if we found a cycle, mark nodes in the cycle
        if visited[u] == 1:
            # cycle starts at first occurrence of u in path
            idx = path.index(u)
            for v in path[idx:]:
                in_cycle[v] = True
        # mark entire path as done
        for v in path:
            visited[v] = 2

    # count positions always occupied => cycle nodes
    result = sum(in_cycle[1:])
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
