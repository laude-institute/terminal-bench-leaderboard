#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    L = int(next(it))
    c = [int(next(it)) for _ in range(N)]
    c.sort()

    def can(h):
        # count papers with citations >= h
        idx = bisect.bisect_left(c, h)
        count1 = N - idx
        if count1 >= h:
            return True
        # need extra citations for papers with c == h-1
        needed = h - count1
        if needed > L:
            return False
        left = bisect.bisect_left(c, h-1)
        right = bisect.bisect_right(c, h-1)
        count2 = right - left
        return count2 >= needed

    # binary search maximum h
    lo, hi = 0, N + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid):
            lo = mid + 1
        else:
            hi = mid
    # result is lo-1
    print(lo - 1)

if __name__ == "__main__":
    main()
