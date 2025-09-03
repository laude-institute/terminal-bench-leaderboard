#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0].strip()
    costs = list(map(int, data[1:]))
    n = len(s)
    T = "bessie"
    L = len(T)

    # Precompute automaton transitions (no overlaps in "bessie")
    # failure function: all proper prefixes that are suffix and start char
    # Since "bessie" has no border, fail is 0 except when char=='b'
    # For state j (0..L) and char c, compute next state and match increment
    trans = [[0] * 26 for _ in range(L+1)]
    for j in range(L+1):
        for ci in range(26):
            c = chr(ci + ord('a'))
            nj = 0
            if j < L and c == T[j]:
                nj = j + 1
            else:
                # if mismatch, check if c matches first char
                if c == T[0]:
                    nj = 1
                else:
                    nj = 0
            trans[j][ci] = nj

    # dp[j] = (matches, -cost)
    dp = [(-10**18, -10**18)] * (L+1)
    dp[0] = (0, 0)

    for i, ch in enumerate(s):
        ci = ord(ch) - ord('a')
        cost = costs[i]
        ndp = [(-10**18, -10**18)] * (L+1)
        for j in range(L+1):
            m, negc = dp[j]
            # delete
            opt_del = (m, negc - cost)
            if opt_del > ndp[j]:
                ndp[j] = opt_del
            # keep
            nj = trans[j][ci]
            add = 0
            if nj == L:
                # complete match
                add = 1
                nj = 0
            opt_keep = (m + add, negc)
            if opt_keep > ndp[nj]:
                ndp[nj] = opt_keep
        dp = ndp

    # extract best
    best = max(dp)
    matches, negcost = best
    print(matches)
    print(-negcost)

if __name__ == '__main__':
    main()
