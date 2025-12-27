#!/usr/bin/env python3
import sys
import heapq

def main():
    input = sys.stdin.readline
    N = int(input())
    cows = []
    for i in range(N):
        s, t, b = map(int, input().split())
        cows.append((s, t, b))

    events = []
    for i, (s, t, b) in enumerate(cows):
        events.append((s, 1, i))   # start event
        events.append((t, -1, i))  # end event

    events.sort()
    free_buckets = []
    used = {}
    max_label = 0

    for _, typ, idx in events:
        s, t, b = cows[idx]
        if typ == -1:
            # end of milking: free buckets
            for label in used[idx]:
                heapq.heappush(free_buckets, label)
            del used[idx]
        else:
            # start of milking: allocate buckets
            allocated = []
            for _ in range(b):
                if free_buckets:
                    allocated.append(heapq.heappop(free_buckets))
                else:
                    max_label += 1
                    allocated.append(max_label)
            allocated.sort()
            used[idx] = allocated

    print(max_label)

if __name__ == "__main__":
    main()
