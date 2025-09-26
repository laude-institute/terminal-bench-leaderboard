#!/usr/bin/env python3
"""
Solution for Message Relay problem.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = int(data[i])

    result = {}  # cow index -> True (non-loopy) or False (loopy)

    for i in range(1, N + 1):
        if i in result:
            continue
        path = []
        cur = i
        while True:
            if cur == 0:
                safe = True
                break
            if cur in result:
                safe = result[cur]
                break
            if cur in path:
                safe = False
                break
            path.append(cur)
            cur = F[cur]
        for node in path:
            result[node] = safe

    safe_count = sum(1 for i in range(1, N + 1) if result[i])
    print(safe_count)

if __name__ == '__main__':
    main()
