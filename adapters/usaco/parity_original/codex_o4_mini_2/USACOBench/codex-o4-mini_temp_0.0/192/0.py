#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    mod = 2012
    # Compute prefix balances of the entire sequence
    b = [0] * (n + 1)
    for i, c in enumerate(s):
        b[i+1] = b[i] + (1 if c == '(' else -1)

    # dp[h] = number of ways with Holstein balance = h
    curr = [0] * (n + 1)
    curr[0] = 1
    for i, c in enumerate(s):
        next_dp = [0] * (n + 1)
        # Holstein balance h ranges from 0 to b[i]
        for h in range(0, b[i] + 1):
            ways = curr[h]
            if ways == 0:
                continue
            if c == '(':  # open parenthesis: assign to H or G
                next_dp[h+1] = (next_dp[h+1] + ways) % mod
                next_dp[h]   = (next_dp[h] + ways) % mod
            else:  # close parenthesis: assign to H or G if balance permits
                # assign to H if it has an unmatched '('
                if h > 0:
                    next_dp[h-1] = (next_dp[h-1] + ways) % mod
                # assign to G if it has unmatched '('
                g_balance = b[i] - h
                if g_balance > 0:
                    next_dp[h] = (next_dp[h] + ways) % mod
        curr = next_dp

    # Result is ways where both balances are zero
    print(curr[0] % mod)

if __name__ == '__main__':
    main()
