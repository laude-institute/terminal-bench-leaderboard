#!/usr/bin/env python3
"""
Solution to USACO 'haywire' problem.
Find ordering of cows minimizing total wire length between friends.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # adjacency list: friends of each cow 1..N
    adj = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        friends = list(map(int, input().split()))
        adj[i] = friends

    # position of each cow in the ordering, -1 if not placed
    pos = [-1] * (N+1)
    best = [float('inf')]

    def dfs(depth, visited_mask, current_cost):
        # Prune if cost already exceeds best
        if current_cost >= best[0]:
            return
        # All cows placed
        if depth == N:
            best[0] = current_cost
            return

        # Try placing each unvisited cow at this position
        for cow in range(1, N+1):
            bit = 1 << (cow - 1)
            if visited_mask & bit:
                continue
            # compute cost increment for connecting this cow to already placed friends
            inc = 0
            for f in adj[cow]:
                if pos[f] != -1:
                    inc += depth - pos[f]
            # place cow
            pos[cow] = depth
            dfs(depth + 1, visited_mask | bit, current_cost + inc)
            # backtrack
            pos[cow] = -1

    # start DFS
    dfs(0, 0, 0)
    # output result
    print(best[0])

if __name__ == '__main__':
    main()
