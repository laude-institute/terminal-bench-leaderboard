#!/usr/bin/env python3
"""
Reads N and petal counts of N flowers, then computes the number of
contiguous photo ranges that contain a flower whose petal count equals
the exact average petal count of that range.
"""

def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    petals = list(map(int, data[1:1+N]))
    count = 0

    # Iterate over all contiguous ranges [i, j]
    for i in range(N):
        total = 0
        for j in range(i, N):
            total += petals[j]
            length = j - i + 1
            # Check if average is an integer
            if total % length == 0:
                avg = total // length
                # Check if any flower in the range has petal count == avg
                for k in range(i, j + 1):
                    if petals[k] == avg:
                        count += 1
                        break

    # Output the result
    print(count)

if __name__ == "__main__":
    main()
