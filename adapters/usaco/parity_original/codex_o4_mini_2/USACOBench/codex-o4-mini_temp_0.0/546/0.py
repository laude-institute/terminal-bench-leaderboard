#!/usr/bin/env python3
"""
Count the number of assignments to variables B,E,S,I,G,O,M
that make (B+E+S+S+I+E)*(G+O+E+S)*(M+O+O) even.
No external libraries used.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # Parity counts: index 0 for even, 1 for odd
    counts = {v: [0, 0] for v in ['B', 'E', 'S', 'I', 'G', 'O', 'M']}
    idx = 1
    for _ in range(n):
        var = data[idx]; val = int(data[idx+1]); idx += 2
        counts[var][val & 1] += 1

    # Unpack counts
    be, bo = counts['B']
    ee, eo = counts['E']
    se, so = counts['S']
    ie, io = counts['I']
    ge, go = counts['G']
    oe, oo = counts['O']
    me, mo = counts['M']

    # Total assignments
    total = (
        (be + bo) * (ee + eo) * (se + so) *
        (ie + io) * (ge + go) * (oe + oo) * (me + mo)
    )

    # Factor1 = B + I mod2; odd when one even one odd
    f1_odd = be * io + bo * ie

    # Factor2 = G+O+E+S mod2; count odd-sum combos
    total2 = (ge + go) * (oe + oo) * (ee + eo) * (se + so)
    diff = (ge - go) * (oe - oo) * (ee - eo) * (se - so)
    f2_odd = (total2 - diff) // 2

    # Factor3 = M mod2; odd when M is odd
    f3_odd = mo

    # Assignments where all factors odd => product odd
    odd_assignments = f1_odd * f2_odd * f3_odd

    # Even product when not all factors odd
    print(total - odd_assignments)

if __name__ == '__main__':
    main()
