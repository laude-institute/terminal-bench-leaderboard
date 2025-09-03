#!/usr/bin/env python3
import sys

def main():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    # Parse measurements
    measurements = []  # list of (day, cow, delta)
    idx = 1
    for _ in range(n):
        day = int(input_data[idx]); idx += 1
        cow = input_data[idx]; idx += 1
        delta = int(input_data[idx]); idx += 1
        measurements.append((day, cow, delta))
    # Sort by day
    measurements.sort(key=lambda x: x[0])

    # Initialize outputs and display
    outputs = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}
    # Initially all are displayed (tie)
    display = set(outputs.keys())
    changes = 0

    # Process measurements
    for _, cow, delta in measurements:
        outputs[cow] += delta
        # Determine current leaders
        max_out = max(outputs.values())
        new_display = {c for c, v in outputs.items() if v == max_out}
        if new_display != display:
            changes += 1
            display = new_display

    print(changes)

if __name__ == '__main__':
    main()
