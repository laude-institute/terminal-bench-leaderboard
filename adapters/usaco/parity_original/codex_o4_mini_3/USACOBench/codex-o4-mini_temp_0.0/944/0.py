#!/usr/bin/env python3
"""
Compute smallest perimeter of an axis-aligned rectangle enclosing
at least one connected component (moo network) of cows.
"""
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    coords = [tuple(map(int, input().split())) for _ in range(N)]
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    visited = [False] * N
    best = float('inf')
    # Explore each connected component
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dq = deque([i])
            min_x = max_x = coords[i][0]
            min_y = max_y = coords[i][1]
            while dq:
                u = dq.popleft()
                x, y = coords[u]
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        dq.append(v)
            perimeter = 2 * ((max_x - min_x) + (max_y - min_y))
            if perimeter < best:
                best = perimeter
    print(best)

if __name__ == '__main__':
    main()
