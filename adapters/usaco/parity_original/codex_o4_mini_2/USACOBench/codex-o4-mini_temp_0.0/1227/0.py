#!/usr/bin/env python3
"""
Compute minimum number of even-length prefix reversals
to maximize Guernseys ('G') at even positions.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    s = data[1].strip()
    # Count Gs at even positions initially
    initial_even = sum(1 for i in range(1, N+1) if i % 2 == 0 and s[i-1] == 'G')
    # Track G counts in prefix
    prefix_even = 0
    prefix_odd = 0
    best_delta = 0
    # Iterate through prefixes
    for i, ch in enumerate(s, start=1):
        if ch == 'G':
            if i % 2 == 0:
                prefix_even += 1
            else:
                prefix_odd += 1
        # Only consider even-length prefixes
        if i % 2 == 0:
            # Reversal effect: G at odd -> even (+1), G at even -> odd (-1)
            delta = prefix_odd - prefix_even
            if delta > best_delta:
                best_delta = delta
    # If we can improve, one reversal suffices
    result = 1 if best_delta > 0 else 0
    print(result)

if __name__ == '__main__':
    main()
