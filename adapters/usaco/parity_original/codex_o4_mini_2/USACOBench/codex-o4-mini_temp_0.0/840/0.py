#!/usr/bin/env python3
import sys

def bubble_sort_pass(arr):
    """Perform one pass of bubble sort on arr and return the new list."""
    n = len(arr)
    b = arr.copy()
    for i in range(n-1):
        if b[i] > b[i+1]:
            b[i], b[i+1] = b[i+1], b[i]
    return b

def quickish_sort_work(arr):
    """Return total work_counter for quickish_sort on arr."""
    work = 0
    # use stack for iterative processing of segments
    stack = [arr]
    while stack:
        a = stack.pop()
        n = len(a)
        if n <= 1:
            continue
        # repeat bubble passes until a partition point exists
        while True:
            work += n
            b = bubble_sort_pass(a)
            # compute prefix max and suffix min
            pre = [0] * n
            suf = [0] * n
            pre[0] = b[0]
            for i in range(1, n): pre[i] = max(pre[i-1], b[i])
            suf[n-1] = b[n-1]
            for i in range(n-2, -1, -1): suf[i] = min(suf[i+1], b[i])
            # find partition points
            pts = [i for i in range(n-1) if pre[i] <= suf[i+1]]
            if pts:
                # split into segments
                last = 0
                for i in pts:
                    seg = b[last:i+1]
                    if len(seg) > 0:
                        stack.append(seg)
                    last = i+1
                # last segment
                seg = b[last:]
                if len(seg) > 0:
                    stack.append(seg)
                break
            # else continue with a = b for next pass
            a = b
    return work

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    result = quickish_sort_work(arr)
    print(result)

if __name__ == '__main__':
    main()
