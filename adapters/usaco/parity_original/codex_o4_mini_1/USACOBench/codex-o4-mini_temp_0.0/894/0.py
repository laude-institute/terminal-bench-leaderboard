#!/usr/bin/env python3
"""
Compute the minimum number of grass types needed on a tree of fields
such that no two fields at distance 1 or 2 share the same type.
This equals (maximum degree of the tree) + 1.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # degree count for each field (1-indexed)
    deg = [0] * (n + 1)
    for _ in range(n - 1):
        u = int(next(it))
        v = int(next(it))
        deg[u] += 1
        deg[v] += 1
    # answer is maximum degree plus one
    result = max(deg[1:]) + 1
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
