#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    s = data[1].strip()
    # Compute initial count of G at even positions (1-based)
    E_orig = 0
    for i, ch in enumerate(s, start=1):
        if ch == 'G' and i % 2 == 0:
            E_orig += 1
    # Prepare for best prefix reversal gain (one operation)
    prefix = 0
    best1 = 0
    # Prepare for best segment flip gain (two operations)
    best2 = 0
    min_pref_even = 0
    # Compute both gains in one pass
    prefix1 = 0
    for i, ch in enumerate(s, start=1):
        # B value: +1 for G at odd, -1 for G at even, 0 otherwise
        if ch == 'G':
            B = 1 if i % 2 == 1 else -1
        else:
            B = 0
        # For best1 (prefix ending at even)
        prefix1 += B
        if i % 2 == 0:
            if prefix1 > best1:
                best1 = prefix1
        # For best2 (segment [l,r] with l odd, r even)
        prefix += B
        if i % 2 == 0:
            # candidate segment sum ending here
            gain = prefix - min_pref_even
            if gain > best2:
                best2 = gain
            # update minimal even-indexed prefix
            if prefix < min_pref_even:
                min_pref_even = prefix
    # Determine answer based on maximal achievable gain
    max_gain = max(best2, 0)
    if max_gain == 0:
        print(0)
    elif best1 == max_gain:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
