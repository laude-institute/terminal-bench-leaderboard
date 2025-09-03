#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    events = []  # (x, type, y_low, y_high)
    for _ in range(n):
        x1 = int(next(it)); y1 = int(next(it))
        x2 = int(next(it)); y2 = int(next(it))
        y_low = min(y1, y2)
        y_high = max(y1, y2)
        events.append((x1, 1, y_low, y_high))  # rectangle enters
        events.append((x2, -1, y_low, y_high)) # rectangle leaves
    # sort events by x
    events.sort(key=lambda e: e[0])
    def union_length(intervals):
        if not intervals:
            return 0
        # merge intervals
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        total = 0
        curr_start, curr_end = intervals_sorted[0]
        for s, e in intervals_sorted[1:]:
            if s > curr_end:
                total += curr_end - curr_start
                curr_start, curr_end = s, e
            else:
                curr_end = max(curr_end, e)
        total += curr_end - curr_start
        return total

    active = []  # list of (y_low, y_high)
    prev_x = events[0][0]
    area = 0
    for x, typ, y1, y2 in events:
        dx = x - prev_x
        if dx:
            covered_y = union_length(active)
            area += covered_y * dx
            prev_x = x
        if typ == 1:
            active.append((y1, y2))
        else:
            # remove one matching interval
            active.remove((y1, y2))
    # output result
    print(area)

if __name__ == '__main__':
    main()
