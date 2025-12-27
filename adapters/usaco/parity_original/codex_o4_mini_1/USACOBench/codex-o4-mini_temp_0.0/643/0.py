#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    sizes = [int(next(it)) for _ in range(n)]
    sizes.sort()

    # Compute max window ending at each j
    left_len = [0] * n
    l = 0
    for j in range(n):
        while sizes[j] - sizes[l] > k:
            l += 1
        left_len[j] = j - l + 1
    # Prefix max of left_len
    prefix_max = [0] * n
    for j in range(n):
        if j == 0:
            prefix_max[j] = left_len[j]
        else:
            prefix_max[j] = max(prefix_max[j-1], left_len[j])

    # Compute max window starting at each i
    start_len = [0] * n
    r = n - 1
    for i in range(n-1, -1, -1):
        while sizes[r] - sizes[i] > k:
            r -= 1
        start_len[i] = r - i + 1
    # Suffix max of start_len
    suffix_max = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], start_len[i])

    # Combine two disjoint windows
    ans = 0
    for split in range(-1, n):
        left = prefix_max[split] if split >= 0 else 0
        right = suffix_max[split+1] if split+1 < n else 0
        ans = max(ans, left + right)
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
