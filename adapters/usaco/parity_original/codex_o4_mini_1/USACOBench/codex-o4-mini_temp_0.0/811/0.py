#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, B = map(int, input().split())
    f = list(map(int, input().split()))
    # boots attributes (1-indexed)
    s = [0] * (B + 1)
    d = [0] * (B + 1)
    for i in range(1, B + 1):
        si, di = map(int, input().split())
        s[i], d[i] = si, di
    INF = 10**18
    # dp[i][b] = min discards to reach tile i wearing boot b
    dp = [[INF] * (B + 1) for _ in range(N)]
    # initial: at tile 0 (f[0]=0), can wear any boot b by discarding b-1 boots
    for b in range(1, B + 1):
        if s[b] >= f[0]:
            dp[0][b] = b - 1
    # fill dp
    for i in range(N):
        for b in range(1, B + 1):
            cost = dp[i][b]
            if cost == INF:
                continue
            # move forward up to d[b] steps
            maxstep = d[b]
            for k in range(i + 1, min(N, i + maxstep + 1)):
                if f[k] <= s[b] and dp[k][b] > cost:
                    dp[k][b] = cost
            # switch to a deeper boot
            for nb in range(b + 1, B + 1):
                if s[nb] >= f[i]:
                    newcost = cost + (nb - b - 1)
                    if dp[i][nb] > newcost:
                        dp[i][nb] = newcost
    # answer is min over boots at last tile
    ans = min(dp[N - 1][b] for b in range(1, B + 1))
    print(ans)

if __name__ == '__main__':
    main()
