#!/usr/bin/env python3
"""
Count contiguous subsequences whose median is at least X.
Approach: map heights >= X to +1, < X to -1, then count subarrays
with non-negative sum via prefix sums and a Fenwick tree.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, X = map(int, data[:2])
    H = list(map(int, data[2:2+N]))
    # Convert heights to +1/-1
    A = [1 if h >= X else -1 for h in H]
    # Build prefix sums
    prefix = [0]
    for a in A:
        prefix.append(prefix[-1] + a)
    # Coordinate compression
    vals = sorted(set(prefix))
    idx = {v: i+1 for i, v in enumerate(vals)}
    size = len(vals) + 2
    # Fenwick (BIT) structure
    bit = [0] * size

    def update(i):
        while i < size:
            bit[i] += 1
            i += i & -i

    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    # Count valid subarrays
    ans = 0
    for p in prefix:
        j = idx[p]
        ans += query(j)
        update(j)
    # Output result
    print(ans)

if __name__ == "__main__":
    main()
