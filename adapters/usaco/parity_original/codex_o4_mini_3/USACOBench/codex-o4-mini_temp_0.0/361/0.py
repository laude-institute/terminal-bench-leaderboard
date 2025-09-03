#!/usr/bin/env python3
import sys
import heapq

def main():
    input = sys.stdin.readline
    n = int(input())
    cows = []
    for _ in range(n):
        g, d = map(int, input().split())
        cows.append((g, d))
    # Sort cows by deadline
    cows.sort(key=lambda x: x[1])
    min_heap = []
    for g, d in cows:
        heapq.heappush(min_heap, g)
        # If more cows than allowed by deadline, remove smallest milk yield
        if len(min_heap) > d:
            heapq.heappop(min_heap)
    # Total milk is sum of scheduled cows
    print(sum(min_heap))

if __name__ == "__main__":
    main()
