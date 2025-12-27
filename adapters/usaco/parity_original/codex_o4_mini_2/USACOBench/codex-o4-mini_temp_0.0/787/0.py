#!/usr/bin/env python3
import sys
import bisect

def main():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    cows = [int(input()) for _ in range(N)]
    stores = [tuple(map(int, input().split())) for _ in range(M)]
    rents = [int(input()) for _ in range(R)]

    # Sort cows by production descending and compute prefix sums
    cows.sort(reverse=True)
    milk_psum = [0] * (N + 1)
    for i in range(1, N + 1):
        milk_psum[i] = milk_psum[i-1] + cows[i-1]

    # Sort stores by price descending and compute cumulative capacity and revenue
    stores.sort(key=lambda x: -x[1])
    caps_psum = []
    rev_psum = []
    total_cap = total_rev = 0
    for q, p in stores:
        total_cap += q
        total_rev += q * p
        caps_psum.append(total_cap)
        rev_psum.append(total_rev)

    # Sort rentals by price descending and compute prefix sums
    rents.sort(reverse=True)
    rent_psum = [0] * (R + 1)
    for i in range(1, R + 1):
        rent_psum[i] = rent_psum[i-1] + rents[i-1]

    # Try milking k cows and renting the rest
    best = 0
    for k in range(N + 1):
        milk = milk_psum[k]
        # Compute milk revenue via binary search in caps_psum
        if milk == 0 or M == 0:
            milk_rev = 0
        else:
            idx = bisect.bisect_left(caps_psum, milk)
            if idx >= M:
                milk_rev = rev_psum[-1]
            else:
                prev_cap = caps_psum[idx-1] if idx > 0 else 0
                prev_rev = rev_psum[idx-1] if idx > 0 else 0
                extra = milk - prev_cap
                milk_rev = prev_rev + extra * stores[idx][1]
        # Compute rental revenue for remaining cows
        num_rent = min(N - k, R)
        rent_rev = rent_psum[num_rent]

        best = max(best, milk_rev + rent_rev)

    print(best)

if __name__ == "__main__":
    main()
