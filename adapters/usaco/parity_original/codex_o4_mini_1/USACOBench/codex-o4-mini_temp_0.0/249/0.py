#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    N, M, R = map(int, data.readline().split())
    L = [0] + [int(data.readline()) for _ in range(N)]
    Rv = [0] + [int(data.readline()) for _ in range(M)]
    edges = []
    for _ in range(R):
        i, j = map(int, data.readline().split())
        edges.append((i, j))
    # Sort edges by left index then right index
    edges.sort()
    # dpR[j]: best sum ending at right site j
    dpR = Rv[:]  # 1-indexed
    ans = max(max(L[1:]), max(Rv[1:]) if M > 0 else 0)
    # Process edges grouped by i
    idx = 0
    while idx < R:
        i = edges[idx][0]
        # collect all js for this i
        js = []
        while idx < R and edges[idx][0] == i:
            js.append(edges[idx][1])
            idx += 1
        # process this group in increasing j (already sorted)
        local_dpL = L[i]
        updates = {}
        for j in js:
            # extend to right: L->R
            fLR = local_dpL + Rv[j]
            # extend to left: R->L
            fRL = dpR[j] + L[i]
            # update answer
            if fLR > ans:
                ans = fLR
            if fRL > ans:
                ans = fRL
            # update local dpL for next j (ensure fRL not used for same j->R)
            if fRL > local_dpL:
                local_dpL = fRL
            # record dpR updates after this row
            prev = updates.get(j)
            if prev is None or fLR > prev:
                updates[j] = fLR
        # apply updates to dpR
        for j, v in updates.items():
            if v > dpR[j]:
                dpR[j] = v
        # continue to next i
    # output result
    print(ans)

if __name__ == '__main__':
    main()
