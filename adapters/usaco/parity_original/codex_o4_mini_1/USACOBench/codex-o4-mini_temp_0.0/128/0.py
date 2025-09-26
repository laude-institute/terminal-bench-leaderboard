#!/usr/bin/env python3
"""
Haybale Restacking: minimal work to transform current piles A into target piles B on a circle.
Approach: compute prefix imbalances, find median imbalance, sum distances.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Compute prefix sums of (B_i - A_i)
    prefix = []
    s = 0
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        s += (b - a)
        prefix.append(s)
    # Find median of prefix sums
    # The sum over all (b-a) is zero, so prefix[-1] == 0
    sorted_pref = sorted(prefix)
    # median at index n//2
    med = sorted_pref[n // 2]
    # Compute total work as sum of abs(prefix[i] - med)
    total = 0
    for x in prefix:
        total += abs(x - med)
    print(total)

if __name__ == '__main__':
    main()
