#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    cur = 0
    events = []  # list of (position, delta)
    # Record painting intervals
    for _ in range(n):
        dist = int(next(it))
        dir = next(it)
        nxt = cur + dist if dir == 'R' else cur - dist
        start = min(cur, nxt)
        end = max(cur, nxt)
        events.append((start, 1))
        events.append((end, -1))
        cur = nxt
    # Coordinate compression
    coords = sorted({pos for pos, _ in events})
    idx = {v: i for i, v in enumerate(coords)}
    diff = [0] * (len(coords) + 1)
    for pos, delta in events:
        diff[idx[pos]] += delta
    # Sweep line to accumulate coats
    ans = 0
    coats = 0
    for i in range(len(coords) - 1):
        coats += diff[i]
        if coats >= k:
            ans += coords[i+1] - coords[i]
    print(ans)

if __name__ == '__main__':
    main()
