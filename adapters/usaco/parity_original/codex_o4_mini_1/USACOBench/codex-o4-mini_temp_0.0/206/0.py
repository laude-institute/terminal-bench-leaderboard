#!/usr/bin/env python3
"""
Solution to 'Scrambled Letters' problem.
Computes the minimum and maximum possible original positions of each scrambled cow name.
"""
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    names = data[1:]

    # Compute lexicographically smallest and largest anagrams
    min_strs = []  # smallest anagram of each name
    max_strs = []  # largest anagram of each name
    for s in names:
        sorted_chars = sorted(s)
        min_strs.append(''.join(sorted_chars))
        max_strs.append(''.join(reversed(sorted_chars)))

    # Prepare sorted lists for binary search
    sorted_mins = sorted(min_strs)
    sorted_maxs = sorted(max_strs)

    # Determine positions
    output = []
    for min_s, max_s in zip(min_strs, max_strs):
        # Minimum position: 1 + count of other names whose max_anagram < this min_anagram
        min_pos = bisect.bisect_left(sorted_maxs, min_s) + 1
        # Maximum position: count of names whose min_anagram <= this max_anagram
        max_pos = bisect.bisect_right(sorted_mins, max_s)
        output.append(f"{min_pos} {max_pos}")

    sys.stdout.write("\n".join(output))

if __name__ == '__main__':
    main()
