#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    B = int(next(it))
    P = []  # gift prices
    S = []  # shipping costs
    for _ in range(N):
        p = int(next(it)); s = int(next(it))
        P.append(p); S.append(s)
    # total cost without coupon
    A = [P[i] + S[i] for i in range(N)]
    # cost with coupon on gift i
    C = [P[i] // 2 + S[i] for i in range(N)]
    # sort A with original indices
    sorted_A = sorted((A[i], i) for i in range(N))
    # prefix sums of sorted A-values
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + sorted_A[i][0]
    # map original index to position in sorted_A
    pos_in_sorted = [0] * N
    for idx, (_, orig) in enumerate(sorted_A):
        pos_in_sorted[orig] = idx

    # check if we can gift k cows within budget
    def feasible(k):
        if k == 0:
            return True
        # need k-1 full-price gifts and one coupon gift
        for i in range(N):
            # cost for coupon on cow i
            cost = C[i]
            # sum of k-1 smallest A[j] for j != i
            pos = pos_in_sorted[i]
            if k-1 <= 0:
                sumA = 0
            elif pos >= k-1:
                sumA = prefix[k-1]
            else:
                # cow i is among the k-1 cheapest, take one more
                sumA = prefix[k] - A[i]
            if cost + sumA <= B:
                return True
        return False

    # binary search max k
    low, high = 0, N
    while low < high:
        mid = (low + high + 1) // 2
        if feasible(mid):
            low = mid
        else:
            high = mid - 1
    print(low)

if __name__ == '__main__':
    main()
