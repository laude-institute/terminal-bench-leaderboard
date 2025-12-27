#!/usr/bin/env python3
import sys

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline
    W, N = map(int, input().split())
    words = [input().strip() for _ in range(W)]

    # Trie node definition
    class Node:
        __slots__ = ('children', 'count', 'idxs')
        def __init__(self):
            self.children = {}
            self.count = 0
            self.idxs = []  # list of dictionary indices ending here

    root = Node()
    # Build trie and count subtree words
    for i, w in enumerate(words, start=1):
        node = root
        node.count += 1
        for c in w:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            node.count += 1
        node.idxs.append(i)

    # Find k-th word in lex order in subtree rooted at node
    def kth(node, k):
        # Check words ending at this node
        if node.idxs:
            if k <= len(node.idxs):
                return node.idxs[k-1]
            k -= len(node.idxs)
        # Traverse children in sorted order
        for c in sorted(node.children):
            child = node.children[c]
            if child.count < k:
                k -= child.count
            else:
                return kth(child, k)
        return -1

    outputs = []
    for _ in range(N):
        parts = input().split()
        k = int(parts[0])
        prefix = parts[1]
        node = root
        # Traverse to prefix node
        found = True
        for c in prefix:
            if c not in node.children:
                found = False
                break
            node = node.children[c]
        # If prefix not found or too few completions
        if not found or node.count < k:
            outputs.append(-1)
        else:
            outputs.append(kth(node, k))

    print("\n".join(map(str, outputs)))

if __name__ == '__main__':
    main()
