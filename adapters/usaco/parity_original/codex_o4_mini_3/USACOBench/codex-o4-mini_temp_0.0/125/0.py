#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, D = map(int, input().split())
    drops = [tuple(map(int, input().split())) for _ in range(N)]
    # Sort drops by x-coordinate
    drops.sort(key=lambda x: x[0])
    xs = [d[0] for d in drops]
    ys = [d[1] for d in drops]

    # Deques to maintain indices of min and max y in the window
    minQ = deque()
    maxQ = deque()
    ans = float('inf')
    left = 0

    for right in range(N):
        y = ys[right]
        # Maintain increasing deque for min y
        while minQ and ys[minQ[-1]] > y:
            minQ.pop()
        minQ.append(right)
        # Maintain decreasing deque for max y
        while maxQ and ys[maxQ[-1]] < y:
            maxQ.pop()
        maxQ.append(right)

        # Shrink window from the left while condition holds
        while left <= right and ys[maxQ[0]] - ys[minQ[0]] >= D:
            width = xs[right] - xs[left]
            ans = min(ans, width)
            # Pop left index from deques if present
            if minQ[0] == left:
                minQ.popleft()
            if maxQ[0] == left:
                maxQ.popleft()
            left += 1

    # Output result
    print(ans if ans != float('inf') else -1)

if __name__ == '__main__':
    main()
