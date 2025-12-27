#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    # Directions: 0=N,1=E,2=S,3=W
    # Prefix states: position and direction after first i commands
    px = [0] * (n + 1)
    py = [0] * (n + 1)
    pd = [0] * (n + 1)
    for i in range(n):
        x, y, d = px[i], py[i], pd[i]
        c = s[i]
        if c == 'F':
            if d == 0:
                y += 1
            elif d == 1:
                x += 1
            elif d == 2:
                y -= 1
            else:
                x -= 1
        elif c == 'L':
            d = (d + 3) % 4
        else:  # 'R'
            d = (d + 1) % 4
        px[i+1], py[i+1], pd[i+1] = x, y, d
    # Suffix effects: for each i, for each starting dir, delta pos and end dir executing s[i:]
    dx = [[0] * 4 for _ in range(n + 1)]
    dy = [[0] * 4 for _ in range(n + 1)]
    ed = [[0] * 4 for _ in range(n + 1)]
    for d in range(4):
        ed[n][d] = d
    for i in range(n-1, -1, -1):
        c = s[i]
        for d in range(4):
            x1 = y1 = 0
            d1 = d
            if c == 'F':
                if d1 == 0:
                    y1 = 1
                elif d1 == 1:
                    x1 = 1
                elif d1 == 2:
                    y1 = -1
                else:
                    x1 = -1
            elif c == 'L':
                d1 = (d1 + 3) % 4
            else:  # 'R'
                d1 = (d1 + 1) % 4
            dx[i][d] = x1 + dx[i+1][d1]
            dy[i][d] = y1 + dy[i+1][d1]
            ed[i][d] = ed[i+1][d1]
    # Collect distinct end positions
    seen = set()
    for i in range(n):
        for c in ('F', 'L', 'R'):
            if c == s[i]:
                continue
            # prefix state
            x, y, d = px[i], py[i], pd[i]
            # apply replacement
            if c == 'F':
                if d == 0:
                    y += 1
                elif d == 1:
                    x += 1
                elif d == 2:
                    y -= 1
                else:
                    x -= 1
            elif c == 'L':
                d = (d + 3) % 4
            else:  # 'R'
                d = (d + 1) % 4
            # apply suffix from i+1
            x_end = x + dx[i+1][d]
            y_end = y + dy[i+1][d]
            seen.add((x_end, y_end))
    print(len(seen))

if __name__ == '__main__':
    main()
