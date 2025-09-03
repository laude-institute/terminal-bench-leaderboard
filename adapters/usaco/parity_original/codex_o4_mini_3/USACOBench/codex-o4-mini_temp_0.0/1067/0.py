#!/usr/bin/env python3
import sys
import threading

def main():
    import bisect
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    pts = [(int(next(it)), int(next(it))) for _ in range(N)]
    # Sort by x and by y
    pts_x = sorted(pts, key=lambda p: p[0])
    xs = [p[0] for p in pts_x]
    ys_x = [p[1] for p in pts_x]
    pts_y = sorted(pts, key=lambda p: p[1])
    ys = [p[1] for p in pts_y]
    xs_y = [p[0] for p in pts_y]
    total = 0
    INF = 10**30
    # Phase 1: x-intervals where dx >= dy
    for l in range(N):
        sortedY = []  # y-values in current x-range
        for r in range(l, N):
            dx = xs[r] - xs[l]
            # insert ys_x[r] into sortedY
            bisect.insort(sortedY, ys_x[r])
            M = len(sortedY)
            # for each y-interval in sortedY
            for a in range(M):
                y_a = sortedY[a]
                lower_y = sortedY[a-1] if a > 0 else -INF
                # extend b while dy <= dx
                for b in range(a, M):
                    y_b = sortedY[b]
                    if y_b - y_a > dx:
                        break
                    # compute feasible Y0 bounds
                    low_bound = max(y_b - dx, lower_y)
                    if b == M-1:
                        up_bound = y_a
                    else:
                        up_bound = min(y_a, sortedY[b+1] - dx)
                    if low_bound < up_bound:
                        total += 1
    # Phase 2: y-intervals where dy > dx
    for l in range(N):
        sortedX = []
        for r in range(l, N):
            dy = ys[r] - ys[l]
            bisect.insort(sortedX, xs_y[r])
            M = len(sortedX)
            for a in range(M):
                x_a = sortedX[a]
                lower_x = sortedX[a-1] if a > 0 else -INF
                for b in range(a, M):
                    x_b = sortedX[b]
                    # require dy > dx
                    if x_b - x_a >= dy:
                        break
                    # compute feasible X0 bounds
                    low_bound = max(x_b - dy, lower_x)
                    if b == M-1:
                        up_bound = x_a
                    else:
                        up_bound = min(x_a, sortedX[b+1] - dy)
                    if low_bound < up_bound:
                        total += 1
    # include empty subset
    print(total + 1)

if __name__ == '__main__':
    main()
