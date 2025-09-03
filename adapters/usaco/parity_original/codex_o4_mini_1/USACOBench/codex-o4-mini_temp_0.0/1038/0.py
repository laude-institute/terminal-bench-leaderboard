#!/usr/bin/env python3
import sys

def can_place(intervals, n, D):
    # Greedily place cows with at least D spacing
    count = 1
    last = intervals[0][0]
    for a, b in intervals:
        # next possible position
        pos = max(a, last + D)
        if pos > b:
            continue
        # place cows in this interval
        # we can place multiple cows here
        # but greedy one by one
        n_remaining = n - count
        # number of cows we can place in [pos, b] stepping D
        add = (b - pos) // D + 1
        if add >= n_remaining:
            return True
        count += add
        last = pos + (add - 1) * D
    return count >= n

def main():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    vals = list(map(int, data[2:]))
    intervals = []
    for i in range(0, 2*m, 2):
        a, b = vals[i], vals[i+1]
        intervals.append((a, b))
    intervals.sort()
    # binary search on D
    low, high = 1, (intervals[-1][1] - intervals[0][0]) // (n - 1) + 1
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if can_place(intervals, n, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

if __name__ == '__main__':
    main()
