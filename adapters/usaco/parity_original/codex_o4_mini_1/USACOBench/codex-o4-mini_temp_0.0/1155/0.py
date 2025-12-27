#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1].strip()
    # Helper to count substrings with exactly one of target and length>=3
    def count_lonely(ch):
        # positions with sentinel at 0 and n+1
        pos = [0]
        for i, c in enumerate(s, start=1):
            if c == ch:
                pos.append(i)
        pos.append(n+1)
        total = 0
        # iterate over each real occurrence
        for j in range(1, len(pos)-1):
            p = pos[j]
            L = pos[j-1] + 1
            R = pos[j+1] - 1
            left = p - L + 1
            right = R - p + 1
            # total substrings containing only this ch
            cnt = left * right
            # subtract substrings of length <3 (len 1 and len 2)
            # always substring [p,p]
            invalid = 1
            # length 2 to left
            if p - L >= 1:
                invalid += 1
            # length 2 to right
            if R - p >= 1:
                invalid += 1
            total += cnt - invalid
        return total

    # count for G and for H
    result = count_lonely('G') + count_lonely('H')
    print(result)

if __name__ == '__main__':
    main()
