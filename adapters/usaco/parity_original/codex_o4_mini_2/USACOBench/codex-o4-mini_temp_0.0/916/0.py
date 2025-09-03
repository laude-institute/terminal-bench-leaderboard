#!/usr/bin/env python3
"""
Assign grass seed types to pastures such that each cow's two favorite pastures have different grass types.
Greedy lexicographical assignment: for each pasture 1..N, choose the smallest type not used by any already-assigned neighbor.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N, M = map(int, data[:2])
    nums = list(map(int, data[2:]))
    # Build adjacency list
    adj = [[] for _ in range(N+1)]
    for i in range(0, 2*M, 2):
        u = nums[i]
        v = nums[i+1]
        adj[u].append(v)
        adj[v].append(u)
    # grass[i] is assigned type for pasture i
    grass = [0] * (N+1)
    result = []
    # Assign types in order to ensure lexicographically smallest
    for i in range(1, N+1):
        used = set()
        for nei in adj[i]:
            if grass[nei] != 0:
                used.add(grass[nei])
        # choose smallest available type 1..4
        for t in range(1, 5):
            if t not in used:
                grass[i] = t
                result.append(str(t))
                break
    # Output concatenated types
    sys.stdout.write(''.join(result))

if __name__ == '__main__':
    main()
