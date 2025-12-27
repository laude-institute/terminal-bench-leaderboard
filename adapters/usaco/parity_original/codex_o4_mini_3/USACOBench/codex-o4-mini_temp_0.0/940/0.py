#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Build reversed adjacency list
    rev_adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(next(it))
        b = int(next(it))
        rev_adj[b].append(a)
    # Check each station as candidate
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        # DFS stack
        stack = [i]
        visited[i] = True
        count = 1
        while stack:
            u = stack.pop()
            for v in rev_adj[u]:
                if not visited[v]:
                    visited[v] = True
                    count += 1
                    stack.append(v)
        if count == n:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()
