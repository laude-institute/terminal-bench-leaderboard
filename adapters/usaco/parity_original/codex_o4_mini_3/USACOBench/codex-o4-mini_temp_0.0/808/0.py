#!/usr/bin/env python3
"""
Hoofball solution: compute minimum initial balls so every cow receives ball.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    xs = list(map(int, input().split()))
    xs.sort()
    # Determine pass targets
    pass_to = [0] * N
    for i in range(N):
        if i == 0:
            pass_to[i] = 1
        elif i == N - 1:
            pass_to[i] = N - 2
        else:
            left_dist = xs[i] - xs[i-1]
            right_dist = xs[i+1] - xs[i]
            # tie -> left
            if left_dist <= right_dist:
                pass_to[i] = i - 1
            else:
                pass_to[i] = i + 1
    # Count indegrees
    indegree = [0] * N
    for i in range(N):
        indegree[pass_to[i]] += 1
    # Initial balls for cows with zero indegree
    result = sum(1 for i in range(N) if indegree[i] == 0)
    # Handle mutual pairs with no other incoming
    for i in range(N):
        j = pass_to[i]
        if j > i and pass_to[j] == i and indegree[i] == 1 and indegree[j] == 1:
            result += 1
    print(result)

if __name__ == "__main__":
    main()
