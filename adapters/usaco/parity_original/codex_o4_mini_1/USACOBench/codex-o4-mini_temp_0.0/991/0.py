#!/usr/bin/env python3
import sys

def can_repay(N, K, M, X):
    days = 0
    paid = 0
    # simulate repayment in chunks
    while days < K and paid < N:
        remaining = N - paid
        # daily payment based on X
        y = remaining // X
        if y < M:
            # once base rate applies, pay M for all remaining days
            paid += (K - days) * M
            break
        # compute how many days this payment y remains constant
        # solve for d: remaining - d*y < X*y -> d > (remaining - X*y)/y
        # so max full days with this y is:
        d = (remaining - X * y) // y + 1
        # cap to remaining days
        if d <= 0:
            d = 1
        if days + d > K:
            d = K - days
        # advance
        paid += d * y
        days += d
    return paid >= N

def main():
    data = sys.stdin.read().strip().split()
    N, K, M = map(int, data)
    # binary search for largest X
    low, high = 1, N
    while low < high:
        mid = (low + high + 1) // 2
        if can_repay(N, K, M, mid):
            low = mid
        else:
            high = mid - 1
    print(low)

if __name__ == '__main__':
    main()
