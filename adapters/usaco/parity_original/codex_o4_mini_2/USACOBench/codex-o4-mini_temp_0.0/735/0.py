#!/usr/bin/env python3

def main():
    # Read input positions
    x, y = map(int, input().split())
    total_distance = 0
    current = x
    step = 0

    # Search in zig-zag pattern until we find Bessie at y
    while True:
        # Compute next target offset (doubling each time, alternating sign)
        offset = 1 << step
        if step % 2 == 0:
            target = x + offset
        else:
            target = x - offset

        # Check if y lies between current and target positions
        if min(current, target) <= y <= max(current, target):
            total_distance += abs(y - current)
            break
        # Otherwise, travel full segment and continue
        total_distance += abs(target - current)
        current = target
        step += 1

    # Output total distance traveled
    print(total_distance)

if __name__ == '__main__':
    main()
