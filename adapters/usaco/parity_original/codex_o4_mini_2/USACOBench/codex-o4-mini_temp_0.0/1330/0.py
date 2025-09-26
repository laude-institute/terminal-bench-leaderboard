#!/usr/bin/env python3
"""
Compute maximum number of contiguous "bessie" substrings after deletions
and the minimum deletion cost to achieve it.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0]
    costs = list(map(int, data[1:]))
    pattern = 'bessie'
    M = len(pattern)
    # dp[j]: best (occurrences, cost) having matched j characters of pattern
    INF = 10**18
    dp_occ = [-INF] * M
    dp_cost = [INF] * M
    dp_occ[0] = 0
    dp_cost[0] = 0
    # Process each character
    for i, c in enumerate(s):
        ci = costs[i]
        ndp_occ = [-INF] * M
        ndp_cost = [INF] * M
        for j in range(M):
            occ = dp_occ[j]
            if occ < -INF//2:
                continue
            cost = dp_cost[j]
            # Option 1: delete this char
            occ_d = occ
            cost_d = cost + ci
            if occ_d > ndp_occ[j] or (occ_d == ndp_occ[j] and cost_d < ndp_cost[j]):
                ndp_occ[j] = occ_d
                ndp_cost[j] = cost_d
            # Option 2: keep this char and transition
            if c == pattern[j]:
                # matched next pattern char
                if j + 1 == M:
                    nj = 0
                    occ_k = occ + 1
                    cost_k = cost
                else:
                    nj = j + 1
                    occ_k = occ
                    cost_k = cost
            else:
                # fallback on mismatch (KMP reset)
                if c == pattern[0]:
                    nj = 1
                else:
                    nj = 0
                occ_k = occ
                cost_k = cost
            if occ_k > ndp_occ[nj] or (occ_k == ndp_occ[nj] and cost_k < ndp_cost[nj]):
                ndp_occ[nj] = occ_k
                ndp_cost[nj] = cost_k
        dp_occ, dp_cost = ndp_occ, ndp_cost
    # Extract best result
    best_occ = max(dp_occ)
    best_cost = INF
    for j in range(M):
        if dp_occ[j] == best_occ and dp_cost[j] < best_cost:
            best_cost = dp_cost[j]
    print(best_occ)
    print(best_cost)

if __name__ == '__main__':
    main()
