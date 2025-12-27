#!/usr/bin/env python3
"""
Solution to find a station reachable from all others in a directed tree.
"""
import sys

def main():
    # Read number of stations
    n = int(sys.stdin.readline())
    # Build reversed adjacency: for each edge a->b, add b->a
    rev_adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        rev_adj[b].append(a)

    # Try each station i as candidate
    for i in range(1, n+1):
        visited = [False] * (n+1)
        stack = [i]
        visited[i] = True
        # DFS on reversed graph to count reachability
        while stack:
            u = stack.pop()
            for v in rev_adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        # If all stations reached, output i
        if all(visited[1:]):
            print(i)
            return
    # No such station
    print(-1)

if __name__ == "__main__":
    main()
