#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    unmatched_open = 0
    flips = 0
    for c in s:
        if c == '(':
            unmatched_open += 1
        else:
            if unmatched_open > 0:
                unmatched_open -= 1
            else:
                flips += 1
                unmatched_open += 1
    flips += unmatched_open // 2
    print(flips)

if __name__ == "__main__":
    main()
