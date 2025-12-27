#!/usr/bin/env python3
"""
Reads a list of days and subscription constant K, then computes
the minimum cost to cover all viewing days with subscriptions.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    days = list(map(int, data[2:2+N]))
    # Start with covering the first day: cost = 1 day + K
    cost = K + 1
    # For each subsequent day, decide to extend or start new
    for i in range(1, N):
        gap = days[i] - days[i-1]
        # Cost to extend subscription: gap days
        # Cost to start new: 1 day + K
        if gap <= K + 1:
            cost += gap
        else:
            cost += K + 1
    print(cost)

if __name__ == '__main__':
    main()
