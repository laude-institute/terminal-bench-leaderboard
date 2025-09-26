#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    a = [0] * (n + 1)
    v = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(next(it))
        v[i] = int(next(it))
    visited = [False] * (n + 1)
    in_current = [False] * (n + 1)
    total_v = sum(v[1:])
    total_min = 0
    for i in range(1, n + 1):
        if not visited[i]:
            cur = i
            stack = []
            # traverse until a visited node
            while not visited[cur]:
                visited[cur] = True
                in_current[cur] = True
                stack.append(cur)
                cur = a[cur]
            # if we found a cycle in this traversal
            if in_current[cur]:
                mn = v[cur]
                x = a[cur]
                while x != cur:
                    if v[x] < mn:
                        mn = v[x]
                    x = a[x]
                total_min += mn
            # cleanup markers
            for node in stack:
                in_current[node] = False
    # result is total weights minus minimal drop per cycle
    print(total_v - total_min)

if __name__ == '__main__':
    main()
