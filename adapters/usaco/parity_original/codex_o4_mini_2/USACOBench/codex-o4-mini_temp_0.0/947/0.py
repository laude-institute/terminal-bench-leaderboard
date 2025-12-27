#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    A = list(map(int, (next(it) for _ in range(2*N))))
    # compute inversions in first half
    inv1 = 0
    ones = 0
    for i in range(N):
        if A[i] == 1:
            ones += 1
        else:
            inv1 += ones
    # compute inversions in second half
    inv2 = 0
    ones = 0
    for i in range(N, 2*N):
        if A[i] == 1:
            ones += 1
        else:
            inv2 += ones
    diff = inv1 - inv2
    # if already tied
    if diff == 0:
        print(0)
        return
    # count ones in positions 0..N-2 and zeros in positions N+1..2N-1
    o1 = sum(A[:N-1])
    z2 = (N-1) - sum(A[N+1:])
    ans = abs(diff)
    # boundary swap possible if bits differ
    if A[N-1] != A[N]:
        delta = z2 - o1
        # cost 1 + |new_diff|
        cand = 1 + abs(diff + delta)
        # or exactly 1 if it ties
        if diff + delta == 0:
            cand = 1
        ans = min(ans, cand)
    print(ans)

if __name__ == '__main__':
    main()
