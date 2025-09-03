#!/usr/bin/env python3
"""
Compute all K such that after discarding the first K scores,
dropping the minimum remaining score, and averaging the rest,
the resulting average is maximized.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = list(map(int, data[1:]))

    # Compute suffix sums and suffix minimums
    suffix_sum = [0] * (n + 1)
    suffix_min = [10**18] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + scores[i]
        suffix_min[i] = min(suffix_min[i + 1], scores[i])

    best_num = -1
    best_den = 1
    result = []

    # Try all K from 1 to n-2
    for k in range(1, n - 1):
        # remaining count = n - k
        # after dropping one min, count = n - k - 1
        num = suffix_sum[k] - suffix_min[k]
        den = n - k - 1
        # Compare fractions num/den vs best_num/best_den
        if num * best_den > best_num * den:
            best_num, best_den = num, den
            result = [k]
        elif num * best_den == best_num * den:
            result.append(k)

    # Output results
    out = sys.stdout
    for k in result:
        out.write(str(k) + "\n")


if __name__ == '__main__':
    main()
