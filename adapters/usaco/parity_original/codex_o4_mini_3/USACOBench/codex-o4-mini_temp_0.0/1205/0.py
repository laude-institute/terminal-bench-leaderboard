#!/usr/bin/env python3

import sys

def can_spell(word, blocks):
    """
    Return True if 'word' can be spelled using each block at most once.
    'blocks' is a list of sets of characters on each block.
    """
    def dfs(i, used):
        if i == len(word):
            return True
        for b in range(4):
            if not (used >> b) & 1 and word[i] in blocks[b]:
                if dfs(i + 1, used | (1 << b)):
                    return True
        return False
    return dfs(0, 0)

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # Next four tokens are the block faces
    blocks = [set(data[1 + i]) for i in range(4)]
    # Following tokens are the words to check
    words = data[5:5 + n]
    for word in words:
        print("YES" if can_spell(word, blocks) else "NO")

if __name__ == "__main__":
    main()
