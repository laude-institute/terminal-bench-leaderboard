#!/usr/bin/env python3
"""
Compute the minimum number of left-move operations to transform
one permutation a into another permutation b by moving cows left.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # initial lineup and desired lineup
    a = list(map(int, data[1:1+n]))
    b = list(map(int, data[1+n:1+2*n]))
    # map cow ID to its index in a
    pos = {cow: idx for idx, cow in enumerate(a)}
    # track which positions are removed (processed)
    removed = [False] * n
    head = 0  # index of current 'front' in the dynamic list
    moves = 0
    for cow in b:
        idx = pos[cow]
        if idx == head:
            # cow is at front: no move needed
            removed[head] = True
            # advance head to next unremoved
            while head < n and removed[head]:
                head += 1
        else:
            # cow not at front: perform a move
            moves += 1
            removed[idx] = True
    # output result
    print(moves)

if __name__ == '__main__':
    main()
