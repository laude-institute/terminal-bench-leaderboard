#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    # Read number of distinct output entries
    N = int(data.readline())
    # Read counts of cows by output
    cows = []  # list of tuples (output, count)
    for _ in range(N):
        count, output = map(int, data.readline().split())
        cows.append((output, count))
    # Sort by milk output
    cows.sort()
    # Two pointers to pair smallest with largest
    i, j = 0, len(cows) - 1
    max_time = 0
    while i <= j:
        out_i, cnt_i = cows[i]
        out_j, cnt_j = cows[j]
        if i < j:
            # Pair as many as possible between these groups
            pairs = min(cnt_i, cnt_j)
            max_time = max(max_time, out_i + out_j)
            # Decrease counts
            cnt_i -= pairs
            cnt_j -= pairs
            # Update or advance pointers
            if cnt_i == 0:
                i += 1
            else:
                cows[i] = (out_i, cnt_i)
            if cnt_j == 0:
                j -= 1
            else:
                cows[j] = (out_j, cnt_j)
        else:
            # Same group: must pair within group (count is even)
            max_time = max(max_time, out_i * 2)
            break
    # Output the minimum time needed
    print(max_time)

if __name__ == "__main__":
    main()
