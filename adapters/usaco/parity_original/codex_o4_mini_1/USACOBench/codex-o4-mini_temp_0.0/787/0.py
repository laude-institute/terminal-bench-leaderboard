#!/usr/bin/env python3
import sys
import bisect

def main():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    cows = [int(input()) for _ in range(N)]
    stores = []
    for _ in range(M):
        q, p = map(int, input().split())
        stores.append((p, q))
    rentals = [int(input()) for _ in range(R)]

    # Sort cows by milk production descending
    cows.sort(reverse=True)
    # Prefix sum of milk production
    milk_prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        milk_prefix[i] = milk_prefix[i-1] + cows[i-1]

    # Sort stores by price descending
    stores.sort(key=lambda x: x[0], reverse=True)
    # Prefix sums for store quantities and revenue
    store_qty = [0] * (M + 1)
    store_money = [0] * (M + 1)
    for i in range(1, M + 1):
        p, q = stores[i-1]
        store_qty[i] = store_qty[i-1] + q
        store_money[i] = store_money[i-1] + q * p

    # Sort rentals descending and prefix sum
    rentals.sort(reverse=True)
    rent_prefix = [0] * (min(R, N) + 1)
    for i in range(1, len(rent_prefix)):
        rent_prefix[i] = rent_prefix[i-1] + rentals[i-1]

    # Helper to compute milk revenue for given total milk
    def milk_revenue(total_milk):
        # find number of full stores
        idx = bisect.bisect_right(store_qty, total_milk) - 1
        rev = store_money[idx]
        remaining = total_milk - store_qty[idx]
        if idx + 1 <= M and remaining > 0:
            price, qty = stores[idx]
            rev += remaining * price
        return rev

    # Try renting j cows (highest rental offers) and milking rest
    max_profit = 0
    max_rent = min(R, N)
    for j in range(0, max_rent + 1):
        milk_cows = N - j
        total_milk = milk_prefix[milk_cows]
        profit = rent_prefix[j] + milk_revenue(total_milk)
        if profit > max_profit:
            max_profit = profit

    print(max_profit)

if __name__ == '__main__':
    main()
