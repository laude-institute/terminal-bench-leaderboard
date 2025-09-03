#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    # Try each length k from 1 to n
    for k in range(1, n + 1):
        seen = set()
        unique = True
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
