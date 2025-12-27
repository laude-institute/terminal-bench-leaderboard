#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Read hay bale coordinates into a set for O(1) lookup
    S = set()
    min_y = None
    start_x = None
    # Find starting cell: lowest y, then lowest x
    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        S.add((x, y))
        if min_y is None or y < min_y or (y == min_y and x < start_x):
            min_y = y
            start_x = x
    # Starting vertex is bottom-left corner of that cell
    v_x, v_y = start_x, min_y
    # Directions: east, north, west, south
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # For each directed edge, offset to the cell on its left
    left_offsets = [
        (0, 0),    # east -> cell above edge
        (-1, 0),   # north -> cell left of edge
        (-1, -1),  # west -> cell below edge
        (0, -1),   # south -> cell right of edge
    ]
    # Start tracing boundary
    d = 0  # initial direction: east
    start_v = (v_x, v_y)
    start_d = d
    count = 0
    # Walk until we return to start edge
    while True:
        # Move along current edge
        dx, dy = dirs[d]
        v_x += dx
        v_y += dy
        count += 1
        # Determine next direction: keep shape on left
        # Order: turn right, straight, turn left, back
        for nd in ((d + 3) % 4, d, (d + 1) % 4, (d + 2) % 4):
            lx, ly = left_offsets[nd]
            # Check if cell to left of the candidate edge is occupied
            if (v_x + lx, v_y + ly) in S:
                next_d = nd
                break
        # If we've returned to starting edge, stop
        if (v_x, v_y) == start_v and next_d == start_d:
            break
        d = next_d
    # Output the perimeter
    sys.stdout.write(str(count))

if __name__ == '__main__':
    main()
