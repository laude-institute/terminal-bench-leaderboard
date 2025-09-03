#!/usr/bin/env python3
"""
Solution to the milking order problem.
"""
import sys

def can_place(N, social, fixed, pos):
    # Attempt to build an order with cow 1 at position pos
    order = [0] * (N + 1)
    occupied = [False] * (N + 1)
    # place fixed cows
    for cow, p in fixed.items():
        order[p] = cow
        occupied[p] = True
    # place cow 1
    order[pos] = 1
    occupied[pos] = True
    cur = 1
    for cow in social:
        # determine if cow has a fixed position
        if cow == 1 or cow in fixed:
            p = pos if cow == 1 else fixed[cow]
            # must respect order
            if p < cur:
                return False
            cur = p + 1
        else:
            # find next free slot
            while cur <= N and occupied[cur]:
                cur += 1
            if cur > N:
                return False
            occupied[cur] = True
            cur += 1
    return True

def main():
    data = sys.stdin.read().split()
    N, M, K = map(int, data[:3])
    idx = 3
    social = list(map(int, data[idx:idx+M])); idx += M
    fixed = {}
    for _ in range(K):
        c = int(data[idx]); p = int(data[idx+1]); idx += 2
        fixed[c] = p
    # if cow 1 has fixed position, that's the answer
    if 1 in fixed:
        print(fixed[1])
        return
    # try earliest possible position
    for pos in range(1, N + 1):
        # skip if occupied by other fixed cow
        if pos in fixed.values():
            continue
        if can_place(N, social, fixed, pos):
            print(pos)
            return

if __name__ == '__main__':
    main()
