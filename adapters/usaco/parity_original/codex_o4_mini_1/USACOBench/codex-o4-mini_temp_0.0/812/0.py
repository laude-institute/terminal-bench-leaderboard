#!/usr/bin/env python3
"""
Manure Teleporter Problem
Compute minimal total driving distance using an optimal teleporter endpoint y.
"""
import sys

def main():
    data = sys.stdin
    n_line = data.readline().strip()
    if not n_line:
        return
    N = int(n_line)
    total_direct = 0
    events = []  # (position, slope change)
    for _ in range(N):
        a_str = data.readline().split()
        if not a_str:
            continue
        a, b = map(int, a_str)
        direct = abs(a - b)
        total_direct += direct
        via0 = abs(a)
        # saving height
        t = direct - via0
        if t > 0:
            # triangle from y in [b-t, b+t]
            events.append((b - t, 1))
            events.append((b, -2))
            events.append((b + t, 1))
    # no teleport benefit
    if not events:
        print(total_direct)
        return
    # sweep line over events to find max savings
    events.sort()
    i = 0
    prev_x = events[0][0]
    slope = 0
    curr_saving = 0
    max_saving = 0
    # initialize slope at first position
    while i < len(events) and events[i][0] == prev_x:
        slope += events[i][1]
        i += 1
    # process remaining events
    while i < len(events):
        x, _ = events[i]
        dx = x - prev_x
        curr_saving += slope * dx
        if curr_saving > max_saving:
            max_saving = curr_saving
        # apply all slope changes at x
        while i < len(events) and events[i][0] == x:
            slope += events[i][1]
            i += 1
        prev_x = x
    # minimal total distance
    result = total_direct - max_saving
    print(result)

if __name__ == '__main__':
    main()
