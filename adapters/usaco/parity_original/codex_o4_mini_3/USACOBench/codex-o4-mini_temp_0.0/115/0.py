#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    events = []
    ys = set()
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        # normalize y-interval
        y_low, y_high = min(y1, y2), max(y1, y2)
        events.append((x1, 1, y_low, y_high))
        events.append((x2, -1, y_low, y_high))
        ys.add(y_low)
        ys.add(y_high)
    # coordinate compression
    ys = sorted(ys)
    y_i = {v: i for i, v in enumerate(ys)}

    class SegmentTree:
        def __init__(self, n):
            self.n = n
            self.count = [0] * (4 * n)
            self.length = [0] * (4 * n)

        def update(self, node, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                self.count[node] += val
            else:
                mid = (l + r) // 2
                self.update(node * 2, l, mid, ql, qr, val)
                self.update(node * 2 + 1, mid, r, ql, qr, val)
            if self.count[node] > 0:
                self.length[node] = ys[r] - ys[l]
            else:
                if l + 1 == r:
                    self.length[node] = 0
                else:
                    self.length[node] = self.length[node * 2] + self.length[node * 2 + 1]

    # sort events by x-coordinate
    events.sort()
    st = SegmentTree(len(ys) - 1)
    prev_x = events[0][0]
    area = 0
    # sweep line
    for x, typ, y_low, y_high in events:
        dx = x - prev_x
        area += st.length[1] * dx
        st.update(1, 0, len(ys) - 1, y_i[y_low], y_i[y_high], typ)
        prev_x = x
    print(area)

if __name__ == '__main__':
    main()
