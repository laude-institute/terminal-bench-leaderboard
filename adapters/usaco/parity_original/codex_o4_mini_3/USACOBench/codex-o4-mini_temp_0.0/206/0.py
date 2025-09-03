#!/usr/bin/env python3
import sys
import bisect

def main():
    input = sys.stdin.readline
    n = int(input())
    s = [input().strip() for _ in range(n)]

    min_strs = [''.join(sorted(name)) for name in s]
    max_strs = [''.join(sorted(name, reverse=True)) for name in s]

    sorted_mins = sorted(min_strs)
    sorted_maxs = sorted(max_strs)

    for i in range(n):
        mn = min_strs[i]
        mx = max_strs[i]
        # lowest possible position
        c_min = bisect.bisect_left(sorted_maxs, mn)
        min_rank = c_min + 1
        # highest possible position
        c_max = bisect.bisect_right(sorted_mins, mx)
        max_rank = c_max
        sys.stdout.write(f"{min_rank} {max_rank}\n")

if __name__ == "__main__":
    main()
