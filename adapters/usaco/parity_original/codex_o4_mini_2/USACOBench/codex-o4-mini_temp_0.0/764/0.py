#!/usr/bin/env python3
"""
Solution to the Bovine Shuffle problem:
Count positions that always contain cows after infinite shuffles,
i.e., the total number of nodes in cycles of the directed graph.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = [0] + list(map(int, data[1:]))
    color = [0] * (n + 1)  # 0=unvisited,1=visiting,2=visited
    ans = 0
    for u in range(1, n + 1):
        if color[u] != 0:
            continue
        stack = []
        curr = u
        # traverse until we hit a visited node
        while color[curr] == 0:
            color[curr] = 1
            stack.append(curr)
            curr = a[curr]
        # if we found a cycle (curr is in current path)
        if color[curr] == 1:
            # count cycle size
            cnt = 1
            idx = len(stack) - 1
            while stack[idx] != curr:
                cnt += 1
                idx -= 1
            ans += cnt
        # mark path nodes as fully visited
        for node in stack:
            color[node] = 2
    print(ans)

if __name__ == '__main__':
    main()
