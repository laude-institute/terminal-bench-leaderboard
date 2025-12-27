#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    a = list(map(int, data[1:]))
    # Maximum initial value and upper bound for possible merges
    max_initial = max(a)
    max_k = max_initial + N.bit_length() + 2
    # dp[k] maps start index to end index for segments collapsible to k
    dp = [dict() for _ in range(max_k + 1)]
    # Initialize base segments of length 1
    for i, v in enumerate(a):
        dp[v][i] = i + 1
    ans = max_initial
    # Build up possible merges for each k
    for k in range(1, max_k):
        cur = dp[k]
        if not cur:
            continue
        # Try merging two adjacent segments of value k
        for start, mid in list(cur.items()):
            if mid in cur:
                dp[k + 1][start] = cur[mid]
                if k + 1 > ans:
                    ans = k + 1
    # Output the highest achievable value
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
