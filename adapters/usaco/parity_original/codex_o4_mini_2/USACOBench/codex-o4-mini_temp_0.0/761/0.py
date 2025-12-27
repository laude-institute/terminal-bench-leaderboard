#!/usr/bin/env python3
"""
Solution to the milk output display change problem.
Processes measurement logs and counts display changes.
"""

import sys

def main():
    data = sys.stdin.read().strip().splitlines()
    n = int(data[0])
    # Parse measurements: (day, cow, change)
    events = []
    for line in data[1:]:
        parts = line.split()
        day = int(parts[0])
        cow = parts[1]
        change = int(parts[2])
        events.append((day, cow, change))

    # Sort events by day
    events.sort(key=lambda x: x[0])

    # Initial productions
    productions = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}
    # Initial display leaders
    max_prod = 7
    leaders = set(productions.keys())
    display_changes = 0

    # Process each measurement
    for _, cow, change in events:
        # Update production
        productions[cow] += change

        # Determine current leaders
        current_max = max(productions.values())
        current_leaders = {c for c, p in productions.items() if p == current_max}

        # Check if display changes
        if current_leaders != leaders:
            display_changes += 1
            leaders = current_leaders

    # Output result
    print(display_changes)

if __name__ == '__main__':
    main()
