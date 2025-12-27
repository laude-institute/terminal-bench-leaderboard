#!/usr/bin/env python3
import sys
from bisect import bisect_left, bisect_right

def simulate(mirrors, a, b):
    # Build lookup for mirror positions
    from collections import defaultdict
    x_map = defaultdict(list)
    y_map = defaultdict(list)
    mirror_dict = {}
    for i, (x, y, orient) in enumerate(mirrors):
        x_map[x].append(y)
        y_map[y].append(x)
        mirror_dict[(x, y)] = (i, orient)
    for ys in x_map.values(): ys.sort()
    for xs in y_map.values(): xs.sort()
    # Ray starts at (0,0) going right
    x, y = 0, 0
    dx, dy = 1, 0
    visited = set()
    while True:
        state = (x, y, dx, dy)
        if state in visited:
            return False
        visited.add(state)
        # Find next mirror in path
        next_m = None
        if dx != 0:
            row = y
            xs = y_map.get(row, [])
            if dx > 0:
                idx = bisect_right(xs, x)
                if idx < len(xs):
                    next_m = (xs[idx], y)
            else:
                idx = bisect_left(xs, x) - 1
                if idx >= 0:
                    next_m = (xs[idx], y)
        else:
            col = x
            ys = x_map.get(col, [])
            if dy > 0:
                idx = bisect_right(ys, y)
                if idx < len(ys):
                    next_m = (x, ys[idx])
            else:
                idx = bisect_left(ys, y) - 1
                if idx >= 0:
                    next_m = (x, ys[idx])
        # Find next barn if on same line
        next_barn = None
        if dy == 0 and y == b and ((dx > 0 and a > x) or (dx < 0 and a < x)):
            next_barn = (a, b)
        if dx == 0 and x == a and ((dy > 0 and b > y) or (dy < 0 and b < y)):
            next_barn = (a, b)
        # Compute distances
        d_barn = abs(a - x) + abs(b - y) if next_barn else None
        if next_m:
            mx, my = next_m
            d_m = abs(mx - x) + abs(my - y)
        else:
            d_m = None
        # Check if barn is hit first
        if next_barn and (d_m is None or d_barn < d_m):
            return True
        # If no mirror ahead, beam exits
        if not next_m:
            return False
        # Reflect off mirror
        mx, my = next_m
        _, orient = mirror_dict[(mx, my)]
        if orient == '/':
            dx, dy = dy, dx
        else:
            dx, dy = -dy, -dx
        x, y = mx, my

def main():
    data = sys.stdin.read().split()
    N, a, b = map(int, data[:3])
    mirrors = []
    idx = 3
    for _ in range(N):
        x = int(data[idx]); y = int(data[idx+1]); orient = data[idx+2]
        mirrors.append([x, y, orient])
        idx += 3
    # Check without toggling
    if simulate(mirrors, a, b):
        print(0)
        return
    # Try toggling each mirror
    for i in range(N):
        orig = mirrors[i][2]
        mirrors[i][2] = '/' if orig == '\\' else '\\'
        if simulate(mirrors, a, b):
            print(i+1)
            return
        mirrors[i][2] = orig
    print(-1)

if __name__ == '__main__':
    main()
