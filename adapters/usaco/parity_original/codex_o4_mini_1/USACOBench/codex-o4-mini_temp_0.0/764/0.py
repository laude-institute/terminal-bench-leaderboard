#!/usr/bin/env python3
"""
Solution to "Bovine Shuffle" problem.
Find number of positions that remain occupied after infinite shuffles.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    # a_i: target position for position i
    a = list(map(int, data[1:1+N]))

    # Compute indegrees: count of incoming edges for each node
    indegree = [0] * (N + 1)
    for ai in a:
        indegree[ai] += 1

    # Use queue to remove non-cycle nodes (Kahn's algorithm)
    from collections import deque
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    # Remove nodes not in any cycle
    while q:
        u = q.popleft()
        v = a[u-1]
        indegree[u] = -1  # mark removed
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

    # Remaining nodes with indegree > 0 are in cycles
    result = sum(1 for i in range(1, N+1) if indegree[i] > 0)
    print(result)

if __name__ == '__main__':
    main()
