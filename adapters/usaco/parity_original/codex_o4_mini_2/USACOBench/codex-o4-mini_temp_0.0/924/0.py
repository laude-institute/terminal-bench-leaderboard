#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    n = int(data.readline())
    probs = [int(data.readline()) for _ in range(n)]
    ans = 0.0
    prod_q = 1.0  # product of (1 - p_i)
    sum_pq = 0.0  # sum of p_i / (1 - p_i)
    left = 0
    for right in range(n):
        p = probs[right] / 1e6
        q = 1.0 - p
        prod_q *= q
        sum_pq += p / q
        # shrink window while sum_pq >= 1 to maintain optimal range
        while left <= right and sum_pq >= 1.0:
            p_l = probs[left] / 1e6
            q_l = 1.0 - p_l
            prod_q /= q_l
            sum_pq -= p_l / q_l
            left += 1
        # update answer: probability of exactly one acceptance
        current = prod_q * sum_pq
        if current > ans:
            ans = current
    # output scaled by 1e6 and floored to integer
    print(int(ans * 1e6))

if __name__ == '__main__':
    main()
