#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin.readline().split()
    if not data:
        return
    C, N = map(int, data)
    masks = []
    size = 1 << C
    present = [False] * size
    # Read teams and record patterns
    for _ in range(N):
        s = sys.stdin.readline().strip()
        m = 0
        for ch in s:
            m = (m << 1) | (1 if ch == 'H' else 0)
        masks.append(m)
        present[m] = True
    # Multi-source BFS to compute min distance to any existing pattern
    mask_all = size - 1
    INF = C + 1
    dist = [INF] * size
    dq = deque()
    for m in range(size):
        if present[m]:
            dist[m] = 0
            dq.append(m)
    while dq:
        u = dq.popleft()
        du = dist[u]
        for i in range(C):
            v = u ^ (1 << i)
            if dist[v] > du + 1:
                dist[v] = du + 1
                dq.append(v)
    # For each team, max difference = C - min distance from complement
    out = []
    for m in masks:
        dmin = dist[m ^ mask_all]
        out.append(str(C - dmin))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
