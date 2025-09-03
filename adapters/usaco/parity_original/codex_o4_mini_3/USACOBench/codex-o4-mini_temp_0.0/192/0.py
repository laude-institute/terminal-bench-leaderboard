#!/usr/bin/env python3
"""
Balanced Cow Breeds (bbreeds)

Given a parentheses string s of length N, count the number of ways to assign each parenthesis
to one of two breeds (H or G) such that the subsequence of parentheses assigned to each breed
is balanced. Output the count modulo 2012.
"""
import sys

def main():
    MOD = 2012
    s = sys.stdin.readline().strip()
    # Quick check: ensure global string never goes negative and ends at zero
    bal = 0
    for c in s:
        if c == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            print(0)
            return
    if bal != 0:
        print(0)
        return

    # dp[j] = number of ways with H-balance = j, G-balance = current_bal - j
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    current_bal = 0

    for c in s:
        if c == '(':
            # balance increases by 1
            current_bal += 1
            new_dp = [0] * (current_bal + 1)
            for j in range(current_bal):
                v = dp[j]
                if v:
                    # assign '(' to G: H-balance remains j
                    new_dp[j] = (new_dp[j] + v) % MOD
                    # assign '(' to H: H-balance increases
                    new_dp[j+1] = (new_dp[j+1] + v) % MOD
            dp = new_dp
        else:
            # balance decreases by 1
            new_bal = current_bal - 1
            new_dp = [0] * (new_bal + 1)
            for j in range(current_bal + 1):
                v = dp[j]
                if not v:
                    continue
                # assign ')' to H: H-balance must be >=1
                if j >= 1:
                    new_dp[j-1] = (new_dp[j-1] + v) % MOD
                # assign ')' to G: G-balance must be >=1 -> current_bal - j >= 1
                if j <= new_bal:
                    new_dp[j] = (new_dp[j] + v) % MOD
            dp = new_dp
            current_bal = new_bal

    # both balances zero means H-balance == 0
    print(dp[0] % MOD)

if __name__ == '__main__':
    main()
