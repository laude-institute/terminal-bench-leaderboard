#!/usr/bin/env python3
"""
1. Problem Restatement:
   Given lists of possible integer values for variables B, E, S, I, G, O, M,
   count how many assignments make (B+E+S+S+I+E)*(G+O+E+S)*(M+O+O) a multiple of 7.

2. Solution Concept:
   Use modular arithmetic: only sums mod 7 matter. Count how many values of each
   variable are congruent to each remainder mod 7. Then iterate over all
   possible residue assignments (7^7 combinations), compute each factor mod 7,
   and accumulate the product of counts if any factor is 0 mod 7.

3. Pseudocode:
   initialize counts for each var in {B,E,S,I,G,O,M} as array[7]=0
   read N
   for each input line:
       var, val = parse line
       counts[var][val % 7] += 1
   total = 0
   for each tuple of residues (rb, re, rs, ri, rg, ro, rm) in [0..6]^7:
       ways = prod(counts[var][res] for each var,res)
       if ways == 0: continue
       s1 = (rb + 2*re + 2*rs + ri) % 7
       s2 = (rg + ro + re + rs) % 7
       s3 = (rm + 2*ro) % 7
       if s1 == 0 or s2 == 0 or s3 == 0:
           total += ways
   print(total)
"""

import sys
from itertools import product

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Initialize count of residues for each variable
    vars_list = ['B','E','S','I','G','O','M']
    counts = {v: [0]*7 for v in vars_list}
    for _ in range(n):
        var = next(it)
        val = int(next(it))
        counts[var][val % 7] += 1

    total = 0
    # Iterate over all residue assignments
    for rb, re, rs, ri, rg, ro, rm in product(range(7), repeat=7):
        w = (counts['B'][rb] * counts['E'][re] * counts['S'][rs] *
             counts['I'][ri] * counts['G'][rg] * counts['O'][ro] *
             counts['M'][rm])
        if w == 0:
            continue
        # Compute the three sums mod 7
        s1 = (rb + 2*re + 2*rs + ri) % 7
        s2 = (rg + ro + re + rs) % 7
        s3 = (rm + 2*ro) % 7
        if s1 == 0 or s2 == 0 or s3 == 0:
            total += w
    print(total)

if __name__ == '__main__':
    main()
