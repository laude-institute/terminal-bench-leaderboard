#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    coords = []
    for i in range(N):
        x = int(data[1 + 2*i])
        y = int(data[1 + 2*i + 1])
        coords.append((x, y))
    total = 0
    for i in range(N):
        j = (i + 1) % N
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        dist = dx + dy
        # add detour if aligned and blocked
        if x1 == x2:
            for k, (xk, yk) in enumerate(coords):
                if k != i and k != j and xk == x1 and min(y1, y2) < yk < max(y1, y2):
                    dist += 2
                    break
        elif y1 == y2:
            for k, (xk, yk) in enumerate(coords):
                if k != i and k != j and yk == y1 and min(x1, x2) < xk < max(x1, x2):
                    dist += 2
                    break
        total += dist
    sys.stdout.write(str(total))

if __name__ == "__main__":
    main()
