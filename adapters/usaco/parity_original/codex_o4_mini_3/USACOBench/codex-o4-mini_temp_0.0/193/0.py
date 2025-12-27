#!/usr/bin/env python3
"""
Problem: Balanced Cow Breeds

1. Restatement:
   Given a parentheses string of length N, count the number of ways to assign each parenthesis
   to one of two breeds (H or G) such that the subsequence of parentheses for each breed is
   balanced. Return the count mod 2012.

2. Conceptual Solution:
   Use dynamic programming tracking, at each position i, the number of open parentheses (
   count) for H (h_open) and G (g_open). Exploit that h_open + g_open equals the net balance
   of the prefix. Transition by assigning each '(' to either H or G (incrementing the corresponding
   open count), and for ')' by closing in H or G if possible. Keep states only for possible splits
   of the current prefix balance.

3. Pseudocode:
   read s
   mod = 2012
   dp = [1]  # dp[h_open] with initial balance 0
   balance = 0
   for each char in s:
       if char == '(':
           new_balance = balance + 1
           dp2 = zeros of length new_balance+1
           for h in 0..balance:
               ways = dp[h]
               dp2[h+1] += ways      # assign '(' to H
               dp2[h]   += ways      # assign '(' to G
           balance = new_balance
       else:  # char == ')'
           new_balance = balance - 1
           dp2 = zeros of length new_balance+1
           for h in 0..new_balance:
               dp2[h]   += dp[h+1]  # close in H (h_open must have been >=1)
               dp2[h]   += dp[h]    # close in G (g_open must have been >=1)
           balance = new_balance
       dp = dp2 % mod
   answer = dp[0]
   print(answer)
"""

import sys

def main():
    s = sys.stdin.readline().strip()
    mod = 2012
    n = len(s)

    # dp[h] = ways with h open for H and (balance - h) open for G
    dp = [0] * (n + 2)
    dp[0] = 1
    balance = 0

    for c in s:
        if c == '(':
            balance += 1
            dp2 = [0] * (n + 2)
            # assign '(' to H or G
            for h in range(0, balance):
                ways = dp[h]
                if ways:
                    # to H: h -> h+1
                    dp2[h+1] = (dp2[h+1] + ways) % mod
                    # to G: h unchanged
                    dp2[h]   = (dp2[h] + ways) % mod
            dp = dp2
        else:
            # must close one
            dp2 = [0] * (n + 2)
            # after closing, balance decreases
            for h in range(0, balance + 1):
                # close in H: from h+1 -> h
                dp2[h] = (dp2[h] + dp[h+1]) % mod
                # close in G: from same h
                dp2[h] = (dp2[h] + dp[h]) % mod
            balance -= 1
            dp = dp2

    # result is when no opens remain for H (and G)
    print(dp[0] % mod)

if __name__ == '__main__':
    main()
