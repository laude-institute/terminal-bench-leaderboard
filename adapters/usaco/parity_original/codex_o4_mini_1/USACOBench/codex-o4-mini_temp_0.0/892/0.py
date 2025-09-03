#!/usr/bin/env python3
"""
Solution to Farmer John's sleepy cow sorting problem.

We find the longest increasing suffix of the permutation. The minimum number
of moves equals the number of cows before that suffix.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    p = list(map(int, data[1:1+n]))
    # Find the largest k such that p[k:] is strictly increasing
    # Starting from the end, move k left while p[k-1] < p[k]
    k = n - 1
    while k > 0 and p[k-1] < p[k]:
        k -= 1
    # k is the number of moves needed
    print(k)

if __name__ == '__main__':
    main()
