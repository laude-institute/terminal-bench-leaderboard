#!/usr/bin/env python3
import sys

def can_wash(a):
    last = -1
    piles = []  # list of stacks (each is list)
    for x in a:
        # rinse from leftmost stack while its top < x
        while piles and piles[0][-1] < x:
            y = piles[0].pop()
            if y < last:
                return False
            last = y
            if not piles[0]:
                piles.pop(0)
        # place x on leftmost pile with top > x, or new pile
        placed = False
        for p in piles:
            if p[-1] > x:
                p.append(x)
                placed = True
                break
        if not placed:
            piles.append([x])
    # final rinse: empty remaining plates
    while piles:
        y = piles[0].pop()
        if y < last:
            return False
        last = y
        if not piles[0]:
            piles.pop(0)
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    # binary search max k
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_wash(a[:mid]):
            lo = mid
        else:
            hi = mid - 1
    print(lo)

if __name__ == '__main__':
    main()
