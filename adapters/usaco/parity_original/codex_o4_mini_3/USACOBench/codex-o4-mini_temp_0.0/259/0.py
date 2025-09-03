#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    bessie_segments = []
    for _ in range(n):
        speed = int(next(it))
        time = int(next(it))
        bessie_segments.append((speed, time))
    elsie_segments = []
    for _ in range(m):
        speed = int(next(it))
        time = int(next(it))
        elsie_segments.append((speed, time))

    # Expand speeds per time unit
    bessie_speeds = []
    for speed, t in bessie_segments:
        bessie_speeds.extend([speed] * t)
    elsie_speeds = []
    for speed, t in elsie_segments:
        elsie_speeds.extend([speed] * t)

    total_time = len(bessie_speeds)
    bessie_dist = 0
    elsie_dist = 0
    prev_leader = 0  # 0 = tie/no leader, 1 = Bessie, 2 = Elsie
    lead_changes = 0

    for i in range(total_time):
        bessie_dist += bessie_speeds[i]
        elsie_dist += elsie_speeds[i]
        if bessie_dist > elsie_dist:
            curr_leader = 1
        elif elsie_dist > bessie_dist:
            curr_leader = 2
        else:
            curr_leader = 0

        # Count change only when switching from one leader to the other
        if curr_leader != 0 and curr_leader != prev_leader and prev_leader != 0:
            lead_changes += 1
        # Update prev_leader when someone is ahead
        if curr_leader != 0:
            prev_leader = curr_leader

    print(lead_changes)

if __name__ == "__main__":
    main()
