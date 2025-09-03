#!/usr/bin/env python3
"""
Lifeguards problem: maximize coverage after firing one lifeguard.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    intervals = []
    for _ in range(n):
        start = int(next(it))
        end = int(next(it))
        intervals.append((start, end))
    # Build events: (time, type, id), type = 1 for start, -1 for end
    events = []
    for idx, (start, end) in enumerate(intervals):
        events.append((start, 1, idx))
        events.append((end, -1, idx))
    # Sort by time, then end events before start events
    events.sort(key=lambda x: (x[0], x[1]))
    active = set()
    unique = [0] * n
    total_covered = 0
    prev_time = events[0][0]
    for time, typ, idx in events:
        if time > prev_time:
            duration = time - prev_time
            if active:
                total_covered += duration
                if len(active) == 1:
                    only = next(iter(active))
                    unique[only] += duration
            prev_time = time
        # Process event
        if typ == 1:
            active.add(idx)
        else:
            active.remove(idx)
    # If only one lifeguard, firing them leaves zero coverage
    if n == 1:
        print(0)
    else:
        # Remove lifeguard with minimum unique coverage
        min_unique = min(unique)
        print(total_covered - min_unique)

if __name__ == "__main__":
    main()
