#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    C, N = map(int, data[:2])
    masks = []
    idx = 2
    for _ in range(N):
        s = data[idx]
        idx += 1
        m = 0
        for ch in s:
            # encode 'H' as 1, 'G' as 0
            m = (m << 1) | (1 if ch == 'H' else 0)
        masks.append(m)
    M = 1 << C
    # distance to nearest input mask for every possible mask
    dist = [-1] * M
    dq = deque()
    # multi-source BFS initialization
    for m in masks:
        if dist[m] == -1:
            dist[m] = 0
            dq.append(m)
    # BFS over hypercube
    while dq:
        m = dq.popleft()
        d = dist[m]
        for i in range(C):
            m2 = m ^ (1 << i)
            if dist[m2] == -1:
                dist[m2] = d + 1
                dq.append(m2)
    # compute answers
    mask_all = M - 1
    out = []
    for m in masks:
        # complement mask
        sc = (~m) & mask_all
        # minimal flips from sc to any input = dist[sc]
        # max hamming distance = C - that minimal distance
        out.append(str(C - dist[sc]))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
