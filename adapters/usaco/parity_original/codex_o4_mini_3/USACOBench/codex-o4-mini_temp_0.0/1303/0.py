#!/usr/bin/env python3
"""
Solves the grazing alibi problem.
Reads G grazing events and N cow alibis, each with (x,y,t).
Counts cows whose alibi is impossible to reconcile with the grazing schedule.
"""
import sys
import bisect

def main():
    input = sys.stdin.readline
    G, N = map(int, input().split())
    # Read and sort grazing events by time
    grazings = [tuple(map(int, input().split())) for _ in range(G)]
    grazings.sort(key=lambda event: event[2])
    xs = [g[0] for g in grazings]
    ys = [g[1] for g in grazings]
    ts = [g[2] for g in grazings]

    innocent_count = 0
    for _ in range(N):
        x0, y0, t0 = map(int, input().split())
        # Find insertion point in grazing times
        idx = bisect.bisect_left(ts, t0)
        possible = True
        # Check travel from alibi to next grazing
        if idx < G:
            dt = ts[idx] - t0
            dx = xs[idx] - x0
            dy = ys[idx] - y0
            if dx*dx + dy*dy > dt*dt:
                possible = False
        # Check travel from previous grazing to alibi
        if possible and idx > 0:
            dt = t0 - ts[idx-1]
            dx = x0 - xs[idx-1]
            dy = y0 - ys[idx-1]
            if dx*dx + dy*dy > dt*dt:
                possible = False
        # If impossible, alibi proves innocence
        if not possible:
            innocent_count += 1

    print(innocent_count)

if __name__ == '__main__':
    main()
