#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    N, M = map(int, data.readline().split())
    intervals = []
    for _ in range(M):
        a, b = map(int, data.readline().split())
        intervals.append((a, b))
    # sort intervals by start
    intervals.sort()

    # check if we can place N cows with minimum distance D
    def can_place(D):
        count = 1
        last = intervals[0][0]
        for a, b in intervals:
            # next possible position in this interval
            pos = max(last + D, a)
            # place as many cows as fit in [a, b]
            while pos <= b:
                count += 1
                last = pos
                if count >= N:
                    return True
                pos = last + D
        return False

    # binary search for largest D
    low, high = 1, intervals[-1][1] - intervals[0][0]
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    print(best)

if __name__ == '__main__':
    main()
