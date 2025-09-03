#!/usr/bin/env python3
"""
Compute earliest possible dates for milking sessions given minimum start days
and constraints that session b occurs at least x days after a.
"""
import sys

def main():
    import sys
    from collections import deque

    data = sys.stdin.readline().split()
    N, M, C = map(int, data)
    S = list(map(int, sys.stdin.readline().split()))
    # Build graph
    adj = [[] for _ in range(N)]
    indegree = [0] * N
    for _ in range(C):
        a, b, x = map(int, sys.stdin.readline().split())
        # zero-index
        u = a - 1
        v = b - 1
        adj[u].append((v, x))
        indegree[v] += 1

    # Earliest date for each session
    earliest = S[:]
    # Kahn's algorithm for DAG longest path
    q = deque()
    for i in range(N):
        if indegree[i] == 0:
            q.append(i)

    while q:
        u = q.popleft()
        for v, w in adj[u]:
            # relax constraint
            if earliest[u] + w > earliest[v]:
                earliest[v] = earliest[u] + w
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    # Output results
    out = sys.stdout
    for d in earliest:
        out.write(str(d))
        out.write("\n")


if __name__ == '__main__':
    main()
