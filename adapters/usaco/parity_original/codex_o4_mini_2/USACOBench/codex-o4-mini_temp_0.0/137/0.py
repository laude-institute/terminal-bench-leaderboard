#!/usr/bin/env python3
"""
USACO 2012 December Bronze Problem: Tied Down
Computes minimum number of fence posts to remove so Bessie can pull rope free.
Uses nonzero winding number test for each post.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    bx = int(next(it)); by = int(next(it))  # Bessie's position (unused in winding test)
    # Read fence posts
    posts = [(int(next(it)), int(next(it))) for _ in range(N)]
    # Read rope points (closed loop with M segments)
    rope = [(int(next(it)), int(next(it))) for _ in range(M+1)]

    def is_left(xi, yi, xj, yj, xk, yk):
        """Returns >0 if point (xk,yk) is left of line from (xi,yi) to (xj,yj)."""
        return (xj - xi) * (yk - yi) - (xk - xi) * (yj - yi)

    def winding_number(px, py):
        """Compute winding number of rope around point (px,py)."""
        wn = 0
        for i in range(len(rope) - 1):
            xi, yi = rope[i]
            xj, yj = rope[i+1]
            # upward crossing
            if yi <= py:
                if yj > py and is_left(xi, yi, xj, yj, px, py) > 0:
                    wn += 1
            # downward crossing
            else:
                if yj <= py and is_left(xi, yi, xj, yj, px, py) < 0:
                    wn -= 1
        return wn

    # Count posts with nonzero winding number
    result = sum(1 for (px, py) in posts if winding_number(px, py) != 0)
    print(result)

if __name__ == '__main__':
    main()
