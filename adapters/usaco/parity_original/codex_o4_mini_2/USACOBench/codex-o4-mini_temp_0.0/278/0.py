#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # Initialize foot positions: (x, y) coordinates
    feet = {
        'FL': (0, 1),  # front left
        'FR': (1, 1),  # front right
        'RL': (0, 0),  # rear left
        'RR': (1, 0),  # rear right
    }
    # Orientation: 0 = north, 1 = east, 2 = south, 3 = west
    ori = 0
    # Track bounds
    xs = [x for x, y in feet.values()]
    ys = [y for x, y in feet.values()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # Base direction vectors: forward, right, back, left (when facing north)
    dir_map = {
        'F': (0, 1),
        'R': (1, 0),
        'B': (0, -1),
        'L': (-1, 0),
    }

    for _ in range(N):
        inst = input().strip()
        foot = inst[:2]
        action = inst[2]
        if action == 'P':
            # Pivot 90deg clockwise around the planted foot
            px, py = feet[foot]
            new_feet = {}
            for f, (x, y) in feet.items():
                if f == foot:
                    new_feet[f] = (x, y)
                else:
                    # Translate to origin, rotate cw, translate back
                    rx, ry = x - px, y - py
                    nrx, nry = ry, -rx
                    new_feet[f] = (px + nrx, py + nry)
            feet = new_feet
            ori = (ori + 1) % 4
        else:
            # Move one foot by one cell
            dx, dy = dir_map[action]
            # Rotate movement vector by current orientation
            for _ in range(ori):
                dx, dy = dy, -dx
            x, y = feet[foot]
            feet[foot] = (x + dx, y + dy)
        # Check for collision
        if len(set(feet.values())) < 4:
            print(-1)
            return
        # Update bounds
        for x, y in feet.values():
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

    # Compute minimal stage area
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(width * height)

if __name__ == '__main__':
    main()
