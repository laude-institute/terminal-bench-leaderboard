#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    G = int(next(it))
    logs = []
    for _ in range(n):
        day = int(next(it))
        cow = int(next(it))
        delta = int(next(it))
        logs.append((day, cow, delta))
    # Sort measurements by day
    logs.sort(key=lambda x: x[0])

    # Track current milk output for each cow (default G)
    cows = {}
    # Multiset of outputs: production -> count
    counts = {G: n + 1}

    current_max = G
    leaders = counts[G]
    changes = 0

    for day, cow, delta in logs:
        old = cows.get(cow, G)
        new = old + delta
        cows[cow] = new
        # Update counts
        counts[old] -= 1
        if counts[old] == 0:
            del counts[old]
        counts[new] = counts.get(new, 0) + 1

        prev_max = current_max
        prev_leaders = leaders

        # Determine new current_max and leaders
        if new > current_max:
            current_max = new
            leaders = counts[new]
        else:
            if old == prev_max and old not in counts:
                # previous max removed, find new max
                current_max = max(counts.keys())
            # Update leaders count for current_max
            leaders = counts[current_max]

        # Check if display changes
        if current_max != prev_max or leaders != prev_leaders:
            changes += 1

    # Output result
    print(changes)

if __name__ == '__main__':
    main()
