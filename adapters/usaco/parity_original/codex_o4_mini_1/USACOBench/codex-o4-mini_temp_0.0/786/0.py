#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    intervals = []
    for i in range(n):
        a = int(next(it)); b = int(next(it))
        intervals.append((a, b, i))

    # Create events: (time, type, id)
    events = []  # type: list[tuple[int, int, int]]
    for a, b, idx in intervals:
        events.append((a, 1, idx))
        events.append((b, -1, idx))
    events.sort(key=lambda x: x[0])

    active = set()
    prev_time = events[0][0]
    total = 0
    unique = [0] * n

    for time, typ, idx in events:
        delta = time - prev_time
        if active:
            total += delta
            if len(active) == 1:
                only = next(iter(active))
                unique[only] += delta
        if typ == 1:
            active.add(idx)
        else:
            active.remove(idx)
        prev_time = time

    # If only one lifeguard, removing it leaves 0 coverage
    if n == 1:
        print(0)
        return

    # Remove lifeguard with minimal unique coverage
    min_unique = min(unique)
    print(total - min_unique)

if __name__ == '__main__':
    main()
