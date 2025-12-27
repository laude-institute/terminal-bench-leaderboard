#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    sizes = list(map(int, data[1:1+n]))
    total = sum(sizes)
    # Sort bales descending for better pruning
    sizes.sort(reverse=True)

    best = total
    bins = [0, 0, 0]

    sys.setrecursionlimit(10000)
    def dfs(idx):
        nonlocal best
        if idx == n:
            current_max = max(bins)
            if current_max < best:
                best = current_max
            return
        s = sizes[idx]
        seen = set()
        for i in range(3):
            # skip same-sum bins to avoid symmetric states
            if bins[i] in seen:
                continue
            seen.add(bins[i])
            bins[i] += s
            # prune if current max already >= best
            if max(bins) < best:
                dfs(idx + 1)
            bins[i] -= s

    dfs(0)
    print(best)

if __name__ == '__main__':
    main()
