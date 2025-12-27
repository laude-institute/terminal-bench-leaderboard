#!/usr/bin/env python3
"""
Simulate bucket assignment for cow milking to find total buckets needed.
"""
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    events = []  # (time, type, cow_id, buckets_needed)
    for cow_id in range(n):
        s = int(next(it))
        t = int(next(it))
        b = int(next(it))
        events.append((s, 'start', cow_id, b))
        events.append((t, 'end', cow_id, b))
    # Sort events by time (times are distinct)
    events.sort(key=lambda x: x[0])

    available = []  # min-heap of freed bucket labels
    assigned = {}   # cow_id -> list of labels assigned
    next_label = 1  # next new bucket label to use
    max_label = 0   # track highest label used

    for _, typ, cow_id, b in events:
        if typ == 'start':
            labels = []
            for _ in range(b):
                if available:
                    labels.append(heapq.heappop(available))
                else:
                    labels.append(next_label)
                    max_label = max(max_label, next_label)
                    next_label += 1
            assigned[cow_id] = labels
        else:  # 'end'
            # free buckets
            for lbl in assigned.get(cow_id, []):
                heapq.heappush(available, lbl)
            # optional: del assigned[cow_id]

    # Output total buckets needed
    print(max_label)

if __name__ == '__main__':
    main()
