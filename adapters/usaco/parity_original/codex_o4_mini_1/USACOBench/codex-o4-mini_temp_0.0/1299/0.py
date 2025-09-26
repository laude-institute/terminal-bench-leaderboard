#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0]); T = int(data[1])
    deliveries = []
    idx = 2
    for _ in range(N):
        d = int(data[idx]); b = int(data[idx+1])
        idx += 2
        deliveries.append((d, b))

    current = 0
    eaten = 0
    last_day = 1
    for d, b in deliveries:
        interval = d - last_day
        eat = min(current, interval)
        eaten += eat
        current -= eat
        # delivery arrives
        current += b
        last_day = d

    # After last delivery until day T
    if last_day <= T:
        interval = T - last_day + 1
        eat = min(current, interval)
        eaten += eat

    print(eaten)

if __name__ == "__main__":
    main()
