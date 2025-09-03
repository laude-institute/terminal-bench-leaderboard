#!/usr/bin/env python3
def main():
    n = int(input().strip())
    a = [int(input().strip()) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    for length in range(2, n+1):
        for l in range(n-length+1):
            r = l + length - 1
            for k in range(l, r):
                if dp[l][k] and dp[l][k] == dp[k+1][r]:
                    dp[l][r] = dp[l][k] + 1
                    break
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] > ans:
                ans = dp[i][j]
    print(ans)

if __name__ == "__main__":
    main()
