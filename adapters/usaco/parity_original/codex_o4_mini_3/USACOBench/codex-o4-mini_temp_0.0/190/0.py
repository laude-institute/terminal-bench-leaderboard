#!/usr/bin/env python3
"""
Compute the minimum number of parentheses to reverse
to make a given string balanced.
"""
import sys

def main():
    s = sys.stdin.readline().strip()
    balance = 0
    flips = 0
    for ch in s:
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        # If too many ')' in prefix, flip one to '('
        if balance < 0:
            flips += 1
            balance = 1
    # Any excess '(' must be flipped half as many times
    flips += balance // 2
    print(flips)

if __name__ == '__main__':
    main()
