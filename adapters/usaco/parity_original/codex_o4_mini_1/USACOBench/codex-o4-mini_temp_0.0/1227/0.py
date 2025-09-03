#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1]
    # Total Guernseys
    total_g = s.count('G')
    # Count Gs at even positions (1-based indexing)
    init_even = sum(1 for i, c in enumerate(s, start=1) if i % 2 == 0 and c == 'G')
    # Max possible Gs at even positions
    max_even_possible = min(total_g, n // 2)
    # How many more we need
    needed = max_even_possible - init_even
    if needed <= 0:
        print(0)
        return
    # Compute best single reversal delta
    odd_count = 0
    even_count = 0
    best_delta = 0
    # Iterate prefixes of even length
    for i, c in enumerate(s, start=1):
        if i % 2 == 1:
            if c == 'G':
                odd_count += 1
        else:
            if c == 'G':
                even_count += 1
            # Only consider even-length prefix
            delta = odd_count - even_count
            if delta > best_delta:
                best_delta = delta
    # If one reversal suffices
    if best_delta >= needed:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
