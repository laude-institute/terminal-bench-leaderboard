#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    idx = 1
    greater = []  # list of lower bounds (G p means x >= p)
    lesser = []   # list of upper bounds (L p means x <= p)
    for _ in range(n):
        typ = data[idx]; p = int(data[idx+1])
        idx += 2
        if typ == 'G':
            greater.append(p)
        else:
            lesser.append(p)
    greater.sort()
    lesser.sort()
    ans = n
    # candidate positions are all given p values
    for p in set(greater + lesser):
        # cows lying from greater constraints: those with p_i > p
        g_viol = len(greater) - bisect.bisect_right(greater, p)
        # cows lying from lesser constraints: those with p_i < p
        l_viol = bisect.bisect_left(lesser, p)
        ans = min(ans, g_viol + l_viol)
    print(ans)

if __name__ == '__main__':
    main()
