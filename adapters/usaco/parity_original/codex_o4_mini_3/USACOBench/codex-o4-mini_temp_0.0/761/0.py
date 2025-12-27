#!/usr/bin/env python3
"""
Simulates Farmer John's cow milk output display changes.
"""
import sys

def main():
    data = sys.stdin.read().strip().splitlines()
    n = int(data[0])
    records = []
    for line in data[1:1+n]:
        parts = line.split()
        day = int(parts[0])
        name = parts[1]
        delta = int(parts[2])
        records.append((day, name, delta))
    # Sort measurements by day
    records.sort(key=lambda x: x[0])
    # Initial outputs
    outputs = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}
    # Initial display: all cows (tie)
    current_max = 7
    display = set(outputs.keys())
    changes = 0
    # Process each measurement
    for day, name, delta in records:
        outputs[name] += delta
        new_max = max(outputs.values())
        new_display = {cow for cow, val in outputs.items() if val == new_max}
        if new_display != display:
            changes += 1
            display = new_display
    # Output the number of display changes
    print(changes)

if __name__ == '__main__':
    main()
