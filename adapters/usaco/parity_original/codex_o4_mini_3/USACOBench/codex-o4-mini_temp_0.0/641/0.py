#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    cows = []
    for idx in range(N):
        x, y = map(int, input().split())
        cows.append((x, y, idx))

    # Sort cows by x and y to find extremes
    x_sorted = sorted((x, idx) for x, _, idx in cows)
    y_sorted = sorted((y, idx) for _, y, idx in cows)

    # Extract first two and last two extremes for x and y
    xmin1, i_xmin1 = x_sorted[0]
    xmin2, i_xmin2 = x_sorted[1]
    xmax1, i_xmax1 = x_sorted[-1]
    xmax2, i_xmax2 = x_sorted[-2]
    ymin1, i_ymin1 = y_sorted[0]
    ymin2, i_ymin2 = y_sorted[1]
    ymax1, i_ymax1 = y_sorted[-1]
    ymax2, i_ymax2 = y_sorted[-2]

    # Candidate cows to remove are those at any extreme
    candidates = {i_xmin1, i_xmin2, i_xmax1, i_xmax2,
                  i_ymin1, i_ymin2, i_ymax1, i_ymax2}

    best_area = float('inf')
    for remove_idx in candidates:
        # Determine new bounds excluding this cow
        cur_xmin = xmin2 if remove_idx == i_xmin1 else xmin1
        cur_xmax = xmax2 if remove_idx == i_xmax1 else xmax1
        cur_ymin = ymin2 if remove_idx == i_ymin1 else ymin1
        cur_ymax = ymax2 if remove_idx == i_ymax1 else ymax1

        area = (cur_xmax - cur_xmin) * (cur_ymax - cur_ymin)
        if area < best_area:
            best_area = area

    print(best_area)

if __name__ == '__main__':
    main()
