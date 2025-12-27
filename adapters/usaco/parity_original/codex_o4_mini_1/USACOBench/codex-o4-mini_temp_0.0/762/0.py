#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = list(map(int, data[1:]))
    # Compute suffix sums
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + scores[i]
    # Compute suffix minimums
    INF = 10**18
    suffix_min = [INF] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(scores[i], suffix_min[i + 1])
    # Find best K values
    best_num = -1
    best_den = 1
    results = []
    # K from 1 to n-2 inclusive
    for k in range(1, n - 1):
        # Remaining count = n-k, after dropping one => denom = n-k-1
        num = suffix_sum[k] - suffix_min[k]
        den = n - k - 1
        # Compare num/den to best_num/best_den via cross multiplication
        if best_num * den < num * best_den:
            best_num, best_den = num, den
            results = [k]
        elif best_num * den == num * best_den:
            results.append(k)
    # Output results
    out = sys.stdout
    for k in results:
        out.write(f"{k}\n")

if __name__ == '__main__':
    main()
