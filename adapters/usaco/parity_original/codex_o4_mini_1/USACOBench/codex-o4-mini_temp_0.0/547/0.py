#!/usr/bin/env python3
"""
Farmer John has N hay bales at various positions along a road.
Bessie the cow is trapped between bales and can break through a bale
if she can build up speed over D units, where D is the distance she runs.
She can break any bale of size strictly less than D, removing it permanently.
Compute the total length of starting positions from which she cannot escape
past the leftmost or rightmost bale.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    bales = []  # list of (position, size)
    for _ in range(N):
        size, pos = map(int, input().split())
        bales.append((pos, size))
    bales.sort()
    positions = [p for p, s in bales]
    sizes = [s for p, s in bales]

    ans = 0
    i, j = 0, 1
    # two-pointer scan for trapped intervals
    while i < N and j < N:
        if i == j:
            j += 1
            continue
        dist = positions[j] - positions[i]
        # if distance > left bale size, left bale breaks
        if dist > sizes[i]:
            i += 1
        # if distance > right bale size, right bale breaks
        elif dist > sizes[j]:
            j += 1
        else:
            # neither bale can break: trapped interval
            ans += dist
            i += 1
            j = i + 1

    print(ans)

if __name__ == "__main__":
    main()
