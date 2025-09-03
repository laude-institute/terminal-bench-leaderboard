#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    cows = []  # list of (x, y, idx)
    for i in range(n):
        x, y = map(int, input().split())
        cows.append((x, y, i))

    # Sort by x and by y
    sorted_x = sorted(cows, key=lambda c: c[0])
    sorted_y = sorted(cows, key=lambda c: c[1])

    # Extract extremes and second extremes
    min_x, _, min_x_id = sorted_x[0]
    sec_min_x, _, sec_min_x_id = sorted_x[1]
    max_x, _, max_x_id = sorted_x[-1]
    sec_max_x, _, sec_max_x_id = sorted_x[-2]

    _, min_y, min_y_id = sorted_y[0]
    _, sec_min_y, sec_min_y_id = sorted_y[1]
    _, max_y, max_y_id = sorted_y[-1]
    _, sec_max_y, sec_max_y_id = sorted_y[-2]

    # Candidate cows to remove (those affecting the bounding box)
    candidates = {
        min_x_id, sec_min_x_id, max_x_id, sec_max_x_id,
        min_y_id, sec_min_y_id, max_y_id, sec_max_y_id
    }

    best_area = None
    # Compute area for each removal candidate
    for cid in candidates:
        # Determine new min_x
        if cid != min_x_id:
            cur_min_x = min_x
        else:
            cur_min_x = sec_min_x
        # New max_x
        if cid != max_x_id:
            cur_max_x = max_x
        else:
            cur_max_x = sec_max_x
        # New min_y
        if cid != min_y_id:
            cur_min_y = min_y
        else:
            cur_min_y = sec_min_y
        # New max_y
        if cid != max_y_id:
            cur_max_y = max_y
        else:
            cur_max_y = sec_max_y

        # Compute area, note area = 0 if line
        area = (cur_max_x - cur_min_x) * (cur_max_y - cur_min_y)
        if best_area is None or area < best_area:
            best_area = area

    # Output result
    print(best_area if best_area is not None else 0)

if __name__ == '__main__':
    main()
