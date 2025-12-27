#!/usr/bin/env python3
"""
Unlocking Blocks puzzle solution.
"""
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n1 = int(next(it))
    n2 = int(next(it))
    n3 = int(next(it))
    # Read shapes squares
    shape1 = [(int(next(it)), int(next(it))) for _ in range(n1)]
    shape2 = [(int(next(it)), int(next(it))) for _ in range(n2)]
    shape3 = [(int(next(it)), int(next(it))) for _ in range(n3)]
    # Precompute sets and bounding boxes
    set1 = set(shape1)
    min1x = min(x for x, y in shape1)
    max1x = max(x for x, y in shape1)
    min1y = min(y for x, y in shape1)
    max1y = max(y for x, y in shape1)
    # relative coords for shape2 and shape3
    # as given, initial offsets are zero
    min2x = min(x for x, y in shape2)
    max2x = max(x for x, y in shape2)
    min2y = min(y for x, y in shape2)
    max2y = max(y for x, y in shape2)
    min3x = min(x for x, y in shape3)
    max3x = max(x for x, y in shape3)
    min3y = min(y for x, y in shape3)
    max3y = max(y for x, y in shape3)

    # BFS on offsets of shape2 and shape3 relative to initial
    # We fix shape1 at its initial location
    bound = 20
    # state: (dx2, dy2, dx3, dy3)
    start = (0, 0, 0, 0)
    dq = deque([start])
    visited = set([start])
    # Directions: (dx, dy)
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    while dq:
        dx2, dy2, dx3, dy3 = dq.popleft()
        # Check bounding boxes disjoint for all pairs
        # shape1 box
        b1 = (min1x, max1x, min1y, max1y)
        # shape2 box shifted
        b2 = (min2x+dx2, max2x+dx2, min2y+dy2, max2y+dy2)
        # shape3 box shifted
        b3 = (min3x+dx3, max3x+dx3, min3y+dy3, max3y+dy3)
        def disjoint(a, b):
            return (a[1] < b[0] or b[1] < a[0]
                    or a[3] < b[2] or b[3] < a[2])
        if disjoint(b1, b2) and disjoint(b1, b3) and disjoint(b2, b3):
            print(1)
            return
        # Build current occupied sets for collision checking
        cur2 = {(x+dx2, y+dy2) for x, y in shape2}
        cur3 = {(x+dx3, y+dy3) for x, y in shape3}
        # Try moves for shape2
        for ddx, ddy in dirs:
            ndx2, ndy2 = dx2 + ddx, dy2 + ddy
            if not (-bound <= ndx2 <= bound and -bound <= ndy2 <= bound):
                continue
            # collision check moving shape2
            ok = True
            for x, y in cur2:
                nx, ny = x + ddx, y + ddy
                if (nx, ny) in set1 or (nx, ny) in cur3:
                    ok = False
                    break
            if not ok:
                continue
            state = (ndx2, ndy2, dx3, dy3)
            if state not in visited:
                visited.add(state)
                dq.append(state)
        # Try moves for shape3
        for ddx, ddy in dirs:
            ndx3, ndy3 = dx3 + ddx, dy3 + ddy
            if not (-bound <= ndx3 <= bound and -bound <= ndy3 <= bound):
                continue
            # collision check moving shape3
            ok = True
            for x, y in cur3:
                nx, ny = x + ddx, y + ddy
                if (nx, ny) in set1 or (nx, ny) in cur2:
                    ok = False
                    break
            if not ok:
                continue
            state = (dx2, dy2, ndx3, ndy3)
            if state not in visited:
                visited.add(state)
                dq.append(state)
    # Exhausted without separating
    print(0)

if __name__ == '__main__':
    main()
