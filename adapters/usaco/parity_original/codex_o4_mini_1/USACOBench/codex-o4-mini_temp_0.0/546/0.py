#!/usr/bin/env python3
"""
Restatement:
Counts assignments of B,E,S,I,G,O,M given value lists so that the product of (B+E+S+S+I+E)*(G+O+E+S)*(M+O+O) is even.
"""
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    # Count even/odd options for each variable
    cnt = {v: [0, 0] for v in ['B', 'E', 'S', 'I', 'G', 'O', 'M']}
    idx = 1
    for _ in range(N):
        var = data[idx]; val = int(data[idx+1]); idx += 2
        cnt[var][val % 2] += 1
    # Total assignments
    total = 1
    for v in cnt:
        total *= sum(cnt[v])
    # Count assignments where product is odd (all factors odd)
    bad = 0
    for b in (0, 1):
        for e in (0, 1):
            for s in (0, 1):
                for i in (0, 1):
                    for g in (0, 1):
                        for o in (0, 1):
                            for m in (0, 1):
                                # Factor parities
                                f1 = (b + e + i) % 2
                                f2 = (g + o + e + s) % 2
                                f3 = m
                                if f1 == 1 and f2 == 1 and f3 == 1:
                                    ways = (
                                        cnt['B'][b] * cnt['E'][e] * cnt['S'][s] *
                                        cnt['I'][i] * cnt['G'][g] * cnt['O'][o] *
                                        cnt['M'][m]
                                    )
                                    bad += ways
    # Valid = total - odd-product assignments
    print(total - bad)

if __name__ == '__main__':
    main()
