#!/usr/bin/env python3
"""
Solver for Farmer John's grass planting problem.
Reads a tree of N nodes, computes the maximum degree Δ,
and outputs Δ+1 (minimum colors needed so no two nodes
at distance ≤2 share the same color).
"""
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    # Degree count for each field
    deg = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1
    # The answer is max degree + 1
    max_deg = max(deg[1:])
    print(max_deg + 1)

if __name__ == "__main__":
    main()
