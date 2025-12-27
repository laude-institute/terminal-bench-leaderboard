#!/usr/bin/env python3
import sys

def main():
    # Read cowphabet order and heard sequence
    order = sys.stdin.readline().strip()
    heard = sys.stdin.readline().strip()

    # Map each letter to its index in the cowphabet
    index_map = {ch: i for i, ch in enumerate(order)}

    count = 1  # at least one full hum
    prev_idx = -1
    for ch in heard:
        idx = index_map[ch]
        # If current letter comes before or same as previous, a new hum starts
        if idx <= prev_idx:
            count += 1
        prev_idx = idx

    # Output the minimum number of hums
    print(count)

if __name__ == '__main__':
    main()
