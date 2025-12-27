#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # feet positions: FL, FR, RL, RR
    # initial positions: FL(0,1), FR(1,1), RL(0,0), RR(1,0)
    feet = {
        'FL': [0, 1],
        'FR': [1, 1],
        'RL': [0, 0],
        'RR': [1, 0],
    }
    # facing: 0=N,1=E,2=S,3=W
    facing = 0
    # direction vectors for N,E,S,W
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # track bounds
    xs = [pos[0] for pos in feet.values()]
    ys = [pos[1] for pos in feet.values()]
    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)

    for _ in range(n):
        inst = next(it)
        foot = inst[:2]
        act = inst[2]
        if act == 'P':
            # pivot around feet[foot]
            px, py = feet[foot]
            # rotate other feet
            for k, v in feet.items():
                if k == foot:
                    continue
                dx = v[0] - px
                dy = v[1] - py
                # rotate 90 deg clockwise: (dx,dy)->(dy,-dx)
                ndx = dy
                ndy = -dx
                feet[k] = [px + ndx, py + ndy]
            # update facing
            facing = (facing + 1) % 4
        else:
            # move foot one cell
            # map act to relative direction
            if act == 'F':
                vec = dirs[facing]
            elif act == 'B':
                vec = dirs[(facing + 2) % 4]
            elif act == 'R':
                vec = dirs[(facing + 1) % 4]
            elif act == 'L':
                vec = dirs[(facing + 3) % 4]
            else:
                # invalid action
                continue
            feet[foot][0] += vec[0]
            feet[foot][1] += vec[1]
        # check for overlap
        seen = set()
        for v in feet.values():
            tup = (v[0], v[1])
            if tup in seen:
                print(-1)
                return
            seen.add(tup)
        # update bounds
        for v in feet.values():
            x, y = v
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)
    # compute area
    width = maxx - minx + 1
    height = maxy - miny + 1
    print(width * height)

if __name__ == '__main__':
    main()
