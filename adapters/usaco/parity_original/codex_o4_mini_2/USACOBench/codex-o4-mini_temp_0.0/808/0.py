#!/usr/bin/env python3
"""
Solution for the hoofball problem.
Reads N and positions, computes minimum initial balls needed.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    xs = list(map(int, input().split()))
    # Pair positions with original indices and sort by position
    cows = sorted((x, i) for i, x in enumerate(xs))
    # out[i] = index of cow to which cow i passes
    out = [None] * N
    for idx, (x, i) in enumerate(cows):
        # determine nearest neighbor
        if idx == 0:
            target = cows[1][1]
        elif idx == N - 1:
            target = cows[N - 2][1]
        else:
            left_x, left_i = cows[idx - 1]
            right_x, right_i = cows[idx + 1]
            if x - left_x <= right_x - x:
                target = left_i
            else:
                target = right_i
        out[i] = target
    # compute indegrees
    indegree = [0] * N
    for i in range(N):
        indegree[out[i]] += 1
    # count cows with zero inbound passes
    zero_in = sum(1 for d in indegree if d == 0)
    # count mutual pairs with no other inbound edges
    mutual = 0
    for i in range(N):
        j = out[i]
        if out[j] == i and i < j and indegree[i] == 1 and indegree[j] == 1:
            mutual += 1
    print(zero_in + mutual)

if __name__ == '__main__':
    main()
