#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    # Universe of letters: uppercase and lowercase
    all_letters = [chr(c) for c in range(ord('A'), ord('Z')+1)] + [chr(c) for c in range(ord('a'), ord('z')+1)]
    for _ in range(t):
        s = data[idx]; idx += 1
        target = data[idx]; idx += 1
        # Build desired mapping
        mapping = {}
        possible = True
        for cs, ct in zip(s, target):
            if cs == ct:
                continue
            if cs in mapping:
                if mapping[cs] != ct:
                    possible = False
                    break
            else:
                mapping[cs] = ct
        if not possible:
            print(-1)
            continue
        # Build graph edges for cs -> ct
        # Count edges
        edges = len(mapping)
        # Build adjacency for SCC
        nodes = set(mapping.keys()) | set(mapping.values())
        adj = {c: [] for c in nodes}
        radj = {c: [] for c in nodes}
        for u, v in mapping.items():
            adj[u].append(v)
            radj[v].append(u)
        # Kosaraju
        visited = set()
        order = []

        def dfs(u):
            visited.add(u)
            for v in adj.get(u, []):
                if v not in visited:
                    dfs(v)
            order.append(u)

        for u in nodes:
            if u not in visited:
                dfs(u)
        comp = {}
        visited.clear()
        cid = 0

        def rdfs(u):
            visited.add(u)
            comp[u] = cid
            for v in radj.get(u, []):
                if v not in visited:
                    rdfs(v)

        # Process in reverse order
        for u in reversed(order):
            if u not in visited:
                rdfs(u)
                cid += 1
        # Count sizes of components
        sizes = {}
        for u in nodes:
            sizes[comp[u]] = sizes.get(comp[u], 0) + 1
        # Count cycles (SCCs with size >1)
        cycles = sum(1 for sz in sizes.values() if sz > 1)
        # Count spare letters
        used = set(s) | set(target)
        spare = len([c for c in all_letters if c not in used])
        if cycles > 0 and spare == 0:
            print(-1)
        else:
            # operations = edges + cycles
            print(edges + cycles)

if __name__ == '__main__':
    main()
