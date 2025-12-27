#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    # Read preferences, convert to 0-based gift indices
    prefs = [[int(next(it)) - 1 for _ in range(n)] for _ in range(n)]

    # For each cow, pointer to current best available gift
    pointer = [0] * n
    # Track which gifts have been removed (assigned in completed cycles)
    removed = [False] * n
    # Track which cows are still in the market
    active = [True] * n
    remaining = n
    # Final assignment for each cow
    assignment = [-1] * n
    # Initial owners: gift i is owned by cow i
    owner = list(range(n))

    while remaining > 0:
        # Build the directed graph: cow -> owner of its top available gift
        edge = [-1] * n
        for i in range(n):
            if not active[i]:
                continue
            # Advance pointer past removed gifts
            while pointer[i] < n and removed[prefs[i][pointer[i]]]:
                pointer[i] += 1
            g = prefs[i][pointer[i]]
            edge[i] = owner[g]

        # Find a cycle in this graph
        cycle = []
        visited = [False] * n
        for start in range(n):
            if not active[start] or visited[start]:
                continue
            path = []
            index_in_path = {}
            u = start
            # Follow pointers until we stop or find a cycle
            while True:
                visited[u] = True
                index_in_path[u] = len(path)
                path.append(u)
                v = edge[u]
                if v in index_in_path:
                    # cycle detected
                    cycle = path[index_in_path[v]:]
                    break
                if visited[v]:
                    break
                u = v
            if cycle:
                break

        # Assign each cow in the cycle and remove them and their gifts
        for i in cycle:
            g = prefs[i][pointer[i]]
            assignment[i] = g
        for i in cycle:
            active[i] = False
            removed[assignment[i]] = True
            remaining -= 1

    # Output results (convert back to 1-based)
    out = sys.stdout
    for i in range(n):
        out.write(str(assignment[i] + 1) + "\n")

if __name__ == '__main__':
    main()
