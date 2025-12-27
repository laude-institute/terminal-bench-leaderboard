#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    edges = list(map(int, data[2:]))
    adj = [[] for _ in range(n+1)]
    for i in range(0, 2*m, 2):
        u = edges[i]
        v = edges[i+1]
        adj[u].append(v)
        adj[v].append(u)
    grass = [0] * (n+1)
    for u in range(1, n+1):
        used = set()
        for v in adj[u]:
            if grass[v] != 0:
                used.add(grass[v])
        # pick smallest grass type 1-4 not used
        for t in range(1, 5):
            if t not in used:
                grass[u] = t
                break
    # output concatenated without spaces
    print(''.join(str(grass[i]) for i in range(1, n+1)))

if __name__ == '__main__':
    main()
