#!/usr/bin/env python3
"""
Reads N constraints (each 'L p' or 'G p') and finds the minimum number of
cows whose statements are inconsistent with some hiding position x on the number line.
Computes the minimum liars by testing each candidate x among all p_i values.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    L = []  # constraints x <= p_i
    G = []  # constraints x >= p_i
    for _ in range(N):
        typ, p = input().split()
        p = int(p)
        if typ == 'L':
            L.append(p)
        else:
            G.append(p)
    # candidate positions are all given p values
    candidates = set(L) | set(G)
    ans = N
    # for each candidate x, count liars
    for x in candidates:
        # liars: L constraints with p < x, G constraints with p > x
        liars = sum(1 for p in L if p < x) + sum(1 for p in G if p > x)
        if liars < ans:
            ans = liars
    print(ans)

if __name__ == '__main__':
    main()
