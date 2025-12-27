#!/usr/bin/env python3
"""
Solution to the Wormholes problem.
Counts pairings that allow a cycle via +x traversal.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    coords = []
    idx = 1
    for _ in range(N):
        x = int(data[idx]); y = int(data[idx+1])
        coords.append((x, y))
        idx += 2

    # Precompute next wormhole to the right on same y
    next_on_right = [-1] * N
    for i in range(N):
        xi, yi = coords[i]
        best_j = -1
        best_dist = None
        for j in range(N):
            xj, yj = coords[j]
            if yj == yi and xj > xi:
                dist = xj - xi
                if best_dist is None or dist < best_dist:
                    best_dist = dist
                    best_j = j
        next_on_right[i] = best_j

    pair = [-1] * N
    count = 0

    def cycle_exists():
        # Check if a cycle exists for any start
        for start in range(N):
            pos = start
            for _ in range(N):
                nxt = next_on_right[pos]
                if nxt == -1:
                    break
                pos = pair[nxt]
            else:
                # Completed N moves => cycle
                return True
        return False

    def solve():
        nonlocal count
        # find first unpaired wormhole
        try:
            i = pair.index(-1)
        except ValueError:
            # all paired, test cycle
            if cycle_exists():
                count += 1
            return
        # pair i with any j>i unpaired
        for j in range(i+1, N):
            if pair[j] == -1:
                pair[i] = j
                pair[j] = i
                solve()
                pair[i] = pair[j] = -1

    solve()
    print(count)

if __name__ == "__main__":
    main()
