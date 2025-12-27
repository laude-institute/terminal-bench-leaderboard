#!/usr/bin/env python3
"""
Restate the problem:
Given a string S and deletion costs for each character, delete characters
to maximize the number of times "bessie" appears as a contiguous substring
in the resulting string, and minimize total deletion cost.

Conceptual solution:
Use dynamic programming with 6 states (one for each prefix length of "bessie").
State dp[j] stores the best (count, cost) after processing characters,
having matched j letters of the current "bessie". At each character, we
choose to delete it (incurring cost) or keep it. Keeping advances the state
if it matches the next needed letter, completes a pattern, or breaks current match.

Pseudocode:
# Initialize dp[0]=(0,0), dp[1..5]=(-inf,inf)
for each character S[i] with cost c:
    dp2 = [(-inf, inf)] * 6
    for j in 0..5:
        (cnt, cost0) = dp[j]
        # Option 1: delete
        update dp2[j] with (cnt, cost0 + c)
        # Option 2: keep
        if S[i] == pattern[j]:
            if j == 5:
                update dp2[0] with (cnt+1, cost0)
            else:
                update dp2[j+1] with (cnt, cost0)
        else:
            update dp2[0] with (cnt, cost0)
    dp = dp2
# Answer is best over dp[0..5]

import sys
def main():
    S = sys.stdin.readline().strip()
    costs = list(map(int, sys.stdin.readline().split()))
    n = len(S)
    pattern = "bessie"
    m = len(pattern)
    INF = 10**18
    # dp[j] = (count, cost)
    dp = [(-10**9, INF)] * m
    dp[0] = (0, 0)
    for i in range(n):
        ch = S[i]
        c = costs[i]
        dp2 = [(-10**9, INF)] * m
        for j in range(m):
            cnt, cost0 = dp[j]
            # delete
            cand = (cnt, cost0 + c)
            if cand[0] > dp2[j][0] or (cand[0] == dp2[j][0] and cand[1] < dp2[j][1]):
                dp2[j] = cand
            # keep
            if ch == pattern[j]:
                if j == m-1:
                    cand2 = (cnt + 1, cost0)
                    if cand2[0] > dp2[0][0] or (cand2[0] == dp2[0][0] and cand2[1] < dp2[0][1]):
                        dp2[0] = cand2
                else:
                    cand2 = (cnt, cost0)
                    if cand2[0] > dp2[j+1][0] or (cand2[0] == dp2[j+1][0] and cand2[1] < dp2[j+1][1]):
                        dp2[j+1] = cand2
            else:
                # keep as extraneous, break match
                cand2 = (cnt, cost0)
                if cand2[0] > dp2[0][0] or (cand2[0] == dp2[0][0] and cand2[1] < dp2[0][1]):
                    dp2[0] = cand2
        dp = dp2
    # get best result
    best = dp[0]
    for j in range(1, m):
        if dp[j][0] > best[0] or (dp[j][0] == best[0] and dp[j][1] < best[1]):
            best = dp[j]
    # output
    print(best[0])
    print(best[1])

if __name__ == '__main__':
    main()
