#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    # Directions: 0=N, 1=E, 2=S, 3=W
    # Precompute suffix effects: dx, dy, final direction for each start dir
    suf_dx = [[0]*4 for _ in range(n+1)]
    suf_dy = [[0]*4 for _ in range(n+1)]
    suf_dir = [[0]*4 for _ in range(n+1)]
    for d in range(4):
        suf_dir[n][d] = d
    # Build suffix from end to start
    for i in range(n-1, -1, -1):
        c = s[i]
        for d in range(4):
            if c == 'F':
                # move forward
                if d == 0:
                    mx, my = 0, 1
                elif d == 1:
                    mx, my = 1, 0
                elif d == 2:
                    mx, my = 0, -1
                else:
                    mx, my = -1, 0
                d2 = d
            elif c == 'L':
                mx, my = 0, 0
                d2 = (d + 3) % 4
            else:  # 'R'
                mx, my = 0, 0
                d2 = (d + 1) % 4
            dx2 = suf_dx[i+1][d2]
            dy2 = suf_dy[i+1][d2]
            suf_dx[i][d] = mx + dx2
            suf_dy[i][d] = my + dy2
            suf_dir[i][d] = suf_dir[i+1][d2]

    # Simulate prefix and consider one-mistake replacements
    seen = set()
    x = y = 0
    d = 0
    for i in range(n):
        for c in ('F', 'L', 'R'):
            if c == s[i]:
                continue
            # apply replacement c
            if c == 'F':
                if d == 0:
                    mx, my = 0, 1
                elif d == 1:
                    mx, my = 1, 0
                elif d == 2:
                    mx, my = 0, -1
                else:
                    mx, my = -1, 0
                d2 = d
            elif c == 'L':
                mx, my = 0, 0
                d2 = (d + 3) % 4
            else:  # 'R'
                mx, my = 0, 0
                d2 = (d + 1) % 4
            x1, y1 = x + mx, y + my
            dxs = suf_dx[i+1][d2]
            dys = suf_dy[i+1][d2]
            seen.add((x1 + dxs, y1 + dys))
        # apply actual command
        c0 = s[i]
        if c0 == 'F':
            if d == 0:
                y += 1
            elif d == 1:
                x += 1
            elif d == 2:
                y -= 1
            else:
                x -= 1
        elif c0 == 'L':
            d = (d + 3) % 4
        else:  # 'R'
            d = (d + 1) % 4

    print(len(seen))

if __name__ == '__main__':
    main()
