#!/usr/bin/env python3
"""
Solution for temperature adjustment problem.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    p = [int(next(it)) for _ in range(n)]
    t = [int(next(it)) for _ in range(n)]
    prev = 0
    total_diff = 0
    for pi, ti in zip(p, t):
        b = pi - ti
        total_diff += abs(b - prev)
        prev = b
    # account for return to zero
    total_diff += abs(prev)
    # each operation contributes 2 to total_diff
    result = total_diff // 2
    print(result)

if __name__ == "__main__":
    main()
