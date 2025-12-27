#!/usr/bin/env python3
"""
Solution for Poker Hands problem.
Compute the minimum number of straights needed to remove all cards.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    counts = list(map(int, data[1:1+n]))
    prev = 0
    total_straights = 0
    for count in counts:
        if count > prev:
            total_straights += count - prev
        prev = count
    print(total_straights)

if __name__ == '__main__':
    main()
