#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    open_count = 0
    result = 0
    for i in range(len(s) - 1):
        if s[i] == '(' and s[i+1] == '(':
            open_count += 1
        if s[i] == ')' and s[i+1] == ')':
            result += open_count
    print(result)

if __name__ == '__main__':
    main()
