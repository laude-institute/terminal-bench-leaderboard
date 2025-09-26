#!/usr/bin/env python3
"""
Solution to the Poker Hands problem (USACO 2011).
Computes the minimal number of straights needed to play all cards.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    prev = 0
    result = 0
    for _ in range(n):
        a_i = int(next(it))
        if a_i > prev:
            result += a_i - prev
        prev = a_i
    print(result)

if __name__ == '__main__':
    main()
