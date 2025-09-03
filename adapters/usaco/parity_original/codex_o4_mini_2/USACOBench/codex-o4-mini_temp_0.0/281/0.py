#!/usr/bin/env python3
import sys

def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    # Build adjacency list
    adj = [[] for _ in range(N)]
    for i in range(N):
        for _ in range(3):
            f = int(next(it)) - 1
            adj[i].append(f)
    # Total unique edges
    E_total = sum(len(lst) for lst in adj) // 2

    visited = [False] * N
    pos = [0] * N
    best = float('inf')

    def dfs(depth, current_cost, assigned_edges):
        nonlocal best
        # All cows placed
        if depth == N:
            best = min(best, current_cost)
            return
        # Lower bound pruning
        # Each remaining edge costs at least 1
        if current_cost + (E_total - assigned_edges) >= best:
            return

        # Try placing each unvisited cow at this position
        for cow in range(N):
            if not visited[cow]:
                visited[cow] = True
                pos[cow] = depth
                cost_add = 0
                added_edges = 0
                # Account for wires to already placed friends
                for nei in adj[cow]:
                    if visited[nei] and pos[nei] < depth:
                        cost_add += depth - pos[nei]
                        added_edges += 1
                dfs(depth + 1, current_cost + cost_add, assigned_edges + added_edges)
                visited[cow] = False

    dfs(0, 0, 0)
    # Output result
    print(best)

if __name__ == '__main__':
    main()
