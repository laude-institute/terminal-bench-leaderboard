#!/usr/bin/env python3
"""
1. Restate the problem in plain English:
   We have N fields in a line. Each field has a recorded moo volume that includes local cows' moo plus wind-carried moo from the previous field reduced by 1 per step.
   Each cow belongs to one of B breeds, and breed i moos at volume V[i]. Given the recorded volumes, find the minimum total number of cows, or -1 if impossible.

2. Conceptual solution in plain English:
   - For each field, subtract wind contribution max(0, M[i-1] - 1) from recorded volume to get local cows' needed volume.
   - If needed volume is negative, it's impossible.
   - Solve minimal coin-change for each needed volume using breed volumes V[].
   - Precompute a DP array up to max needed volume and sum minimal counts per field.

3. Pseudocode:
   read N, B
   read list V of length B
   read list M of length N
   C = []
   for i in 0..N-1:
       prev = 0 if i==0 else max(0, M[i-1] - 1)
       need = M[i] - prev
       if need < 0: print(-1); exit
       C.append(need)
   maxC = max(C)
   dp[0..maxC] = inf, dp[0]=0
   for v in 1..maxC:
       for coin in V:
           if v>=coin: dp[v] = min(dp[v], dp[v-coin]+1)
   total = 0
   for need in C:
       if dp[need] == inf: print(-1); exit
       total += dp[need]
   print(total)
"""

import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    B = int(next(it))
    V = [int(next(it)) for _ in range(B)]
    M = [int(next(it)) for _ in range(N)]
    # Compute needed local volumes per field
    C = []
    for i in range(N):
        prev = 0 if i == 0 else max(0, M[i-1] - 1)
        need = M[i] - prev
        if need < 0:
            print(-1)
            return
        C.append(need)
    maxC = max(C) if C else 0
    # DP for minimal cows (coin change)
    INF = 10**18
    dp = [INF] * (maxC + 1)
    dp[0] = 0
    for v in range(1, maxC + 1):
        for coin in V:
            if v >= coin and dp[v-coin] + 1 < dp[v]:
                dp[v] = dp[v-coin] + 1
    # Sum results
    total = 0
    for need in C:
        if dp[need] >= INF:
            print(-1)
            return
        total += dp[need]
    print(total)

if __name__ == '__main__':
    main()
