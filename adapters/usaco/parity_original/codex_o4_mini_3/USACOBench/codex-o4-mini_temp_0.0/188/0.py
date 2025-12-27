#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    # Quick check: total balance
    bal = [0] * (n + 1)
    for i, ch in enumerate(s, start=1):
        bal[i] = bal[i-1] + (1 if ch == '(' else -1)
    total = bal[n]
    # Only possible if total balance is +/-2
    if total not in (2, -2):
        print(0)
        return
    # prefix minima
    pref_min = [0] * (n + 1)
    pref_min[0] = bal[0]
    for i in range(1, n+1):
        pref_min[i] = min(pref_min[i-1], bal[i])
    # suffix minima of bal
    suff_min = [0] * (n + 2)
    INF = 10**9
    suff_min[n+1] = INF
    # For suffix starting at i, we consider bal[i]..bal[n]
    suff_min[n] = bal[n]
    for i in range(n-1, -1, -1):
        suff_min[i] = min(bal[i], suff_min[i+1])
    ans = 0
    # If total == 2, flip '(' to ')': later balances drop by 2 -> need suff_min[i] >= 2
    if total == 2:
        for i, ch in enumerate(s, start=1):
            if ch == '(':
                if pref_min[i-1] >= 0 and suff_min[i] >= 2:
                    ans += 1
    else:
        # total == -2, flip ')' to '(': later balances rise by 2 -> need suff_min[i] >= -2
        for i, ch in enumerate(s, start=1):
            if ch == ')':
                if pref_min[i-1] >= 0 and suff_min[i] >= -2:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
