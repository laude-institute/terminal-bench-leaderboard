#!/usr/bin/env python3
"""
Problem: Count the number of rectangles not contained within any other.
"""
import sys

def main():
    input = sys.stdin.readline
    # Read number of rectangles
    N = int(input())
    # Read rectangles: (x1, y1, x2, y2)
    rects = [tuple(map(int, input().split())) for _ in range(N)]
    # Track whether each rectangle is contained in another
    contained = [False] * N
    # Naive O(N^2) check
    for i in range(N):
        x1, y1, x2, y2 = rects[i]
        for j in range(N):
            if i == j:
                continue
            xx1, yy1, xx2, yy2 = rects[j]
            # Check if rect j contains rect i
            if xx1 <= x1 and yy1 <= y1 and xx2 >= x2 and yy2 >= y2:
                contained[i] = True
                break
    # Count uncontained rectangles
    result = contained.count(False)
    print(result)

if __name__ == '__main__':
    main()
