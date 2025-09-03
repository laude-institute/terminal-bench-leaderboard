#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    N, K, M = map(int, data)

    def can(X):
        days = 0
        given = 0
        # Simulate repayment in O(log N) steps
        while days < K and given < N:
            # Compute amount to give today
            y = (N - given) // X
            if y < M:
                # If below minimum, give M for remaining days
                given += (K - days) * M
                break
            # Determine how many days this y persists
            maxd = ((N - given) - y * X) // y + 1
            if days + maxd > K:
                maxd = K - days
            given += maxd * y
            days += maxd
        return given >= N

    # Binary search for largest X
    lo, hi = 1, N
    ans = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if can(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)

if __name__ == "__main__":
    main()
