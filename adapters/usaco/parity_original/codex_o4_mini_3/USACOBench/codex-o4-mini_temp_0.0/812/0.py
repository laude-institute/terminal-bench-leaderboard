#!/usr/bin/env python3
"""
Teleporter optimization: choose y minimizing total hauling distance.
For each manure pile (a, b), direct cost D=|a-b|, teleport saves C=D-|a| if >0.
Saving as function of y is max(0, C-|b-y|), sum of these triangular peaks.
Compute events for piecewise-linear sum, sweep to find max total saving G, answer = totalD - G.
"""
import sys

def main():
    data = sys.stdin
    n_line = data.readline().strip()
    if not n_line:
        return
    n = int(n_line)
    total_direct = 0
    events = []  # list of (position, slope_delta)
    for _ in range(n):
        line = data.readline().split()
        a = int(line[0]); b = int(line[1])
        d = abs(a - b)
        total_direct += d
        c = d - abs(a)
        if c > 0:
            # triangular saving of height c at b, spans [b-c, b+c]
            li = b - c
            mi = b
            ri = b + c
            events.append((li, 1))
            events.append((mi, -2))
            events.append((ri, 1))
    if not events:
        print(total_direct)
        return
    # sweep over events sorted by position
    events.sort(key=lambda x: x[0])
    curr_slope = 0
    curr_saving = 0
    max_saving = 0
    prev_x = events[0][0]
    i = 0
    m = len(events)
    while i < m:
        x = events[i][0]
        # accumulate savings up to x
        dx = x - prev_x
        if dx:
            curr_saving += curr_slope * dx
            if curr_saving > max_saving:
                max_saving = curr_saving
        # process all events at x
        while i < m and events[i][0] == x:
            curr_slope += events[i][1]
            i += 1
        prev_x = x
    # result is direct total minus max saving achievable
    print(total_direct - max_saving)

if __name__ == "__main__":
    main()
