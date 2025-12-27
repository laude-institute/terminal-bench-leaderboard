#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # Adjacency list of friends for each cow (1-based index)
    friends = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        friends[i] = list(map(int, input().split()))

    best = [float('inf')]
    pos = [0] * (N+1)
    used = [False] * (N+1)

    def dfs(k, cost):
        # Prune if cost already exceeds best found
        if cost >= best[0]:
            return
        # All stalls filled
        if k == N:
            best[0] = cost
            return

        # Try placing each unused cow in stall k
        for cow in range(1, N+1):
            if not used[cow]:
                added = 0
                # Add cost for wires to already placed friends
                for fr in friends[cow]:
                    if used[fr]:
                        added += abs(k - pos[fr])
                used[cow] = True
                pos[cow] = k
                dfs(k+1, cost + added)
                used[cow] = False

    dfs(0, 0)
    print(best[0])

if __name__ == '__main__':
    main()
