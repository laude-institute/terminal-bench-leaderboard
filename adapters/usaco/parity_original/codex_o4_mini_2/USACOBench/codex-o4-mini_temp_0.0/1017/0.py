#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M, C = map(int, input().split())
    S = list(map(int, input().split()))
    # Build adjacency list for constraints a->b with weight x
    adj = [[] for _ in range(N)]
    for _ in range(C):
        a, b, x = map(int, input().split())
        adj[a-1].append((b-1, x))

    # Initialize distances with earliest possible days
    dist = S[:]
    in_queue = [True] * N
    queue = deque(range(N))

    # SPFA for longest paths (difference constraints)
    while queue:
        u = queue.popleft()
        in_queue[u] = False
        du = dist[u]
        for v, w in adj[u]:
            if dist[v] < du + w:
                dist[v] = du + w
                if not in_queue[v]:
                    in_queue[v] = True
                    queue.append(v)

    # Output results
    out = sys.stdout.write
    for d in dist:
        out(str(d) + '\n')

if __name__ == '__main__':
    main()
