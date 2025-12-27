#!/usr/bin/env python3
"""
Solution for soulmate cows compatibility problem.
Allowed operations on personality p: *2, /2 if even, +1.
Compute minimum operations to transform p into q via BFS.
"""
import sys
from collections import deque

def min_operations(p, q):
    # If already equal, no operations needed
    if p == q:
        return 0
    # Bound search space to avoid infinite growth
    limit = 2 * max(p, q) + 2
    visited = set([p])
    queue = deque([(p, 0)])
    while queue:
        x, d = queue.popleft()
        # generate neighbors
        # multiply by 2
        y = x * 2
        if 0 < y <= limit and y not in visited:
            if y == q:
                return d + 1
            visited.add(y)
            queue.append((y, d + 1))
        # divide by 2 if even
        if x % 2 == 0:
            y = x // 2
            if 0 < y <= limit and y not in visited:
                if y == q:
                    return d + 1
                visited.add(y)
                queue.append((y, d + 1))
        # add 1
        y = x + 1
        if 0 < y <= limit and y not in visited:
            if y == q:
                return d + 1
            visited.add(y)
            queue.append((y, d + 1))
    # unreachable (should not happen)
    return -1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    idx = 1
    results = []
    for _ in range(n):
        p = int(data[idx]); q = int(data[idx+1])
        idx += 2
        results.append(str(min_operations(p, q)))
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    main()
