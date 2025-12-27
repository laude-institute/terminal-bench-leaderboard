#!/usr/bin/env python3
import sys

def can_see(a, b, mirrors):
    # mirrors: list of (x, y, orient) where orient is '/' or '\\'
    # directions: 0=right,1=up,2=left,3=down
    # mapping to dx,dy
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # reflection rules
    def reflect(dx, dy, orient):
        if orient == '/':
            return dy, dx
        else:  # '\\'
            return -dy, -dx

    x, y = 0, 0
    dir_idx = 0
    visited = set()
    # simulate until hit target or infinity
    while True:
        dx, dy = dxy[dir_idx]
        best_t = float('inf')
        best_m = -1
        # check target
        if dx != 0 and y == b:
            t = (a - x) / dx
            if t > 0 and t < best_t:
                best_t = t
                best_m = None  # target
        if dy != 0 and x == a:
            t = (b - y) / dy
            if t > 0 and t < best_t:
                best_t = t
                best_m = None
        # check mirrors
        for i, (mx, my, orient) in enumerate(mirrors):
            if dx != 0 and my == y:
                t = (mx - x) / dx
            elif dy != 0 and mx == x:
                t = (my - y) / dy
            else:
                continue
            if t > 0 and t < best_t:
                best_t = t
                best_m = i
        # no hit
        if best_t == float('inf'):
            return False
        # hit target
        if best_m is None:
            return True
        # hit mirror
        i = best_m
        # move to mirror
        x, y = mirrors[i][0], mirrors[i][1]
        # reflect
        dx, dy = reflect(dx, dy, mirrors[i][2])
        # update dir_idx
        for idx, (ddx, ddy) in enumerate(dxy):
            if (ddx, ddy) == (dx, dy):
                dir_idx = idx
                break
        # detect loops
        state = (i, dir_idx)
        if state in visited:
            return False
        visited.add(state)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    a = int(next(it)); b = int(next(it))
    mirrors = []
    for _ in range(N):
        x = int(next(it)); y = int(next(it)); o = next(it)
        mirrors.append([x, y, o])
    # check without toggle
    if can_see(a, b, mirrors):
        print(0)
        return
    # try toggling each mirror
    for i in range(N):
        mirrors[i][2] = '/' if mirrors[i][2] == '\\' else '\\'
        if can_see(a, b, mirrors):
            print(i+1)
            return
        # revert
        mirrors[i][2] = '/' if mirrors[i][2] == '\\' else '\\'
    print(-1)

if __name__ == '__main__':
    main()
