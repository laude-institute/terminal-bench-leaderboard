#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    # Read number of cows (nodes) and constraints (edges)
    N, M = map(int, input().split())
    # Read milking times
    duration = [0] * (N + 1)
    for i in range(1, N + 1):
        duration[i] = int(input())
    # Build graph and indegree counts
    adj = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        indegree[v] += 1
    # earliest_finish[i]: earliest time cow i finishes milking
    earliest_finish = [0] * (N + 1)
    dq = deque()
    # Initialize queue with cows having no prerequisites
    for i in range(1, N + 1):
        earliest_finish[i] = duration[i]
        if indegree[i] == 0:
            dq.append(i)
    # Topological order processing
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            # Update earliest finish time for v
            finish_time = earliest_finish[u] + duration[v]
            if finish_time > earliest_finish[v]:
                earliest_finish[v] = finish_time
            indegree[v] -= 1
            if indegree[v] == 0:
                dq.append(v)
    # Result is the maximum finishing time
    print(max(earliest_finish[1:]))

if __name__ == "__main__":
    main()
