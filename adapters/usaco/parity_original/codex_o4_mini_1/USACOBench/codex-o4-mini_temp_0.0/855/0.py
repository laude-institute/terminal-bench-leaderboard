#!/usr/bin/env python3
"""
Simulate 100 milk pouring operations among three buckets.
"""
def main():
    # Read capacities and initial amounts for three buckets
    capacities = []
    amounts = []
    for _ in range(3):
        c, m = map(int, input().split())
        capacities.append(c)
        amounts.append(m)
    # Perform 100 pours in cyclic order
    for i in range(100):
        src = i % 3
        dst = (i + 1) % 3
        transfer = min(amounts[src], capacities[dst] - amounts[dst])
        amounts[src] -= transfer
        amounts[dst] += transfer
    # Output final amounts
    for amt in amounts:
        print(amt)

if __name__ == '__main__':
    main()
