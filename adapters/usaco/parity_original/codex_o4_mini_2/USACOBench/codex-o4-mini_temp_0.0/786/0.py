#!/usr/bin/env python3
"""
Solution to the lifeguards problem.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    events = []  # (time, type, index)
    for i in range(N):
        start, end = map(int, input().split())
        # type: 1 for start, -1 for end
        events.append((start, 1, i))
        events.append((end, -1, i))
    # Sort by time; for ties, starts before ends
    events.sort(key=lambda x: (x[0], -x[1]))
    active = set()
    total_covered = 0
    unique_cover = [0] * N
    prev_time = events[0][0]
    for time, typ, idx in events:
        if time > prev_time:
            interval = time - prev_time
            if active:
                total_covered += interval
                # if only one active, it uniquely covers this interval
                if len(active) == 1:
                    only_idx = next(iter(active))
                    unique_cover[only_idx] += interval
            prev_time = time
        # update active set
        if typ == 1:
            active.add(idx)
        else:
            active.remove(idx)
    # fire the lifeguard with minimum unique coverage
    min_unique = min(unique_cover)
    # if all unique_cover are zero, min_unique = 0 -> total_covered
    result = total_covered - min_unique
    print(result)

if __name__ == '__main__':
    main()
