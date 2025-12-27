#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    instrs = [input().strip() for _ in range(N)]

    # Initial foot positions: RL, RR, FL, FR
    # Coordinates: x right, y up; facing north
    pos = {
        'FL': (0, 1),
        'FR': (1, 1),
        'RL': (0, 0),
        'RR': (1, 0),
    }
    # orientation: 0=north,1=east,2=south,3=west
    orient = 0

    # Movement vectors per orientation
    moves = {
        0: {'F': (0, 1),  'B': (0, -1), 'L': (-1, 0), 'R': (1, 0)},
        1: {'F': (1, 0),  'B': (-1, 0), 'L': (0, 1),  'R': (0, -1)},
        2: {'F': (0, -1), 'B': (0, 1),  'L': (1, 0),  'R': (-1, 0)},
        3: {'F': (-1, 0), 'B': (1, 0),  'L': (0, -1), 'R': (0, 1)},
    }

    # Track extremes
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    for ins in instrs:
        foot = ins[:2]
        act = ins[2]

        if act == 'P':  # pivot clockwise
            # pivot around pos[foot]
            px, py = pos[foot]
            # rotate other feet
            for k in pos:
                if k == foot:
                    continue
                x, y = pos[k]
                dx, dy = x - px, y - py
                # clockwise: (dx,dy)->(dy, -dx)
                nx, ny = px + dy, py - dx
                pos[k] = (nx, ny)
            # update orientation
            orient = (orient + 1) % 4
        else:
            # move foot in direction
            dx, dy = moves[orient][act]
            x, y = pos[foot]
            pos[foot] = (x + dx, y + dy)

        # check collision
        if len(set(pos.values())) < 4:
            print(-1)
            return

        # update bounds
        xs = [p[0] for p in pos.values()]
        ys = [p[1] for p in pos.values()]
        min_x, max_x = min(min_x, min(xs)), max(max_x, max(xs))
        min_y, max_y = min(min_y, min(ys)), max(max_y, max(ys))

    # compute area
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(width * height)

if __name__ == '__main__':
    main()
