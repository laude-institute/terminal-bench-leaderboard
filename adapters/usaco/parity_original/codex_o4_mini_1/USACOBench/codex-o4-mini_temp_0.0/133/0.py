#!/usr/bin/env python3
import sys
from collections import deque

def read_shape(n):
    return {tuple(map(int, sys.stdin.readline().split())) for _ in range(n)}

def bounding_box(shape):
    xs = [x for x, y in shape]
    ys = [y for x, y in shape]
    return min(xs), max(xs), min(ys), max(ys)

def is_disjoint(bb1, bb2):
    minx1, maxx1, miny1, maxy1 = bb1
    minx2, maxx2, miny2, maxy2 = bb2
    return maxx1 < minx2 or maxx2 < minx1 or maxy1 < miny2 or maxy2 < miny1

def translate(shape, dx, dy):
    return {(x+dx, y+dy) for x, y in shape}

def can_separate(shapes):
    s1, s2, s3 = shapes
    bb1 = bounding_box(s1)
    bb2_local = bounding_box(s2)
    bb3_local = bounding_box(s3)
    # BFS on offsets for s2 and s3, with s1 fixed
    init = (0, 0, 0, 0)
    dq = deque([init])
    seen = {init}
    # bounds for translations
    B = 20
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while dq:
        dx2, dy2, dx3, dy3 = dq.popleft()
        # compute bboxes
        bb2 = (bb2_local[0]+dx2, bb2_local[1]+dx2, bb2_local[2]+dy2, bb2_local[3]+dy2)
        bb3 = (bb3_local[0]+dx3, bb3_local[1]+dx3, bb3_local[2]+dy3, bb3_local[3]+dy3)
        # check separation: all pairs disjoint
        if is_disjoint(bb1, bb2) and is_disjoint(bb1, bb3) and is_disjoint(bb2, bb3):
            return True
        # current shapes positions
        pos2 = translate(s2, dx2, dy2)
        pos3 = translate(s3, dx3, dy3)
        # try moves for s2 and s3
        for sid in (2, 3):
            for ddx, ddy in dirs:
                if sid == 2:
                    ndx2, ndy2 = dx2 + ddx, dy2 + ddy
                    ndx3, ndy3 = dx3, dy3
                else:
                    ndx2, ndy2 = dx2, dy2
                    ndx3, ndy3 = dx3 + ddx, dy3 + ddy
                state = (ndx2, ndy2, ndx3, ndy3)
                # bounds
                if any(abs(v) > B for v in state):
                    continue
                if state in seen:
                    continue
                # translate moved shape and check collision
                if sid == 2:
                    new2 = translate(s2, ndx2, ndy2)
                    # collision with s1 or s3
                    if new2 & s1 or new2 & pos3:
                        continue
                else:
                    new3 = translate(s3, ndx3, ndy3)
                    if new3 & s1 or new3 & pos2:
                        continue
                seen.add(state)
                dq.append(state)
    return False

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n1, n2, n3 = map(int, (next(it), next(it), next(it)))
    s1 = set()
    s2 = set()
    s3 = set()
    for _ in range(n1): s1.add((int(next(it)), int(next(it))))
    for _ in range(n2): s2.add((int(next(it)), int(next(it))))
    for _ in range(n3): s3.add((int(next(it)), int(next(it))))
    result = can_separate((s1, s2, s3))
    print(1 if result else 0)

if __name__ == '__main__':
    main()
