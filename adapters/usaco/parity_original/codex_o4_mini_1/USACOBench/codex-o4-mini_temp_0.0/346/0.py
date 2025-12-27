#!/usr/bin/env python3
"""
Empty Stalls problem solution using DSU for next free stall.
"""
import sys

def main():
    import sys
    import array
    data = sys.stdin
    line = data.readline().split()
    if not line:
        return
    N, K = map(int, line)
    # DSU parent array, size N+1, using unsigned int for memory efficiency
    parent = array.array('I', range(N+1))

    def find(x):
        # iterative find with path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for _ in range(K):
        parts = data.readline().split()
        if not parts:
            break
        X, Y, A, B = map(int, parts)
        for i in range(1, Y+1):
            p = (A * i + B) % N
            for _ in range(X):
                f = find(p)
                if f == N:
                    f = find(0)
                # occupy f by linking it to next slot
                parent[f] = find(f+1)

    ans = find(0)
    # at least one stall is free, so ans != N
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
