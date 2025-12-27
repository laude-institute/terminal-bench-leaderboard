#!/usr/bin/env python3
"""
Cow FizzBuzz (Moo) problem:
Find the Nth number not divisible by 3 or 5.
"""

import sys

def count_spoken(k):
    # Count numbers from 1..k not divisible by 3 or 5
    return k - k//3 - k//5 + k//15

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    # Binary search for minimal k with count_spoken(k) >= N
    lo, hi = 1, 2 * N + 10
    while lo < hi:
        mid = (lo + hi) // 2
        if count_spoken(mid) >= N:
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == '__main__':
    main()
