#!/usr/bin/env python3
import sys
from collections import deque

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def bounding_box(cells):
    xs = [x for x, y in cells]
    ys = [y for x, y in cells]
    return min(xs), max(xs), min(ys), max(ys)

def offset_cells(cells, dx, dy):
    return [(x + dx, y + dy) for x, y in cells]

def boxes_disjoint(b1, b2):
    # b = (minx, maxx, miny, maxy)
    return b1[1] < b2[0] or b2[1] < b1[0] or b1[3] < b2[2] or b2[3] < b1[2]

def can_separate(c1, c2, c3):
    # BFS on offsets of c2 and c3; fix c1 at origin
    init2 = (0, 0)
    init3 = (0, 0)
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = set()
    q = deque()
    q.append((0,0,0,0))
    seen.add((0,0,0,0))
    # pre-box for c1
    box1 = bounding_box(c1)
    while q:
        dx2, dy2, dx3, dy3 = q.popleft()
        # compute boxes
        box2 = bounding_box(offset_cells(c2, dx2, dy2))
        box3 = bounding_box(offset_cells(c3, dx3, dy3))
        # check goal: all bounding boxes pairwise disjoint
        if boxes_disjoint(box1, box2) and boxes_disjoint(box1, box3) and boxes_disjoint(box2, box3):
            return True
        # try moves
        for obj in (2, 3):
            for ddx, ddy in dirs:
                if obj == 2:
                    ndx2, ndy2 = dx2 + ddx, dy2 + ddy
                    ndx3, ndy3 = dx3, dy3
                else:
                    ndx2, ndy2 = dx2, dy2
                    ndx3, ndy3 = dx3 + ddx, dy3 + ddy
                state = (ndx2, ndy2, ndx3, ndy3)
                if state in seen:
                    continue
                # get new cell positions
                oc2 = set(offset_cells(c2, ndx2, ndy2))
                oc3 = set(offset_cells(c3, ndx3, ndy3))
                # check overlaps
                if set(c1) & oc2: continue
                if set(c1) & oc3: continue
                if oc2 & oc3: continue
                # valid, enqueue
                seen.add(state)
                q.append(state)
    return False

def main():
    n1, n2, n3 = read_ints()
    c1 = [tuple(read_ints()) for _ in range(n1)]
    c2 = [tuple(read_ints()) for _ in range(n2)]
    c3 = [tuple(read_ints()) for _ in range(n3)]
    result = can_separate(c1, c2, c3)
    print(1 if result else 0)

if __name__ == '__main__':
    main()
