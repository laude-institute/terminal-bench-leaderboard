#!/usr/bin/env python3
"""
Milk Scheduling: compute minimum total time to milk all cows with dependencies.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    times = [0] * (n + 1)
    idx = 2
    for i in range(1, n + 1):
        times[i] = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        adj[a].append(b)
        indegree[b] += 1
    # initialize dp with own milking time
    dp = times[:]  # dp[i] is earliest finish time of cow i
    # queue of cows ready to milk
    from collections import deque
    q = deque(i for i in range(1, n + 1) if indegree[i] == 0)
    # process in topological order
    while q:
        u = q.popleft()
        for v in adj[u]:
            # schedule v after u if it extends its finish time
            if dp[v] < dp[u] + times[v]:
                dp[v] = dp[u] + times[v]
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    # result is the max finish time
    print(max(dp[1:]))

if __name__ == '__main__':
    main()
