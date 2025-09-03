#!/usr/bin/env python3
import sys

# Increase recursion limit for deep tries
sys.setrecursionlimit(1000000)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.indices = []

def insert(root, word, index):
    node = root
    node.count += 1
    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
        node.count += 1
    node.indices.append(index)

def find_kth(node, k):
    # Check words ending at this node
    if node.indices:
        if k <= len(node.indices):
            return node.indices[k-1]
        k -= len(node.indices)
    # Traverse children in lex order
    for ch in sorted(node.children):
        child = node.children[ch]
        if k <= child.count:
            return find_kth(child, k)
        k -= child.count
    return -1

def main():
    data = sys.stdin
    W, N = map(int, data.readline().split())
    root = TrieNode()
    # Build trie
    for i in range(1, W+1):
        word = data.readline().strip()
        insert(root, word, i)

    # Process queries
    results = []
    for _ in range(N):
        line = data.readline().split()
        k = int(line[0])
        prefix = line[1]
        node = root
        found = True
        for ch in prefix:
            if ch not in node.children:
                found = False
                break
            node = node.children[ch]
        if not found or node.count < k:
            results.append(-1)
        else:
            results.append(find_kth(node, k))

    # Output results
    print("\n".join(map(str, results)))

if __name__ == '__main__':
    main()
