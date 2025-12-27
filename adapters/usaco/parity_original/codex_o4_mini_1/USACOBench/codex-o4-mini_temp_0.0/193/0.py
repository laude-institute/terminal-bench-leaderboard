#!/usr/bin/env python3
"""
Balanced Cow Breeds (bbreeds)

Count ways to assign each parenthesis to Holstein or Guernsey
so that each breed's subsequence is a balanced parentheses string.
"""
import sys

def main():
    S = sys.stdin.readline().strip()
    N = len(S)
    MOD = 2012
    # dp_cur[h] = number of ways with h balance in H subsequence
    dp_cur = [0] * (N + 1)
    dp_cur[0] = 1
    pref_balance = 0  # current total '(' minus ')'
    for c in S:
        dp_nxt = [0] * (N + 1)
        for h_prev, ways in enumerate(dp_cur):
            if ways == 0:
                continue
            g_prev = pref_balance - h_prev
            # assign to Holsteins
            if c == '(':  # increase H balance
                dp_nxt[h_prev + 1] = (dp_nxt[h_prev + 1] + ways) % MOD
            else:  # c == ')', need h_prev > 0
                if h_prev > 0:
                    dp_nxt[h_prev - 1] = (dp_nxt[h_prev - 1] + ways) % MOD
            # assign to Guernseys
            if c == '(':  # increase G balance (h stays same)
                dp_nxt[h_prev] = (dp_nxt[h_prev] + ways) % MOD
            else:  # c == ')', need g_prev > 0
                if g_prev > 0:
                    dp_nxt[h_prev] = (dp_nxt[h_prev] + ways) % MOD
        # update for next iteration
        pref_balance += 1 if c == '(' else -1
        dp_cur = dp_nxt
    # result is ways with zero balance in H (and G)
    print(dp_cur[0] % MOD)

if __name__ == '__main__':
    main()
