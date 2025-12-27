#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    bales = []  # list of (position, size)
    for _ in range(N):
        s = int(next(it))
        p = int(next(it))
        bales.append((p, s))
    # sort by position
    bales.sort()
    positions = [p for p, _ in bales]
    sizes = [s for _, s in bales]
    intervals = []
    # find trapping intervals
    for i in range(N - 1):
        pi = positions[i]
        si = sizes[i]
        right_limit = pi + si
        furthest = pi
        # scan j until beyond run-up limit
        for j in range(i + 1, N):
            pj = positions[j]
            if pj > right_limit:
                break
            # can break right bale?
            if pj - sizes[j] <= pi:
                if pj > furthest:
                    furthest = pj
        if furthest > pi:
            intervals.append((pi, furthest))
    # merge intervals and sum lengths
    if not intervals:
        print(0)
        return
    intervals.sort()
    total = 0
    cur_start, cur_end = intervals[0]
    for s, e in intervals[1:]:
        if s > cur_end:
            total += cur_end - cur_start
            cur_start, cur_end = s, e
        else:
            if e > cur_end:
                cur_end = e
    total += cur_end - cur_start
    print(total)

if __name__ == '__main__':
    main()
