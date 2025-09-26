#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    sick = []
    healthy = []
    for _ in range(n):
        x = int(next(it))
        s = int(next(it))
        if s == 1:
            sick.append(x)
        else:
            healthy.append(x)
    # If no healthy cows, all sick are connected
    if not healthy:
        print(1)
        return
    # Compute minimal distance between any sick and healthy cow
    D = min(abs(si - hi) for si in sick for hi in healthy)
    # Sort sick positions
    sick.sort()
    # Count connected groups among sick cows with max spread < D
    groups = 1
    for i in range(1, len(sick)):
        if sick[i] - sick[i-1] >= D:
            groups += 1
    print(groups)

if __name__ == '__main__':
    main()
