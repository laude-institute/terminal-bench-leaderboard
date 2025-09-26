#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    edges = list(map(int, data[2:]))
    adj = [[] for _ in range(N+1)]
    for i in range(0, 2*M, 2):
        u = edges[i]
        v = edges[i+1]
        adj[u].append(v)
        adj[v].append(u)
    color = [0] * (N+1)
    for i in range(1, N+1):
        used = set(color[v] for v in adj[i] if color[v])
        for c in range(1, 5):
            if c not in used:
                color[i] = c
                break
    print(''.join(str(color[i]) for i in range(1, N+1)))

if __name__ == '__main__':
    main()
