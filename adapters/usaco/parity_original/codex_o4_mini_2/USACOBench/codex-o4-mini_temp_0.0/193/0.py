#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    mod = 2012
    # Quick check: overall parentheses balance must be non-negative in prefixes and end at zero
    balance = 0
    for c in s:
        if c == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            print(0)
            return
    if balance != 0:
        print(0)
        return

    # dp[h] = number of ways with h unmatched '(' assigned to Holsteins
    dp = [0] * (n + 1)
    dp[0] = 1
    current_sum = 0  # total unmatched '(' across both breeds

    for c in s:
        new_dp = [0] * (n + 1)
        if c == '(':
            # Can assign '(' to H (h+1) or G (h stays same)
            for h in range(current_sum + 1):
                v = dp[h]
                if not v:
                    continue
                new_dp[h + 1] = (new_dp[h + 1] + v) % mod
                new_dp[h] = (new_dp[h] + v) % mod
            current_sum += 1
        else:
            # ')' must match a previous '(' in H or G
            for h in range(current_sum + 1):
                v = dp[h]
                if not v:
                    continue
                # match with H if possible
                if h > 0:
                    new_dp[h - 1] = (new_dp[h - 1] + v) % mod
                # match with G if possible: g = current_sum - h
                if current_sum - h > 0:
                    new_dp[h] = (new_dp[h] + v) % mod
            current_sum -= 1
        dp = new_dp

    # After processing, no unmatched '(' remains
    print(dp[0] % mod)

if __name__ == '__main__':
    main()
