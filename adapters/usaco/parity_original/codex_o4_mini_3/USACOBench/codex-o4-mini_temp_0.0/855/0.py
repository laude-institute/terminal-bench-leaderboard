#!/usr/bin/env python3
import sys

def main():
    # Read capacities and initial amounts
    capacities = []
    milk = []
    for _ in range(3):
        c, m = map(int, sys.stdin.readline().split())
        capacities.append(c)
        milk.append(m)

    # Perform 100 pour operations in cycle: 0->1,1->2,2->0
    for i in range(100):
        src = i % 3
        dst = (i + 1) % 3
        amount = min(milk[src], capacities[dst] - milk[dst])
        milk[src] -= amount
        milk[dst] += amount

    # Output final milk amounts
    for m in milk:
        print(m)

if __name__ == "__main__":
    main()
