#!/usr/bin/env python3
"""
Solution to find a station reachable from all others in a directed tree.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # Build reversed adjacency list
    rev = [[] for _ in range(n+1)]  # 1-indexed
    idx = 1
    for _ in range(n-1):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        # reverse edge direction
        rev[b].append(a)

    # DFS to count reachable nodes from start
    def dfs(u, visited):
        visited[u] = True
        for v in rev[u]:
            if not visited[v]:
                dfs(v, visited)

    # Find minimal station reachable from all
    for station in range(1, n+1):
        visited = [False] * (n+1)
        dfs(station, visited)
        if all(visited[1:]):
            print(station)
            return
    print(-1)

if __name__ == "__main__":
    main()
