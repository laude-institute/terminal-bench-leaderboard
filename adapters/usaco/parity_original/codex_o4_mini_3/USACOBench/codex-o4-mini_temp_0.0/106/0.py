#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    farms = []
    for _ in range(N):
        x = int(next(it)); y = int(next(it))
        farms.append((x, y))
    total = 0
    # build segments: 1->2, 2->3, ..., N->1
    segments = [(i, i+1) for i in range(N-1)]
    segments.append((N-1, 0))
    for a, b in segments:
        xa, ya = farms[a]
        xb, yb = farms[b]
        dx = abs(xa - xb)
        dy = abs(ya - yb)
        cost = dx + dy
        # check for intermediate farm blocking a shortest path
        for k in range(N):
            if k == a or k == b:
                continue
            xk, yk = farms[k]
            # vertical straight path
            if xa == xb == xk and min(ya, yb) < yk < max(ya, yb):
                cost += 2
                break
            # horizontal straight path
            if ya == yb == yk and min(xa, xb) < xk < max(xa, xb):
                cost += 2
                break
            # general case: any shortest path lies in the bounding rectangle
            if xa != xb and ya != yb:
                if min(xa, xb) < xk < max(xa, xb) and min(ya, yb) < yk < max(ya, yb):
                    cost += 2
                    break
        total += cost
    print(total)

if __name__ == '__main__':
    main()
