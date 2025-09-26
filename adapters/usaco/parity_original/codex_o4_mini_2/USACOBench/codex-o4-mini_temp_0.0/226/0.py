#!/usr/bin/env python3
"""
Solution to 'Painting the Fence'.
Records paint interval endpoints and uses a line sweep to sum
length painted at least K times.
"""
import sys

def main():
    data = sys.stdin
    # Read N (moves) and K (coats threshold)
    line = data.readline().split()
    N, K = int(line[0]), int(line[1])
    events = []  # list of (position, delta) events
    pos = 0
    # Record paint intervals from moves
    for _ in range(N):
        parts = data.readline().split()
        dist = int(parts[0])
        direction = parts[1]
        if direction == 'L':
            new_pos = pos - dist
            start, end = new_pos, pos
        else:
            new_pos = pos + dist
            start, end = pos, new_pos
        # Add sweep-line events
        events.append((start, 1))
        events.append((end, -1))
        pos = new_pos

    # Sort events by position
    events.sort()
    total = 0
    cover = 0
    # Sweep through events
    for i in range(len(events) - 1):
        cover += events[i][1]
        # If coverage >= K, add interval length
        if cover >= K:
            length = events[i+1][0] - events[i][0]
            total += length
    # Output result
    print(total)

if __name__ == '__main__':
    main()
