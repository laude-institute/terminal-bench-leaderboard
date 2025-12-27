#!/usr/bin/env python3
import sys
from array import array

def main():
    data = sys.stdin
    N, K = map(int, data.readline().split())
    # parent[i] points to next candidate free stall
    parent = array('I', range(N))

    def find(x):
        # find root with path compression
        root = x
        while parent[root] != root:
            root = parent[root]
        # compress path
        while parent[x] != root:
            nxt = parent[x]
            parent[x] = root
            x = nxt
        return root

    # process input blocks
    for _ in range(K):
        X, Y, A, B = map(int, data.readline().split())
        for i in range(1, Y + 1):
            pref = (A * i + B) % N
            for _ in range(X):
                s = find(pref)
                # occupy s: link to next free (wrap around)
                nxt = find(s + 1 if s + 1 < N else 0)
                parent[s] = nxt

    # find smallest free stall
    for i in range(N):
        if find(i) == i:
            print(i)
            return

if __name__ == '__main__':
    main()
