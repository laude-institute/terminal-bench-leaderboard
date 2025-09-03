#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    edges = data[2:]
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for i in range(0, len(edges), 2):
        u = int(edges[i])
        v = int(edges[i + 1])
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    color = [0] * (n + 1)
    total_J = 0

    # Process each component via BFS
    for i in range(1, n + 1):
        if not visited[i]:
            dq = deque([i])
            visited[i] = True
            color[i] = 0  # initial color
            count = [1, 0]  # count[0] and count[1]
            # BFS
            while dq:
                u = dq.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 1 - color[u]
                        count[color[v]] += 1
                        dq.append(v)
                    else:
                        # Check bipartiteness
                        if color[v] == color[u]:
                            print(-1)
                            return
            # maximize J signs per component
            total_J += max(count)

    print(total_J)

if __name__ == "__main__":
    main()
