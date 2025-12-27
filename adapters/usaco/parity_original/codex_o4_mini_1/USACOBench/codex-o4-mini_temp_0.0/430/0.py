#!/usr/bin/env python3
"""
Odometer problem solution: counts "interesting" numbers between X and Y.
An "interesting" number has all digits same except one differing digit.
"""
import sys

def main():
    X, Y = map(int, sys.stdin.readline().split())
    strX = str(X)
    strY = str(Y)
    lenX = len(strX)
    lenY = len(strY)
    count = 0
    for L in range(lenX, lenY + 1):
        for d in "0123456789":
            for e in "0123456789":
                if e == d:
                    continue
                for i in range(L):
                    if i == 0 and e == "0":
                        continue
                    if i != 0 and d == "0":
                        continue
                    s = d * L
                    s = s[:i] + e + s[i+1:]
                    n = int(s)
                    if X <= n <= Y:
                        count += 1
    print(count)

if __name__ == "__main__":
    main()
