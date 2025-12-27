#!/usr/bin/env python3
"""
1. Restatement:
   There are N cows each occupying a disjoint interval of stalls [s_i, t_i] with a required cooling c_i.
   There are M air conditioners, each covering an interval [a_j, b_j] and providing p_j cooling at cost m_j.
   Choose a subset of air conditioners with minimum total cost so that for every stall occupied by each cow,
   the combined cooling from selected air conditioners is at least c_i.

2. Conceptual Solution:
   Since M <= 10, we can enumerate all subsets of air conditioners (up to 2^10 = 1024).
   For each subset, compute the cooling at each stall (1..100) by summing p_j for selected conditioners.
   Then check each cow’s occupied stalls to ensure the cooling at every stall in its range >= c_i.
   Track the minimum cost among all feasible subsets.

3. Pseudocode:
   read N, M
   read cows: list of (s_i, t_i, c_i)
   read ACs: list of (a_j, b_j, p_j, m_j)
   ans = infinity
   for each mask in 0..(1<<M)-1:
       cost = sum of m_j for j where mask bit j is set
       if cost >= ans: continue
       cooling = array[1..100] initialized to 0
       for each j in 0..M-1:
           if mask has bit j:
               for x in a_j..b_j: cooling[x] += p_j
       valid = true
       for each cow (s_i, t_i, c_i):
           for x in s_i..t_i:
               if cooling[x] < c_i:
                   valid = false; break
           if not valid: break
       if valid: ans = cost
   print(ans)
"""

import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    cows = []
    for _ in range(N):
        s = int(next(it)); t = int(next(it)); c = int(next(it))
        cows.append((s, t, c))
    acs = []
    for _ in range(M):
        a = int(next(it)); b = int(next(it)); p = int(next(it)); m = int(next(it))
        acs.append((a, b, p, m))

    INF = 10**18
    ans = INF
    # Enumerate all subsets of air conditioners
    for mask in range(1 << M):
        cost = 0
        for j in range(M):
            if (mask >> j) & 1:
                cost += acs[j][3]
        if cost >= ans:
            continue
        # compute cooling per stall
        cooling = [0] * 101
        for j in range(M):
            if (mask >> j) & 1:
                a, b, p, m = acs[j]
                for x in range(a, b + 1):
                    cooling[x] += p
        # validate cows
        valid = True
        for s, t, c in cows:
            for x in range(s, t + 1):
                if cooling[x] < c:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            ans = cost

    print(ans)

if __name__ == '__main__':
    main()
