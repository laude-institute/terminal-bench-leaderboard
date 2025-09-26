#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    N, M = map(int, data.readline().split())
    intervals = []
    for _ in range(M):
        a, b = map(int, data.readline().split())
        intervals.append((a, b))
    intervals.sort()

    def can_place(d):
        count = 0
        last = -10**30  # very small
        for a, b in intervals:
            # first possible position in this interval
            start = a if count == 0 else max(a, last + d)
            # place as many cows as possible
            while start <= b:
                count += 1
                last = start
                if count >= N:
                    return True
                start += d
        return False

    # binary search max D
    lo, hi = 1, intervals[-1][1] - intervals[0][0]
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_place(mid):
            lo = mid
        else:
            hi = mid - 1
    print(lo)

if __name__ == '__main__':
    main()
