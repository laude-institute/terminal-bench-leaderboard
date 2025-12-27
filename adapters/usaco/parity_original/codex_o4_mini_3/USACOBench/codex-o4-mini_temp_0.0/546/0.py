#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # counts[var] = [even_count, odd_count]
    counts = {v: [0, 0] for v in ['B', 'E', 'S', 'I', 'G', 'O', 'M']}
    for _ in range(n):
        var = next(it)
        val = int(next(it))
        counts[var][val & 1] += 1

    # unpack counts
    Be, Bo = counts['B'][0], counts['B'][1]
    Ee, Eo = counts['E'][0], counts['E'][1]
    Se, So = counts['S'][0], counts['S'][1]
    Ie, Io = counts['I'][0], counts['I'][1]
    Ge, Go = counts['G'][0], counts['G'][1]
    Oe, Oo = counts['O'][0], counts['O'][1]
    Me, Mo = counts['M'][0], counts['M'][1]

    # total assignments
    total = (Be+Bo) * (Ee+Eo) * (Se+So) * (Ie+Io) * (Ge+Go) * (Oe+Oo) * (Me+Mo)

    # assignments where factor1 = B+I odd
    BI_odd = Be * Io + Bo * Ie

    # assignments where factor2 = G+O+E+S odd
    GOES_total = (Ge+Go) * (Oe+Oo) * (Ee+Eo) * (Se+So)
    # diff = product of (even - odd) for each
    diff = (Ge - Go) * (Oe - Oo) * (Ee - Eo) * (Se - So)
    GOES_odd = (GOES_total - diff) // 2

    # assignments where factor3 = M odd
    M_odd = Mo

    # assignments where all factors odd
    odd_all = BI_odd * GOES_odd * M_odd

    # result: total minus assignments that are all odd
    print(total - odd_all)

if __name__ == '__main__':
    main()
