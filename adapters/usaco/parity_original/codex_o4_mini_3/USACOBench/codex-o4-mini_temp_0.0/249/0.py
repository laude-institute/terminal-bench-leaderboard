#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); M = int(next(it)); R = int(next(it))
    L = [int(next(it)) for _ in range(N)]
    Rv = [int(next(it)) for _ in range(M)]
    left_edges = [[] for _ in range(N+1)]
    for _ in range(R):
        i = int(next(it)); j = int(next(it))
        left_edges[i].append(j)
    # sort edges by j for each i
    for i in range(1, N+1):
        if left_edges[i]:
            left_edges[i].sort()
    # DP
    best_dpR_j = [0] * (M+1)
    ans = 0
    # consider single-node tours
    if L:
        ans = max(ans, max(L))
    if Rv:
        ans = max(ans, max(Rv))
    for i in range(1, N+1):
        edges_j = left_edges[i]
        if not edges_j:
            continue
        best_dpL_group = 0
        # store dpR for updates
        dpR_list = []
        for j in edges_j:
            valL = L[i-1]
            valR = Rv[j-1]
            # transition to R (share i)
            dpR = valL + valR
            if best_dpL_group:
                dpR = max(dpR, best_dpL_group + valR)
            # transition to L (share j)
            dpL = valL + valR
            if best_dpR_j[j]:
                dpL = max(dpL, best_dpR_j[j] + valL)
            # update group best
            best_dpL_group = max(best_dpL_group, dpL)
            # update answer
            if dpR > ans: ans = dpR
            if dpL > ans: ans = dpL
            dpR_list.append((j, dpR))
        # apply dpR updates
        for j, dpR in dpR_list:
            if dpR > best_dpR_j[j]: best_dpR_j[j] = dpR
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
