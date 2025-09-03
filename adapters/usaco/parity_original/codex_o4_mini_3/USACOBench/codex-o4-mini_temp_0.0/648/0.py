#!/usr/bin/env python3
"""
Solution for merging adjacent equal integers to maximize largest value.
"""
import sys, math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    a = [0] * N
    for i in range(N):
        a[i] = int(next(it))
    # Initial maximum value
    ans = max(a)
    # Maximum possible merges add ~log2(N)
    lg = int(math.log2(N)) + 1 if N > 0 else 1
    K_max = ans + lg
    # dp_prev[i] = end index if segment at i merges to k-1
    prev_dp = [0] * N
    # Initialize for k=1 based on singletons
    for i in range(N):
        if a[i] == 1:
            prev_dp[i] = i + 1
    if any(prev_dp):
        ans = max(ans, 1)
    # Iterate k from 2 up to K_max
    for k in range(2, K_max + 1):
        curr_dp = [0] * N
        merged_any = False
        pd = prev_dp
        for i in range(N):
            j = pd[i]
            # merge two (k-1) segments
            if j and j < N and pd[j]:
                curr_dp[i] = pd[j]
                merged_any = True
            # singleton equals k
            elif a[i] == k:
                curr_dp[i] = i + 1
                merged_any = True
        # update answer if any segment forms k
        if merged_any:
            ans = max(ans, k)
        # prepare for next iteration
        prev_dp = curr_dp
    # Output result
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
