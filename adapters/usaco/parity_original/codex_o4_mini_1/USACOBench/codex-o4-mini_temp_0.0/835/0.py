#!/usr/bin/env python3
"""
Read N cows with their maximum wait tolerances w_i.
Compute the minimum number of cows that can end up in the lemonade line
by choosing an arrival order adversarially.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    w = list(map(int, data[1:1+n]))
    # To minimize joins, let cows with highest tolerances arrive first
    w.sort(reverse=True)
    count = 0
    # Greedily accept a cow if her tolerance >= current line length
    for wi in w:
        if wi >= count:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
