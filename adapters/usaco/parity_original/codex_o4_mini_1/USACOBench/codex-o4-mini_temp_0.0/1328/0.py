#!/usr/bin/env python3
import sys

def main():
    t = sys.stdin.readline().strip()
    n = len(t)
    pattern = 'bessie'

    # build next occurrence table
    # next_pos[i][c] = smallest index >= i where t[index] == c, or n if none
    next_pos = [[n] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        next_pos[i] = next_pos[i + 1].copy()
        next_pos[i][ord(t[i]) - 97] = i

    # f[i] = next position after completing one 'bessie' starting at i, or -1
    f = [-1] * n
    children = [[] for _ in range(n + 1)]  # reversed graph

    for i in range(n):
        pos = i
        valid = True
        for ch in pattern:
            idx = ord(ch) - 97
            if pos > n:
                valid = False
                break
            next_i = next_pos[pos][idx]
            if next_i == n:
                valid = False
                break
            pos = next_i + 1
        if not valid:
            continue
        # pos is one past the endpoint of this 'bessie'
        f[i] = pos
        children[pos].append(i)

    # compute subtree sizes in reversed graph
    # size_sub[x] = number of start positions that reach x
    size_sub = [1] * (n + 1)
    for i in range(n + 1):
        for c in children[i]:
            size_sub[i] += size_sub[c]

    # total contribution
    total = 0
    D = n + 1
    for i in range(n):
        if f[i] >= 0:
            total += size_sub[i] * (D - f[i])

    print(total)

if __name__ == '__main__':
    main()
