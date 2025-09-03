#!/usr/bin/env python3
"""
Computes the minimum number of left-move modifications to transform
permutation a into permutation b by finding the longest increasing
subsequence of mapped positions and subtracting its length from N.
"""
import sys
import bisect

def main():
    input = sys.stdin.readline
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Map each cow ID to its position in the initial lineup
    pos = [0] * (N + 1)
    for i, cow in enumerate(a):
        pos[cow] = i
    # Build the sequence of positions for target order
    seq = [pos[cow] for cow in b]
    # Compute LIS length using patience sorting
    tail = []  # tail[i] = smallest ending value of an increasing subsequence of length i+1
    for x in seq:
        idx = bisect.bisect_left(tail, x)
        if idx == len(tail):
            tail.append(x)
        else:
            tail[idx] = x
    # Minimum moves = total cows minus LIS length
    print(N - len(tail))

if __name__ == '__main__':
    main()
