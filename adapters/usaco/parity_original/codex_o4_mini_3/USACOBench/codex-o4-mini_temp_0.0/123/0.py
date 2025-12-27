#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    N = len(s)
    # direction: 0=N,1=E,2=S,3=W
    dx_table = [0, 1, 0, -1]
    dy_table = [1, 0, -1, 0]
    # suffix effects: from i to end starting with direction d
    suffix_dx = [[0] * 4 for _ in range(N + 1)]
    suffix_dy = [[0] * 4 for _ in range(N + 1)]
    suffix_dir = [[0] * 4 for _ in range(N + 1)]
    for d in range(4):
        suffix_dir[N][d] = d
    for i in range(N - 1, -1, -1):
        c = s[i]
        for d in range(4):
            if c == 'F':
                dx1 = dx_table[d]
                dy1 = dy_table[d]
                d1 = d
            elif c == 'L':
                dx1 = 0
                dy1 = 0
                d1 = (d + 3) % 4
            else:  # 'R'
                dx1 = 0
                dy1 = 0
                d1 = (d + 1) % 4
            dx2 = suffix_dx[i + 1][d1]
            dy2 = suffix_dy[i + 1][d1]
            d2 = suffix_dir[i + 1][d1]
            suffix_dx[i][d] = dx1 + dx2
            suffix_dy[i][d] = dy1 + dy2
            suffix_dir[i][d] = d2

    # prefix state
    prefix_x = [0] * (N + 1)
    prefix_y = [0] * (N + 1)
    prefix_dir = [0] * (N + 1)
    for i in range(N):
        c = s[i]
        d = prefix_dir[i]
        x = prefix_x[i]
        y = prefix_y[i]
        if c == 'F':
            x += dx_table[d]
            y += dy_table[d]
            d1 = d
        elif c == 'L':
            d1 = (d + 3) % 4
        else:  # 'R'
            d1 = (d + 1) % 4
        prefix_x[i + 1] = x
        prefix_y[i + 1] = y
        prefix_dir[i + 1] = d1

    # simulate one wrong command
    result = set()
    for i in range(N):
        orig = s[i]
        px = prefix_x[i]
        py = prefix_y[i]
        d = prefix_dir[i]
        for c in ('F', 'L', 'R'):
            if c == orig:
                continue
            if c == 'F':
                dx1 = dx_table[d]
                dy1 = dy_table[d]
                d1 = d
            elif c == 'L':
                dx1 = 0
                dy1 = 0
                d1 = (d + 3) % 4
            else:  # 'R'
                dx1 = 0
                dy1 = 0
                d1 = (d + 1) % 4
            dx2 = suffix_dx[i + 1][d1]
            dy2 = suffix_dy[i + 1][d1]
            fx = px + dx1 + dx2
            fy = py + dy1 + dy2
            result.add((fx, fy))

    print(len(result))

if __name__ == '__main__':
    main()
