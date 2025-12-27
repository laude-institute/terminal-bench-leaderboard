#!/usr/bin/env python3
import sys

def can_spell(word, blocks):
    # backtracking to assign each letter to a distinct block
    L = len(word)
    used = [False] * len(blocks)

    def dfs(pos):
        if pos == L:
            return True
        ch = word[pos]
        for i in range(len(blocks)):
            if not used[i] and ch in blocks[i]:
                used[i] = True
                if dfs(pos+1):
                    return True
                used[i] = False
        return False

    return dfs(0)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    blocks = []
    for _ in range(4):
        blocks.append(set(next(it).strip()))
    for _ in range(n):
        word = next(it).strip()
        print('YES' if can_spell(word, blocks) else 'NO')

if __name__ == '__main__':
    main()
