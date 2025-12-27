#!/usr/bin/env python3
"""
Solution to the haybale feeding problem.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    T = int(data[1])
    deliveries = []
    idx = 2
    for _ in range(N):
        d = int(data[idx])
        b = int(data[idx + 1])
        deliveries.append((d, b))
        idx += 2

    prev_day = 1
    hay = 0
    eaten = 0

    # Process each delivery
    for d, b in deliveries:
        # Bessie eats one per day if hay is available between prev_day and the day before d
        days = d - prev_day
        eat = min(hay, days)
        eaten += eat
        hay -= eat

        # Haybales arrive in the morning of day d
        hay += b
        prev_day = d

    # After last delivery, process through day T
    days = (T + 1) - prev_day
    eat = min(hay, days)
    eaten += eat

    # Output result
    print(eaten)

if __name__ == "__main__":
    main()
