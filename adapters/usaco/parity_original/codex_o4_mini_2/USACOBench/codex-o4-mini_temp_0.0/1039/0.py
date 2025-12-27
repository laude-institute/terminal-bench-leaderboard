#!/usr/bin/env python3
"""
Solution to the cereal distribution problem.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    fav = [0] * N
    sec = [0] * N
    for i in range(N):
        fav[i] = int(next(it)) - 1
        sec[i] = int(next(it)) - 1

    taken = [-1] * M
    ans = [0] * N
    total = 0

    # Add cows from back to front
    for i in range(N - 1, -1, -1):
        cereal = fav[i]
        curr = i
        # Try to assign cereal, bumping as needed
        while True:
            owner = taken[cereal]
            if owner == -1:
                taken[cereal] = curr
                total += 1
                break
            if owner < curr:
                # current cereal owner has priority
                break
            # bump the current owner
            taken[cereal] = curr
            curr = owner
            cereal = sec[curr]
        ans[i] = total

    # Output results
    out = '\n'.join(str(x) for x in ans)
    sys.stdout.write(out)

if __name__ == '__main__':
    main()
