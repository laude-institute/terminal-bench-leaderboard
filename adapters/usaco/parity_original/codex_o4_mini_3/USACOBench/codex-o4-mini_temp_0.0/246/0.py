#!/usr/bin/env python3
"""
Solution to Milk Scheduling (msched):
Compute minimum total time to complete all tasks with durations and precedence constraints.
"""
import sys
from collections import deque

def main():
    data = sys.stdin
    n, m = map(int, data.readline().split())
    # Task durations, 1-indexed
    T = [0] * (n + 1)
    for i in range(1, n + 1):
        T[i] = int(data.readline())

    # Build graph
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, data.readline().split())
        adj[a].append(b)
        indeg[b] += 1

    # Earliest finish times
    dp = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        dp[i] = T[i]
        if indeg[i] == 0:
            q.append(i)

    # Topological order processing
    while q:
        u = q.popleft()
        for v in adj[u]:
            # Update v's earliest finish time
            if dp[v] < dp[u] + T[v]:
                dp[v] = dp[u] + T[v]
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # Result is max finish time across all tasks
    print(max(dp[1:]))

if __name__ == '__main__':
    main()
