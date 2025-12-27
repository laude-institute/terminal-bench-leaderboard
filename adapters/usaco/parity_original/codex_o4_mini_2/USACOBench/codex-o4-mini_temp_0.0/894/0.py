#!/usr/bin/env python3
"""
Compute minimum grass types (colors) needed so that in a tree of N fields,
no two fields at distance 1 or 2 share the same grass type.
This equals max degree of tree plus one.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Degree count for each field
    deg = [0] * (n + 1)
    # Read edges and update degrees
    for _ in range(n - 1):
        u = int(next(it)); v = int(next(it))
        deg[u] += 1
        deg[v] += 1
    # Minimum colors = maximum degree + 1
    max_deg = max(deg[1:])
    print(max_deg + 1)

if __name__ == "__main__":
    main()
