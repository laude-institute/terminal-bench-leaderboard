#!/usr/bin/env python3

def main():
    # Read starting position and cow position
    x, y = map(int, input().split())
    current = x
    total_distance = 0
    step = 1
    direction = 1  # +1 for right, -1 for left

    while True:
        # Compute next target position for this step
        next_pos = x + direction * step
        # Check if cow lies between current and next_pos (inclusive)
        if (current <= y <= next_pos) or (next_pos <= y <= current):
            # Cow found along this segment; add truncated distance
            total_distance += abs(y - current)
            break
        # Cow not found yet; add full segment distance
        total_distance += abs(next_pos - current)
        # Update position and prepare next step
        current = next_pos
        step *= 2
        direction *= -1

    print(total_distance)

if __name__ == "__main__":
    main()
