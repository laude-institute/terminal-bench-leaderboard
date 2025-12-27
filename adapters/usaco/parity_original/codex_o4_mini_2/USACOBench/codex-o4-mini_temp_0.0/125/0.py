#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin
    first = data.readline().split()
    if not first:
        return
    n, D = map(int, first)
    drops = [tuple(map(int, data.readline().split())) for _ in range(n)]
    # Sort drops by x-coordinate
    drops.sort(key=lambda drop: drop[0])
    x_coords = [drop[0] for drop in drops]
    y_vals = [drop[1] for drop in drops]

    # Monotonic deques to track min and max y in the window
    min_dq = deque()
    max_dq = deque()
    ans = float('inf')
    i = 0
    # Slide right pointer j
    for j in range(n):
        # Add j to min deque
        while min_dq and y_vals[min_dq[-1]] >= y_vals[j]:
            min_dq.pop()
        min_dq.append(j)
        # Add j to max deque
        while max_dq and y_vals[max_dq[-1]] <= y_vals[j]:
            max_dq.pop()
        max_dq.append(j)

        # Shrink left pointer i while time span >= D
        while i <= j and y_vals[max_dq[0]] - y_vals[min_dq[0]] >= D:
            ans = min(ans, x_coords[j] - x_coords[i])
            # Remove i from deques if present
            if min_dq[0] == i:
                min_dq.popleft()
            if max_dq[0] == i:
                max_dq.popleft()
            i += 1

    # Output result
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
