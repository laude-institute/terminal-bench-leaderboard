#!/usr/bin/env python3
"""
Simulate 100 milk-pour operations among three buckets.
"""
def main():
    # Read capacities and initial milk amounts
    capacities = []
    milk = []
    for _ in range(3):
        c, m = map(int, input().split())
        capacities.append(c)
        milk.append(m)

    # Perform 100 pours in cycle: 0->1,1->2,2->0
    for i in range(100):
        src = i % 3
        dst = (src + 1) % 3
        amount_to_pour = min(milk[src], capacities[dst] - milk[dst])
        milk[src] -= amount_to_pour
        milk[dst] += amount_to_pour

    # Output final amounts
    for amt in milk:
        print(amt)

if __name__ == "__main__":
    main()
