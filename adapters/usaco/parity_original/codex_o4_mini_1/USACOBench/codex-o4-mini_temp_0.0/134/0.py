#!/usr/bin/env python3
"""
Unlocking Blocks (Silver) solution.
"""
import sys
from collections import deque

def read_input():
    data = sys.stdin.read().split()
    it = iter(data)
    n1, n2, n3 = map(int, (next(it), next(it), next(it)))
    shapes = []
    for n in (n1, n2, n3):
        sq = []
        for _ in range(n):
            x = int(next(it)); y = int(next(it))
            sq.append((x, y))
        shapes.append(sq)
    return shapes

def get_bbox(shape, dx, dy):
    xs = [x+dx for x, y in shape]
    ys = [y+dy for x, y in shape]
    return min(xs), min(ys), max(xs)+1, max(ys)+1

def bbox_overlap(b1, b2):
    # returns True if positive-area overlap
    return (min(b1[2], b2[2]) > max(b1[0], b2[0]) and
            min(b1[3], b2[3]) > max(b1[1], b2[1]))

def shapes_overlap(s1, dx1, dy1, s2, dx2, dy2):
    moved = set((x+dx1, y+dy1) for x, y in s1)
    other = set((x+dx2, y+dy2) for x, y in s2)
    return not moved.isdisjoint(other)

def separated(bboxes):
    # no pair overlaps
    for i in range(3):
        for j in range(i+1, 3):
            if bbox_overlap(bboxes[i], bboxes[j]):
                return False
    return True

def solve():
    shapes = read_input()
    # BFS state: (dx0, dy0, dx1, dy1, dx2, dy2)
    start = (0, 0, 0, 0, 0, 0)
    # bounds for shifts
    LIM = 20
    dq = deque()
    dq.append((start, 0))
    seen = {start}
    while dq:
        (dx0, dy0, dx1, dy1, dx2, dy2), dist = dq.popleft()
        # check separation
        bbs = [get_bbox(shapes[i], (dx0, dy0, dx1, dy1, dx2, dy2)[2*i], (dx0, dy0, dx1, dy1, dx2, dy2)[2*i+1])
               for i in range(3)]
        if separated(bbs):
            print(dist)
            return
        # try moves
        for i in range(3):
            base = [dx0, dy0, dx1, dy1, dx2, dy2]
            for mx, my in ((1,0),(-1,0),(0,1),(0,-1)):
                new = base.copy()
                new[2*i] += mx
                new[2*i+1] += my
                nx, ny = new[2*i], new[2*i+1]
                # bounds
                if not -LIM <= nx <= LIM or not -LIM <= ny <= LIM:
                    continue
                newt = tuple(new)
                if newt in seen:
                    continue
                # check shape collision with others
                ok = True
                for j in range(3):
                    if j == i: continue
                    if shapes_overlap(shapes[i], new[2*i], new[2*i+1],
                                      shapes[j], new[2*j], new[2*j+1]):
                        ok = False
                        break
                if not ok:
                    continue
                seen.add(newt)
                dq.append((newt, dist+1))
    print(-1)

if __name__ == '__main__':
    solve()
