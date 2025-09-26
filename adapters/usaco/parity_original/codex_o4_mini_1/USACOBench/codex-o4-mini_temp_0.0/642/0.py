#!/usr/bin/env python3
"""
Compute the minimum area enclosing all but up to three cows.
We sort cows by x and y, pick critical boundary cows, and test removing
all combinations of up to three critical cows to minimize bounding box area.
"""
import sys
import itertools

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    points = []  # list of (x, y, idx)
    for idx in range(n):
        x, y = map(int, input().split())
        points.append((x, y, idx))

    # Sort by x and y coordinates
    sorted_x = sorted((x, idx) for x, y, idx in points)
    sorted_y = sorted((y, idx) for x, y, idx in points)

    # Identify critical cows at the extremes (first/last 3 in each sort)
    critical = set()
    for x, idx in sorted_x[:3] + sorted_x[-3:]:
        critical.add(idx)
    for y, idx in sorted_y[:3] + sorted_y[-3:]:
        critical.add(idx)
    critical_list = list(critical)

    ans = float('inf')
    # Test removing up to 3 cows from critical set
    for r in range(4):
        for remove in itertools.combinations(critical_list, r):
            removed = set(remove)
            # find new min/max x
            for x, idx in sorted_x:
                if idx not in removed:
                    min_x = x
                    break
            for x, idx in reversed(sorted_x):
                if idx not in removed:
                    max_x = x
                    break
            # find new min/max y
            for y, idx in sorted_y:
                if idx not in removed:
                    min_y = y
                    break
            for y, idx in reversed(sorted_y):
                if idx not in removed:
                    max_y = y
                    break
            # compute area
            area = (max_x - min_x) * (max_y - min_y)
            if area < ans:
                ans = area

    print(ans)

if __name__ == '__main__':
    main()
