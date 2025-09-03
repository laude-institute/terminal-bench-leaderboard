#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    edges = data[2:]
    adj = [[] for _ in range(n)]
    for i in range(0, 2*m, 2):
        u = int(edges[i]) - 1
        v = int(edges[i+1]) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    result = 0

    for i in range(n):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0
            count = [1, 0]

            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        count[color[v]] += 1
                        queue.append(v)
                    elif color[v] == color[u]:
                        print(-1)
                        return

            result += max(count)

    print(result)

if __name__ == "__main__":
    main()
