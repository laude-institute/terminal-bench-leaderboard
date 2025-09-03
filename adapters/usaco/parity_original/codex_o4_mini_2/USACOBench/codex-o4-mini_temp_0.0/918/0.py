#!/usr/bin/env python3
"""
Solution to the 'Herding' problem: compute minimum and maximum moves to
arrange cows into consecutive positions under given move constraints.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    xs = sorted(int(x) for x in data[1:])

    # Compute minimum moves
    # Special case check for near-complete sequences
    inf = 10**18
    # Check two special patterns
    if (xs[-2] - xs[0] == n-2 and xs[-1] - xs[-2] > 2) or \
       (xs[-1] - xs[1] == n-2 and xs[1] - xs[0] > 2):
        min_moves = 2
    else:
        # Sliding window: max cows in any interval of length n
        max_in = 0
        j = 0
        for i in range(n):
            while j < n and xs[j] - xs[i] < n:
                j += 1
            # cows in [i, j-1]
            max_in = max(max_in, j - i)
        min_moves = n - max_in

    # Compute maximum moves
    # We can move endpoints inward one at a time
    max_moves = max(xs[-1] - xs[1], xs[-2] - xs[0]) - (n - 2)

    # Output results
    print(min_moves)
    print(max_moves)

if __name__ == "__main__":
    main()
