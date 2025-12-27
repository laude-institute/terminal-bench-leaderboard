#!/usr/bin/env python3
import sys
import heapq

def main():
    input = sys.stdin.readline
    # Read number of cows
    N = int(input().strip())
    cows = []  # list of (start, end, buckets, index)
    for i in range(N):
        s, t, b = map(int, input().split())
        cows.append((s, t, b, i))
    # Create events: (time, type, cow_index, bucket_count)
    events = []
    for s, t, b, idx in cows:
        events.append((s, 'start', idx, b))
        events.append((t, 'end', idx, b))
    # Sort events by time (times are distinct)
    events.sort(key=lambda x: x[0])
    # Min-heap of available bucket labels
    available = []
    heapq.heapify(available)
    next_label = 1  # next new bucket label
    # Map from cow index to its allocated bucket labels
    cow_buckets = {}
    # Process events in order
    for _, etype, idx, b in events:
        if etype == 'start':
            allocated = []
            # Allocate b smallest available labels
            for _ in range(b):
                if available:
                    allocated.append(heapq.heappop(available))
                else:
                    allocated.append(next_label)
                    next_label += 1
            cow_buckets[idx] = allocated
        else:
            # End event: free the buckets
            for label in cow_buckets.get(idx, []):
                heapq.heappush(available, label)
    # The highest label used is next_label - 1
    print(next_label - 1)

if __name__ == '__main__':
    main()
