#!/usr/bin/env python3
"""
Bessie Blocks Spelling

Reads 4 blocks (6-letter strings) and N words (length <=4).
For each word, determines if it can be spelled by assigning distinct
blocks to letters such that each block has the required letter.
Prints YES or NO per word.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Read 4 blocks
    blocks = [next(it) for _ in range(4)]
    # Read words
    words = [next(it) for _ in range(n)]

    from itertools import permutations

    for word in words:
        L = len(word)
        found = False
        # try all assignments of distinct blocks
        for perm in permutations(range(4), L):
            valid = True
            for i, bidx in enumerate(perm):
                if word[i] not in blocks[bidx]:
                    valid = False
                    break
            if valid:
                found = True
                break
        sys.stdout.write('YES' if found else 'NO')
        sys.stdout.write("\n")

if __name__ == '__main__':
    main()
