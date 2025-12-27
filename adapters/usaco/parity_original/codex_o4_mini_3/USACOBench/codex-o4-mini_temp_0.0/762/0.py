#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    scores = [int(next(it)) for _ in range(n)]

    # Precompute suffix sums and suffix minimums
    suffix_sum = [0] * (n + 1)
    suffix_min = [0] * n
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + scores[i]
        if i == n - 1:
            suffix_min[i] = scores[i]
        else:
            suffix_min[i] = min(scores[i], suffix_min[i + 1])

    best_num = -1  # numerator of best average
    best_den = 1   # denominator of best average
    result = []
    # Iterate K from 1 to n-2
    for k in range(1, n - 1):
        rem = n - k
        if rem < 2:
            break
        total = suffix_sum[k]
        m = suffix_min[k]
        num = total - m
        den = rem - 1
        # Compare num/den vs best_num/best_den via cross multiplication
        if best_num * den < num * best_den:
            best_num, best_den = num, den
            result = [k]
        elif best_num * den == num * best_den:
            result.append(k)

    # Output results
    out = sys.stdout
    for k in result:
        out.write(str(k))
        out.write("\n")

if __name__ == '__main__':
    main()
