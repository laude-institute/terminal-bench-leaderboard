#!/usr/bin/env python3
"""
Problem: cowfind
Count the number of ways to choose a pair of indices x < y such that
the substring at x is '((' and at y is '))'.
"""
import sys

def main():
    s = sys.stdin.readline().strip()
    count_left = 0  # number of '((' seen so far
    result = 0      # total valid pairs
    # Scan through the string, checking each adjacent pair
    for i in range(len(s) - 1):
        if s[i] == '(' and s[i+1] == '(':  # hind legs
            count_left += 1
        elif s[i] == ')' and s[i+1] == ')':  # front legs
            result += count_left
    print(result)

if __name__ == '__main__':
    main()
