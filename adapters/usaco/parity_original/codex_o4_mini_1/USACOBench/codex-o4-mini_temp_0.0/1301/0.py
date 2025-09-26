#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    days = list(map(int, data[2:]))
    # Initial cost: one subscription per day (each costs 1+K)
    total = N * (K + 1)
    # Merge subscriptions across small gaps when beneficial
    for i in range(1, N):
        gap = days[i] - days[i - 1]
        # If gap <= K+1, merging saves (K+1 - gap) cost
        if gap <= K + 1:
            total -= (K + 1 - gap)
    print(total)


if __name__ == "__main__":
    main()
