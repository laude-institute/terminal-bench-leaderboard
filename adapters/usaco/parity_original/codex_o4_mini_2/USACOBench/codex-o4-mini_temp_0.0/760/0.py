#!/usr/bin/env python3
"""
Reads a shuffle mapping and final cow order after three shuffles,
then computes and prints the original cow order before shuffling.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    # Parse input
    n = int(data[0])
    # Shuffle mapping a: cow at position i moves to a[i]
    a = list(map(int, data[1:1+n]))
    # IDs of cows after three shuffles
    final_ids = list(data[1+n:1+2*n])

    # Reverse the shuffle three times to recover initial order
    curr = final_ids
    for _ in range(3):
        prev = [None] * n
        # old[i] = curr[a[i] - 1]
        for i in range(n):
            prev[i] = curr[a[i] - 1]
        curr = prev

    # Output the initial ordering, one per line
    out = '\n'.join(curr)
    print(out)

if __name__ == '__main__':
    main()
