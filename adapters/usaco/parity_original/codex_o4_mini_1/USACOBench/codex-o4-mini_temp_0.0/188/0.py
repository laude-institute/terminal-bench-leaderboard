#!/usr/bin/env python3
import sys

def count_flips(s: str) -> int:
    n = len(s)
    # If length is odd, can't be balanced
    if n % 2 != 0:
        return 0
    # Map parentheses to +1 / -1
    vals = [1 if c == '(' else -1 for c in s]
    # Total sum
    total = sum(vals)
    # Determine target total change
    # Flipping '(' -> ')' changes total by -2, ')' -> '(' by +2
    # To be balanced, new total must be 0
    if total == 2:
        # must flip one '(' to ')'
        target_char = '('
        # for suffix, need prefix[j] >= 2
        require = 2
    elif total == -2:
        # must flip one ')' to '('
        target_char = ')'
        # for suffix, need prefix[j] >= -2
        require = -2
    else:
        return 0
    # Compute prefix sums and prefix minimums
    prefix = [0] * n
    prefix_min = [0] * n
    curr = 0
    for i, v in enumerate(vals):
        curr += v
        prefix[i] = curr
        prefix_min[i] = curr if i == 0 else min(prefix_min[i-1], curr)
    # Compute suffix minimums of prefix
    suffix_min = [0] * n
    for i in range(n-1, -1, -1):
        if i == n-1:
            suffix_min[i] = prefix[i]
        else:
            suffix_min[i] = min(prefix[i], suffix_min[i+1])
    # Count valid flips
    ans = 0
    for i, c in enumerate(s):
        if c != target_char:
            continue
        # check prefix before i stays >= 0
        if i > 0 and prefix_min[i-1] < 0:
            continue
        # check suffix from i onward after flip stays >=0
        # after flip, all prefix[j] for j>=i change by -2 if '('->')' or +2 if ')'
        # so original prefix[j] must be >= require
        if suffix_min[i] < require:
            continue
        ans += 1
    return ans

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    s = data
    print(count_flips(s))

if __name__ == '__main__':
    main()
