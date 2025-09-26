#!/usr/bin/env python3
"""
Solution to the Clumsy Cows problem:
Compute the minimum number of reversals to balance a parentheses string.
"""
import sys

def main():
    s = sys.stdin.readline().strip()
    balance = 0
    reversals = 0
    # Scan the string, treating unmatched ')' by reversing it to '('
    for c in s:
        if c == '(':
            balance += 1
        else:  # c == ')'
            if balance > 0:
                balance -= 1
            else:
                # Reverse this ')' to '('
                reversals += 1
                balance += 1
    # Any remaining '(' require half of them to be reversed to ')'
    reversals += balance // 2
    print(reversals)

if __name__ == '__main__':
    main()
