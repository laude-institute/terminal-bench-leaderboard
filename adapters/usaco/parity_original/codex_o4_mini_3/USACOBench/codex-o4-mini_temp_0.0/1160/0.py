#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    # Count frequencies of interval start and end points
    A = [0] * (m + 1)
    B = [0] * (m + 1)
    for _ in range(n):
        a = int(next(it)); b = int(next(it))
        A[a] += 1
        B[b] += 1
    size = 2 * m
    # Convolution arrays for sums of starts and ends
    cs = [0] * (size + 1)
    ce = [0] * (size + 1)
    # Prepare non-zero entries to speed up convolution
    starts = [(i, v) for i, v in enumerate(A) if v]
    ends = [(i, v) for i, v in enumerate(B) if v]
    # Compute convolution for starts and ends
    for x, ax in starts:
        for y, ay in starts:
            cs[x + y] += ax * ay
    for x, bx in ends:
        for y, by in ends:
            ce[x + y] += bx * by
    # Prefix sums and compute answers for each k
    p1 = 0
    p2 = 0
    out = []
    for k in range(size + 1):
        p1 += cs[k]
        if k > 0:
            p2 += ce[k - 1]
        out.append(str(p1 - p2))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
