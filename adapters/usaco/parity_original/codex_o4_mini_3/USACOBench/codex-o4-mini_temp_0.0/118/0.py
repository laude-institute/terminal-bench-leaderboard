#!/usr/bin/env python3
import sys
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    M = int(next(it))
    P = [0]*N
    C = [0]*N
    for i in range(N):
        P[i] = int(next(it))
        C[i] = int(next(it))
    # prepare sorted by delta (P-C)
    delta_idx = sorted(range(N), key=lambda i: P[i]-C[i])
    # prefix sums of P for sorted by delta
    prefP = [0]*(N+1)
    for i, idx in enumerate(delta_idx):
        prefP[i+1] = prefP[i] + P[idx]
    # sorted by C for coupon selection
    C_sorted = sorted(range(N), key=lambda i: C[i])

    def can_buy(x):
        k = min(K, x)
        full_count = x - k
        # sum of P for full_price cows = first full_count of sorted by delta
        sum_full = prefP[full_count]
        # mark full cows
        used = [False]*N
        for i in range(full_count):
            used[delta_idx[i]] = True
        # select k coupon cows from remaining by smallest C
        sum_coupon = 0
        cnt = 0
        for i in C_sorted:
            if not used[i]:
                sum_coupon += C[i]
                cnt += 1
                if cnt == k:
                    break
        if cnt < k:
            return False
        return sum_full + sum_coupon <= M

    # binary search max x
    low, high = 0, N+1
    while low + 1 < high:
        mid = (low + high) // 2
        if can_buy(mid):
            low = mid
        else:
            high = mid
    print(low)

if __name__ == "__main__":
    main()
