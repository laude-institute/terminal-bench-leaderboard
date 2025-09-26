#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    n = int(data.readline())
    A = [int(data.readline()) for _ in range(n)]
    work = 0
    # stack of (l, r) inclusive indices
    stack = [(0, n-1)]
    while stack:
        l, r = stack.pop()
        L = r - l + 1
        if L <= 1:
            continue
        # check if segment is non-increasing (monotonic decreasing)
        dec = True
        for i in range(l, r):
            if A[i] < A[i+1]:
                dec = False
                break
        if dec:
            # only splits off one by one
            work += L * (L + 1) // 2 - 1
            continue
        # one bubble sort pass
        B = A[l:r+1]
        for i in range(len(B)-1):
            if B[i] > B[i+1]:
                B[i], B[i+1] = B[i+1], B[i]
        # prefix max
        pref = [0] * len(B)
        mx = B[0]
        for i in range(len(B)):
            if B[i] > mx:
                mx = B[i]
            pref[i] = mx
        # suffix min
        suff = [0] * len(B)
        mn = B[-1]
        for i in range(len(B)-1, -1, -1):
            if B[i] < mn:
                mn = B[i]
            suff[i] = mn
        # find partition points
        parts = []
        for i in range(len(B)-1):
            if pref[i] <= suff[i+1]:
                parts.append(i)
        # count work for this segment
        work += L
        # push subsegments
        start = l
        for idx in parts:
            end = l + idx
            stack.append((start, end))
            start = end + 1
        # last
        stack.append((start, r))
    print(work)

if __name__ == '__main__':
    main()
