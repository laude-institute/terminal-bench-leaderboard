#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    C = int(data[0]); N = int(data[1])
    teams = []
    # Convert each team string to a bitmask
    for i in range(N):
        s = data[2 + i]
        mask = 0
        for ch in s:
            mask = (mask << 1) | (1 if ch == 'H' else 0)
        teams.append(mask)

    # Build a binary trie of all masks
    children = [[-1, -1]]  # each node: [child0, child1]
    for mask in teams:
        node = 0
        for pos in range(C - 1, -1, -1):
            bit = (mask >> pos) & 1
            if children[node][bit] == -1:
                children[node][bit] = len(children)
                children.append([-1, -1])
            node = children[node][bit]

    # For each team, traverse trie to maximize Hamming distance
    out = []
    for mask in teams:
        node = 0
        dist = 0
        for pos in range(C - 1, -1, -1):
            bit = (mask >> pos) & 1
            opp = bit ^ 1
            if children[node][opp] != -1:
                dist += 1
                node = children[node][opp]
            else:
                node = children[node][bit]
        out.append(str(dist))

    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
