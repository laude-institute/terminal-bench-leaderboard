#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    # Read N (number of haybales) and M (minimum total flavor)
    N, M = map(int, input().split())
    flavors = []
    spiciness = []
    for _ in range(N):
        f, s = map(int, input().split())
        flavors.append(f)
        spiciness.append(s)

    # Sliding window pointers and current flavor sum
    left = 0
    current_sum = 0
    # Monotonic deque to track max spiciness in window: stores (spice, index)
    dq = deque()
    answer = 10**18  # large initial value

    # Expand the window with right pointer
    for right in range(N):
        current_sum += flavors[right]
        # Maintain deque decreasing by spiciness
        while dq and dq[-1][0] <= spiciness[right]:
            dq.pop()
        dq.append((spiciness[right], right))

        # Try to shrink window while flavor sum meets requirement
        while current_sum >= M:
            # The max spiciness is at the front of deque
            answer = min(answer, dq[0][0])
            # Remove leftmost flavor and advance left pointer
            current_sum -= flavors[left]
            # Pop from deque if the removed index was the max
            if dq and dq[0][1] == left:
                dq.popleft()
            left += 1

    # Output the minimum spiciness found
    print(answer)

if __name__ == '__main__':
    main()
