#!/usr/bin/env python3
"""
Solution to the Flowerpot problem:
Find the minimum width W of an x-interval such that among raindrops inside,
the time difference between the earliest and latest drop is at least D.
"""
import sys
import heapq
from collections import Counter

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    try:
        n = int(next(it))
        D = int(next(it))
    except StopIteration:
        return
    points = []  # list of (x, y)
    for _ in range(n):
        x = int(next(it)); y = int(next(it))
        points.append((x, y))
    # Sort drops by x-coordinate
    points.sort(key=lambda p: p[0])

    l = 0
    ans = float('inf')
    cnt = Counter()
    minheap = []  # holds y
    maxheap = []  # holds -y for max

    for r in range(n):
        x_r, y_r = points[r]
        cnt[y_r] += 1
        heapq.heappush(minheap, y_r)
        heapq.heappush(maxheap, -y_r)

        # Try to shrink window while condition holds
        while l <= r:
            # Clean up invalidated entries
            while minheap and cnt[minheap[0]] == 0:
                heapq.heappop(minheap)
            while maxheap and cnt[-maxheap[0]] == 0:
                heapq.heappop(maxheap)
            if not minheap or not maxheap:
                break
            cur_min = minheap[0]
            cur_max = -maxheap[0]
            if cur_max - cur_min >= D:
                # Update width
                ans = min(ans, points[r][0] - points[l][0])
                # Remove leftmost point
                y_l = points[l][1]
                cnt[y_l] -= 1
                l += 1
            else:
                break

    # Output result
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
