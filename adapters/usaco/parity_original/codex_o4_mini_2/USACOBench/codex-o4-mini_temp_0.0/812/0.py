#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    N = int(data.readline().strip())
    events = []  # list of (y, delta_slope)
    total_direct = 0
    for _ in range(N):
        a, b = map(int, data.readline().split())
        direct = abs(a - b)
        total_direct += direct
        # teleport path saves if |b-y| < direct - |a|
        savings_thresh = direct - abs(a)
        if savings_thresh > 0:
            # interval where teleport is better: (b - thresh, b + thresh)
            l = b - savings_thresh
            m = b
            r = b + savings_thresh
            events.append((l, -1))
            events.append((m, 2))
            events.append((r, -1))
    # if no beneficial intervals, no teleporter use
    if not events:
        print(total_direct)
        return
    # sort events by position
    events.sort()
    # sweep line
    f = total_direct
    slope = 0
    result = f
    prev_y = events[0][0]
    i = 0
    n_events = len(events)
    while i < n_events:
        y = events[i][0]
        # update f to position y
        dy = y - prev_y
        f += slope * dy
        if f < result:
            result = f
        # process all events at y
        while i < n_events and events[i][0] == y:
            slope += events[i][1]
            i += 1
        prev_y = y
    # print minimal cost
    print(result)

if __name__ == '__main__':
    main()
