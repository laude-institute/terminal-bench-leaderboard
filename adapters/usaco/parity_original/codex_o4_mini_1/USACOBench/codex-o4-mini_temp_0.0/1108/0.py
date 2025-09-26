#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    occupied = set()
    comfortable = set()
    # Directions: right, left, up, down
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def count_neighbors(x, y):
        return sum((x + dx, y + dy) in occupied for dx, dy in dirs)

    def is_comfort(x, y):
        return count_neighbors(x, y) == 3

    for _ in range(N):
        x, y = map(int, input().split())
        occupied.add((x, y))
        # Check this cell and its neighbors for comfort status
        to_check = [(x, y)] + [(x + dx, y + dy) for dx, dy in dirs]
        for cx, cy in to_check:
            if (cx, cy) in occupied:
                if (cx, cy) in comfortable:
                    if not is_comfort(cx, cy):
                        comfortable.remove((cx, cy))
                else:
                    if is_comfort(cx, cy):
                        comfortable.add((cx, cy))
        # Output current count of comfortable cows
        print(len(comfortable))

if __name__ == "__main__":
    main()
