#!/usr/bin/env python3
"""
0.py: Solution for 'Empty Stalls' problem.
Implements a circular disjoint-set union (union-find) to allocate stalls efficiently.
No external libraries used.
"""
import sys

def main():
    data = sys.stdin
    # Read number of stalls and specification lines
    N, K = map(int, data.readline().split())
    # DSU parent array with an extra sentinel at index N
    parent = list(range(N + 1))

    def find(x):
        # Path-compression iterative find
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        parent[x_root] = y_root

    # Process each specification line
    for _ in range(K):
        X, Y, A, B = map(int, data.readline().split())
        for i in range(1, Y + 1):
            preferred = (A * i + B) % N
            # X cows prefer this stall
            for _ in range(X):
                # Find next free stall at or after preferred
                nxt = find(preferred)
                if nxt == N:
                    # Wrap around to start
                    nxt = find(0)
                # Occupy stall nxt and link it to nxt+1
                union(nxt, nxt + 1)

    # Find smallest free stall
    for i in range(N):
        if find(i) == i:
            print(i)
            return

if __name__ == '__main__':
    main()
