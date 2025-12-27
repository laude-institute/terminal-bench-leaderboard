#!/usr/bin/env python3
import sys
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    A = int(next(it))
    B = int(next(it))
    friends = []
    for _ in range(N):
        P = int(next(it)); C = int(next(it)); X = int(next(it))
        friends.append((P, C, X))
    # dp[a][b] = max total popularity with a mooney and b ice creams
    dp = [[0] * (B + 1) for _ in range(A + 1)]
    for P, C, X in friends:
        # consider using k discounts (ice creams) for this friend
        max_k = min(C, B // X) if X > 0 else 0
        # precompute cost pairs
        costs = [(C, 0)]  # no discount
        for k in range(1, max_k + 1):
            costs.append((C - k, k * X))
        # update dp in reverse to avoid reuse
        for cost_m, cost_b in costs:
            # skip invalid
            if cost_m < 0 or cost_b > B:
                continue
            for a in range(A, cost_m - 1, -1):
                row = dp[a]
                prev_row = dp[a - cost_m]
                # iterate b reverse
                for b in range(B, cost_b - 1, -1):
                    val = prev_row[b - cost_b] + P
                    if val > row[b]:
                        row[b] = val
    # answer is best at full budgets
    print(dp[A][B])

if __name__ == '__main__':
    main()
