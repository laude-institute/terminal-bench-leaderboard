#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    B = int(next(it))
    P = [0]*N
    S = [0]*N
    for i in range(N):
        P[i] = int(next(it))
        S[i] = int(next(it))
    # compute normal and half costs
    normal = [P[i] + S[i] for i in range(N)]
    half = [P[i]//2 + S[i] for i in range(N)]
    # sort normal costs and record positions
    sc = sorted([(normal[i], i) for i in range(N)])
    sorted_costs = [c for c, _ in sc]
    pos = [0]*N
    for idx, (_, i) in enumerate(sc):
        pos[i] = idx
    # build prefix sums of sorted costs
    prefix = [0]*N
    for i in range(N):
        prefix[i] = sorted_costs[i] + (prefix[i-1] if i > 0 else 0)
    result = 0
    # try using coupon on each cow
    for i in range(N):
        cost_with_coupon = half[i]
        if cost_with_coupon > B:
            continue
        budget_rem = B - cost_with_coupon
        # binary search max m other cows
        low, high = 0, N-1
        best = 0
        while low <= high:
            mid = (low + high) // 2
            # sum of mid cheapest excluding i
            if mid == 0:
                s = 0
            else:
                if pos[i] >= mid:
                    s = prefix[mid-1]
                else:
                    s = prefix[mid] - sorted_costs[pos[i]]
            if s <= budget_rem:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        # update result: coupon cow + best others
        result = max(result, best + 1)
    # output maximum cows
    print(result)

if __name__ == "__main__":
    main()
