#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    A = int(next(it))
    B = int(next(it))
    friends = []
    for _ in range(N):
        P = int(next(it))
        C = int(next(it))
        X = int(next(it))
        friends.append((X, C, P))
    # Sort friends by discount cost X ascending
    friends.sort(key=lambda x: x[0])
    # dp[m][b] = max popularity with m mooney used and b ice used
    # initialize with -1 (unreachable)
    dp = [[-1] * (B+1) for _ in range(A+1)]
    dp[0][0] = 0
    for X, C, P in friends:
        # in-place 0-1 group: iterate backwards
        for m in range(A, -1, -1):
            for b in range(B, -1, -1):
                if dp[m][b] < 0:
                    continue
                # remaining ice for discounts
                rem_ice = B - b
                # max discounts possible for this friend
                d = rem_ice // X
                if d > C:
                    d = C
                m2 = m + C - d
                b2 = b + d * X
                if m2 <= A and b2 <= B:
                    val = dp[m][b] + P
                    if val > dp[m2][b2]:
                        dp[m2][b2] = val
    # find best
    ans = 0
    for m in range(A+1):
        for b in range(B+1):
            if dp[m][b] > ans:
                ans = dp[m][b]
    print(ans)

if __name__ == '__main__':
    main()
