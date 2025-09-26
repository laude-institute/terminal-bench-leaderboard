#!/usr/bin/env python3
import sys

def simulate(mirrors, barn, flip_index):
    # mirrors: list of (x,y,orient), 1-based indexing
    x0, y0 = 0, 0
    bx, by = barn
    dx, dy = 1, 0  # start facing right
    visited = set()
    # Pre-extract positions
    N = len(mirrors) - 1
    while True:
        best_dist = None
        best_i = None
        # check barn first distance
        if dy == 0:
            # horizontal movement
            if by == y0 and (bx - x0) * dx > 0:
                best_dist = abs(bx - x0)
                best_i = 0  # barn marker
        else:
            # vertical movement
            if bx == x0 and (by - y0) * dy > 0:
                best_dist = abs(by - y0)
                best_i = 0
        # check mirrors
        for i in range(1, N+1):
            xi, yi, ori = mirrors[i]
            if dx != 0:
                if yi == y0 and (xi - x0) * dx > 0:
                    dist = abs(xi - x0)
                else:
                    continue
            else:
                if xi == x0 and (yi - y0) * dy > 0:
                    dist = abs(yi - y0)
                else:
                    continue
            if best_dist is None or dist < best_dist:
                best_dist = dist
                best_i = i
        # no intersection
        if best_i is None:
            return False
        # barn reached
        if best_i == 0:
            return True
        # mirror hit
        if (best_i, dx, dy) in visited:
            return False
        visited.add((best_i, dx, dy))
        # get orientation, apply flip if needed
        xi, yi, ori = mirrors[best_i]
        if best_i == flip_index:
            ori = '/' if ori == '\\' else '\\'
        # reflect direction
        if ori == '/':
            # (dx,dy) -> (dy,dx)
            dx, dy = dy, dx
        else:
            # '\\' mirror: (dx,dy) -> (-dy,-dx)
            dx, dy = -dy, -dx
        # update position
        x0, y0 = xi, yi

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    a = int(next(it)); b = int(next(it))
    mirrors = [None] * (N+1)
    for i in range(1, N+1):
        x = int(next(it)); y = int(next(it));
        ori = next(it)
        mirrors[i] = (x, y, ori)
    # check without flip
    if simulate(mirrors, (a,b), 0):
        print(0)
        return
    # check each mirror
    for i in range(1, N+1):
        if simulate(mirrors, (a,b), i):
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()
