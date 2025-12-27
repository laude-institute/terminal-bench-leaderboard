#!/usr/bin/env python3
"""
Compute the minimum number of left-move modifications to transform one permutation into another.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    a = list(map(int, data[1:1+N]))
    b = list(map(int, data[1+N:1+2*N]))
    # Map each cow to its initial position
    posA = [0] * (N + 1)
    for idx, cow in enumerate(a, start=1):
        posA[cow] = idx
    # Collect candidates that don't require an explicit left move
    # i.e., cows whose initial position <= target position
    q = []
    for i, cow in enumerate(b, start=1):
        pos = posA[cow]
        if pos <= i:
            q.append(pos)
    # Find longest increasing subsequence in q
    import bisect
    tail = []  # tail[k] = smallest possible tail of an increasing subseq of length k+1
    for x in q:
        idx = bisect.bisect_left(tail, x)
        if idx == len(tail):
            tail.append(x)
        else:
            tail[idx] = x
    # Result is total cows minus those we can leave unmoved
    result = N - len(tail)
    print(result)

if __name__ == '__main__':
    main()
