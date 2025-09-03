#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    G = int(next(it))
    N = int(next(it))
    # Read and sort grazing events by time
    grazings = []
    for _ in range(G):
        x = int(next(it))
        y = int(next(it))
        t = int(next(it))
        grazings.append((t, x, y))
    grazings.sort()
    # Separate lists for binary search
    T = [t for t, _, _ in grazings]
    X = [x for _, x, _ in grazings]
    Y = [y for _, _, y in grazings]
    innocent_count = 0
    # Evaluate each alibi
    for _ in range(N):
        xa = int(next(it))
        ya = int(next(it))
        ta = int(next(it))
        # Find insertion point among grazings by time
        idx = bisect.bisect_right(T, ta)
        innocent = False
        # Alibi before first grazing
        if idx == 0:
            dt = T[0] - ta
            dx = X[0] - xa
            dy = Y[0] - ya
            if dx*dx + dy*dy > dt*dt:
                innocent = True
        # Alibi after last grazing
        elif idx == G:
            dt = ta - T[-1]
            dx = xa - X[-1]
            dy = ya - Y[-1]
            if dx*dx + dy*dy > dt*dt:
                innocent = True
        # Alibi between two grazings
        else:
            # From previous grazing to alibi
            dt1 = ta - T[idx-1]
            dx1 = xa - X[idx-1]
            dy1 = ya - Y[idx-1]
            # From alibi to next grazing
            dt2 = T[idx] - ta
            dx2 = X[idx] - xa
            dy2 = Y[idx] - ya
            if dx1*dx1 + dy1*dy1 > dt1*dt1 or dx2*dx2 + dy2*dy2 > dt2*dt2:
                innocent = True
        if innocent:
            innocent_count += 1
    # Output result
    print(innocent_count)

if __name__ == '__main__':
    main()
