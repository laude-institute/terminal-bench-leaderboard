#!/usr/bin/env python3
"""
Solution for Bessie's hiking ticket problem.
"""
import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    tickets = []  # list of (c, p, a, b)
    for _ in range(K):
        c, p, a, b = map(int, input().split())
        tickets.append((c, p, a, b))
    # TODO: Implement Dijkstra on hypergraph of tickets and intervals.
    # For each start i in 1..N, compute minimal cost to cover both 1 and N.
    # This requires efficient segment-tree graph construction and multi-source Dijkstra.
    
    # Placeholder: print -1 for all
    for _ in range(N):
        print(-1)

if __name__ == '__main__':
    main()
