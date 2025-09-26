#!/usr/bin/env python3
"""
Solution to Wormholes problem.
Reads N wormholes, computes pairings where a cycle is possible.
"""
import sys

def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    N = int(data[0])
    coords = [(0, 0)] * (N + 1)
    idx = 1
    for i in range(1, N + 1):
        x = int(data[idx]); y = int(data[idx+1])
        coords[i] = (x, y)
        idx += 2

    # Precompute next wormhole to the right on same y
    next_on_right = [0] * (N + 1)
    for i in range(1, N + 1):
        xi, yi = coords[i]
        best = 0
        best_dist = None
        for j in range(1, N + 1):
            xj, yj = coords[j]
            if yj == yi and xj > xi:
                dist = xj - xi
                if best == 0 or dist < best_dist:
                    best = j
                    best_dist = dist
        next_on_right[i] = best

    partner = [0] * (N + 1)

    def has_cycle():
        # Check for any start if cycle exists
        for start in range(1, N + 1):
            pos = start
            for _ in range(N):
                # move through partner then to next on right
                pos = next_on_right[partner[pos]]
                if pos == 0:
                    break
            else:
                return True
        return False

    def count_pairings():
        # find first unpaired
        for i in range(1, N + 1):
            if partner[i] == 0:
                break
        else:
            return 1 if has_cycle() else 0

        total = 0
        for j in range(i + 1, N + 1):
            if partner[j] == 0:
                partner[i] = j
                partner[j] = i
                total += count_pairings()
                partner[i] = partner[j] = 0
        return total

    print(count_pairings())

if __name__ == '__main__':
    main()
