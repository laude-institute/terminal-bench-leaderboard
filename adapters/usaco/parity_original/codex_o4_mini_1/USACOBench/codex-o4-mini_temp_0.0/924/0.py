#!/usr/bin/env python3
"""
1. Restate the problem:
   Given N probabilities p_i that each bull accepts an invitation, choose a contiguous
   interval to maximize the probability of exactly one acceptance.

2. Solution idea:
   Use two pointers with a sliding window. For window [l..r], let P0 = product of (1-p_i)
   and S = sum of p_i/(1-p_i). Then probability of exactly one acceptance is P1 = P0 * S.
   As we expand r, update P0 and S. Then while removing the leftmost element improves P1,
   shrink the window.

3. Pseudocode:
   read N
   read p array (scale ints by 1e6)
   left = 0, P0 = 1.0, S = 0.0, maxP1 = 0.0
   for right in 0..N-1:
       compute ratio = p[r]/(1-p[r])
       S += ratio
       P0 *= (1-p[r])
       while left <= right:
           cur = P0 * S
           r_l = 1-p[left]
           ratio_l = p[left]/r_l
           newP0 = P0 / r_l
           newS = S - ratio_l
           if newP0 * newS > cur:
               P0, S = newP0, newS
               left += 1
           else:
               break
       maxP1 = max(maxP1, P0 * S)
   print floor(maxP1 * 1e6) as int
"""
import sys

def main():
    data = sys.stdin
    n = int(data.readline())
    p = [int(data.readline()) / 1e6 for _ in range(n)]
    left = 0
    P0 = 1.0
    S = 0.0
    maxP1 = 0.0
    for right in range(n):
        pr = p[right]
        one_minus = 1.0 - pr
        ratio = pr / one_minus
        S += ratio
        P0 *= one_minus
        # Shrink window if it improves probability
        while left <= right:
            cur = P0 * S
            pl = p[left]
            r_l = 1.0 - pl
            ratio_l = pl / r_l
            newP0 = P0 / r_l
            newS = S - ratio_l
            if newP0 * newS > cur:
                P0, S = newP0, newS
                left += 1
            else:
                break
        maxP1 = max(maxP1, P0 * S)
    # Output scaled by 1e6 and floored
    print(int(maxP1 * 1e6))

if __name__ == '__main__':
    main()
