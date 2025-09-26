#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    coords = [None]
    idx = 1
    for _ in range(N):
        x = int(data[idx]); y = int(data[idx+1]); idx += 2
        coords.append((x, y))

    # Precompute next wormhole to the right on same y
    next_on_right = [0] * (N + 1)
    for i in range(1, N+1):
        xi, yi = coords[i]
        min_x = None
        next_i = 0
        for j in range(1, N+1):
            xj, yj = coords[j]
            if yj == yi and xj > xi:
                if min_x is None or xj < min_x:
                    min_x = xj
                    next_i = j
        next_on_right[i] = next_i

    # partner[i] is the paired wormhole for i
    partner = [0] * (N + 1)

    def cycle_exists():
        # Try starting from each wormhole
        for start in range(1, N+1):
            pos = start
            for _ in range(N):
                nxt = next_on_right[pos]
                if nxt == 0:
                    break
                pos = partner[nxt]
            else:
                # Completed N moves without exit -> cycle
                return True
        return False

    def solve():
        # Find first unpaired wormhole
        for i in range(1, N+1):
            if partner[i] == 0:
                break
        else:
            # All paired, check for cycle
            return 1 if cycle_exists() else 0

        total = 0
        # Pair i with any j > i that is unpaired
        for j in range(i+1, N+1):
            if partner[j] == 0:
                partner[i] = j
                partner[j] = i
                total += solve()
                partner[i] = 0
                partner[j] = 0
        return total

    # Output the count of pairings causing a cycle
    print(solve())

if __name__ == '__main__':
    main()
