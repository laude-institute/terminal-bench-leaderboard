#!/usr/bin/env python3
import sys

def can_afford(prices, ships, full_costs_sorted, B, k, N):
    # Try using coupon on each cow
    for i in range(N):
        discounted = prices[i] // 2 + ships[i]
        # need k-1 cheapest full costs excluding cow i
        if k - 1 > N - 1:
            continue
        total = discounted
        cnt = 0
        # sum k-1 smallest full costs skipping i
        for cost, j in full_costs_sorted:
            if j == i:
                continue
            total += cost
            cnt += 1
            if cnt == k-1:
                break
        if cnt < k-1:
            continue
        if total <= B:
            return True
    return False

def main():
    data = sys.stdin.read().split()
    N, B = map(int, data[:2])
    nums = list(map(int, data[2:]))
    prices = []
    ships = []
    for i in range(0, 2*N, 2):
        prices.append(nums[i])
        ships.append(nums[i+1])
    # precompute full costs
    full_costs = [(prices[i] + ships[i], i) for i in range(N)]
    full_costs_sorted = sorted(full_costs, key=lambda x: x[0])
    # binary search on k
    low, high = 0, N
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid == 0 or can_afford(prices, ships, full_costs_sorted, B, mid, N):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

if __name__ == "__main__":
    main()
