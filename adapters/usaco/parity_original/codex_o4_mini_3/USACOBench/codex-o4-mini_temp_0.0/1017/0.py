#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M, C = map(int, input().split())
    S = list(map(int, input().split()))
    # Build graph and compute in-degrees
    adj = [[] for _ in range(N)]
    indegree = [0] * N
    for _ in range(C):
        a, b, x = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append((b, x))
        indegree[b] += 1

    # Initialize days with base earliest days
    day = S[:]
    dq = deque()
    # Enqueue nodes with no prerequisites
    for i in range(N):
        if indegree[i] == 0:
            dq.append(i)

    # Topological order relaxation for longest paths
    while dq:
        u = dq.popleft()
        du = day[u]
        for v, w in adj[u]:
            # update earliest day for v
            if day[v] < du + w:
                day[v] = du + w
            indegree[v] -= 1
            if indegree[v] == 0:
                dq.append(v)

    # Output results
    out = sys.stdout.write
    for d in day:
        out(str(d) + '\n')

if __name__ == '__main__':
    main()
