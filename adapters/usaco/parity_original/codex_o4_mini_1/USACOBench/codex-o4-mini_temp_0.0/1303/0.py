#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    G = int(next(it)); N = int(next(it))
    grazes = []
    for _ in range(G):
        x = int(next(it)); y = int(next(it)); t = int(next(it))
        grazes.append((t, x, y))
    grazes.sort()
    times = [t for t, _, _ in grazes]
    count = 0
    for _ in range(N):
        x = int(next(it)); y = int(next(it)); t = int(next(it))
        # find insertion point
        j = bisect.bisect_left(times, t)
        innocent = False
        # check travel from previous grazing
        if j > 0:
            pt, px, py = grazes[j-1]
            dt = t - pt
            dx = x - px; dy = y - py
            if dx*dx + dy*dy > dt*dt:
                innocent = True
        # check travel to next grazing
        if not innocent and j < G:
            nt, nx, ny = grazes[j]
            dt = nt - t
            dx = x - nx; dy = y - ny
            if dx*dx + dy*dy > dt*dt:
                innocent = True
        if innocent:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
