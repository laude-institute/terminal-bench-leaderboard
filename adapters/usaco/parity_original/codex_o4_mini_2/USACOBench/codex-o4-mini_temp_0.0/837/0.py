#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    # Read values with original indices
    a = list(map(int, data[1:1+n]))
    indexed = list(enumerate(a))  # (orig_index, value)
    # Stable sort by value
    sorted_list = sorted(indexed, key=lambda x: x[1])
    # Compute maximum displacement
    max_disp = 0
    for sorted_idx, (orig_idx, _) in enumerate(sorted_list):
        disp = abs(orig_idx - sorted_idx)
        if disp > max_disp:
            max_disp = disp
    # Each iteration moves at most 2 steps towards final
    # Number of 'moo's is at least 1
    ans = (max_disp + 1) // 2
    if ans < 1:
        ans = 1
    print(ans)

if __name__ == '__main__':
    main()
