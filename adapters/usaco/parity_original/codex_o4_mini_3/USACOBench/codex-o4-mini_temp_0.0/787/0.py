#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    R = int(next(it))
    # Read cow productions
    cows = [int(next(it)) for _ in range(N)]
    # Read stores: (price, quantity)
    stores = []
    for _ in range(M):
        q = int(next(it)); p = int(next(it))
        stores.append((p, q))
    # Read rentals
    rents = [int(next(it)) for _ in range(R)]

    # Sort cows by production descending
    cows.sort(reverse=True)
    # Sort stores by price descending
    stores.sort(key=lambda x: x[0], reverse=True)
    # Sort rents descending
    rents.sort(reverse=True)

    # Prefix sum for rental incomes
    rent_prefix = [0] * (min(N, R) + 1)
    for i in range(1, len(rent_prefix)):
        rent_prefix[i] = rent_prefix[i-1] + rents[i-1]

    # Precompute milk income for k cows milked (top k producers)
    milk_income = [0] * (N+1)
    store_idx = 0
    store_rem = stores[0][1] if stores else 0
    cur_rev = 0
    for k in range(1, N+1):
        milk = cows[k-1]
        # Sell this milk greedily
        while milk > 0 and store_idx < M:
            price, _ = stores[store_idx]
            take = min(milk, store_rem)
            cur_rev += take * price
            milk -= take
            store_rem -= take
            if store_rem == 0:
                store_idx += 1
                if store_idx < M:
                    store_rem = stores[store_idx][1]
        milk_income[k] = cur_rev

    # Try all splits: rent i cows, milk N-i cows
    max_income = 0
    # Only up to min(N, R) cows can be rented
    max_rent = min(N, R)
    for i in range(0, max_rent+1):
        milk_cows = N - i
        total = rent_prefix[i] + milk_income[milk_cows]
        if total > max_income:
            max_income = total

    # Also consider renting fewer than available rental offers
    print(max_income)

if __name__ == '__main__':
    main()
