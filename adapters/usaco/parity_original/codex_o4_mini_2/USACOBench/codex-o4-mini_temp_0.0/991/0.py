#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.readline().split()
    N = int(data[0])
    K = int(data[1])
    M = int(data[2])

    def can_repay(X):
        days = 0
        paid = 0
        # simulate repayment in jumps
        while days < K and paid < N:
            # compute today's payment
            y = (N - paid) // X
            if y < M:
                # pay minimum for remaining days
                # days needed to finish
                remaining = N - paid
                # compute needed days by ceiling division
                need_days = (remaining + M - 1) // M
                days += need_days
                break
            # compute number of days we can keep paying y before it changes
            # t = floor((N - paid - X*y) / y) + 1
            t = (N - paid - X * y) // y + 1
            # don't exceed available days
            if days + t > K:
                t = K - days
            days += t
            paid += t * y
        # success if within K days
        return days <= K

    # binary search for largest X
    low, high = 1, N
    answer = 1
    while low <= high:
        mid = (low + high) // 2
        if can_repay(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    print(answer)

if __name__ == '__main__':
    main()
