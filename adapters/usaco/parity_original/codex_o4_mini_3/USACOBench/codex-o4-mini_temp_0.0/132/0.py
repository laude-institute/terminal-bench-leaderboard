#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    H = list(map(int, data[1:]))
    # Pair each height with its index and sort descending
    idxs = sorted([(h, i) for i, h in enumerate(H)], reverse=True)
    active = [False] * n
    islands = 0
    max_islands = 0
    i = 0
    # Activate cells from highest to lowest height
    while i < n:
        current_h = idxs[i][0]
        # Process all cells with this height
        j = i
        while j < n and idxs[j][0] == current_h:
            pos = idxs[j][1]
            left = active[pos - 1] if pos - 1 >= 0 else False
            right = active[pos + 1] if pos + 1 < n else False
            # Determine island count change
            if not left and not right:
                islands += 1
            elif left and right:
                islands -= 1
            # Mark as land (emerged)
            active[pos] = True
            j += 1
        # Update maximum islands after this height
        max_islands = max(max_islands, islands)
        i = j
    print(max_islands)

if __name__ == '__main__':
    main()
