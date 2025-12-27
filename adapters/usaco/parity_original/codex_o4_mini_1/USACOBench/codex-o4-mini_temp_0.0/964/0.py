#!/usr/bin/env python3
"""
Solution for mailbox substring uniqueness problem.
Reads N and string s, finds minimum K such that all substrings
of length K are unique.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    # Try each length K from 1 to n
    for k in range(1, n + 1):
        seen = set()
        unique = True
        # Check all substrings of length k
        for i in range(n - k + 1):
            sub = s[i:i + k]
            if sub in seen:
                unique = False
                break
            seen.add(sub)
        if unique:
            print(k)
            return

if __name__ == '__main__':
    main()
