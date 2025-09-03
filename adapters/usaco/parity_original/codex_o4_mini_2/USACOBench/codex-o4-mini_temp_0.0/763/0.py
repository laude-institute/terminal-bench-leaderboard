#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0]); G = int(data[1])
    logs = []
    idx = 2
    for _ in range(N):
        day = int(data[idx]); cow = int(data[idx+1])
        delta = int(data[idx+2])
        logs.append((day, cow, delta))
        idx += 3

    # Sort measurements by day
    logs.sort()

    outputs = {}      # cow_id -> current output
    counts = {}       # output_value -> count of measured cows
    current_max = G
    default_included = True
    measured_max_count = 0
    changes = 0

    for day, cow, delta in logs:
        old_output = outputs.get(cow, G)
        new_output = old_output + delta

        # Update counts for old output if cow was measured
        if cow in outputs:
            counts[old_output] -= 1
            if counts[old_output] == 0:
                del counts[old_output]
        # Record new output
        outputs[cow] = new_output
        counts[new_output] = counts.get(new_output, 0) + 1

        # Determine the highest output among measured cows
        if counts:
            max_measured = max(counts.keys())
        else:
            max_measured = -1

        # Overall current max is either measured max or G
        if max_measured >= G:
            new_current_max = max_measured
        else:
            new_current_max = G
        new_default_included = (new_current_max == G)
        new_measured_max_count = counts.get(new_current_max, 0)

        # Check if displayed set changes
        if (new_current_max != current_max or
            new_default_included != default_included or
            new_measured_max_count != measured_max_count):
            changes += 1

        current_max = new_current_max
        default_included = new_default_included
        measured_max_count = new_measured_max_count

    print(changes)


if __name__ == '__main__':
    main()
