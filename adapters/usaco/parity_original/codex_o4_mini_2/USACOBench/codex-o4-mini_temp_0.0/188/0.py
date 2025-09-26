#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    # Compute prefix sums: '(' -> +1, ')' -> -1
    pref = [0] * (n + 1)
    for i, c in enumerate(s, start=1):
        pref[i] = pref[i - 1] + (1 if c == '(' else -1)
    total = pref[n]
    # Only flips changing total by +/-2 can balance
    if abs(total) != 2:
        print(0)
        return
    # Compute prefix minimums
    pre_min = [0] * (n + 1)
    pre_min[0] = 0
    for i in range(1, n + 1):
        pre_min[i] = min(pre_min[i - 1], pref[i])
    # Compute suffix minimums of prefix sums
    suf_min = [0] * (n + 2)
    INF = 10**9
    suf_min[n + 1] = INF
    for i in range(n, 0, -1):
        suf_min[i] = pref[i] if i == n else min(pref[i], suf_min[i + 1])
    # Count valid flips
    ans = 0
    if total == 2:
        # Need to flip '(' -> ')'
        for i in range(1, n + 1):
            if s[i - 1] == '(' and pre_min[i - 1] >= 0 and suf_min[i] >= 2:
                ans += 1
    else:
        # total == -2, flip ')' -> '('
        for i in range(1, n + 1):
            if s[i - 1] == ')' and pre_min[i - 1] >= 0 and suf_min[i] >= -2:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
