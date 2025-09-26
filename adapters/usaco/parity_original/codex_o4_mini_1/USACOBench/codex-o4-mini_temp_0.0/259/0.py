#!/usr/bin/env python3
"""
Cow Race: count leadership changes between Bessie and Elsie.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    # Read Bessie's segments
    bessie = [(int(next(it)), int(next(it))) for _ in range(N)]
    # Read Elsie's segments
    elsie = [(int(next(it)), int(next(it))) for _ in range(M)]
    # Total time (same for both)
    total_time = sum(t for _, t in bessie)

    # Initialize pointers and statuses
    iB = iE = 0
    remB = bessie[0][1]
    remE = elsie[0][1]
    speedB = bessie[0][0]
    speedE = elsie[0][0]
    distB = distE = 0
    last_leader = None
    changes = 0

    # Simulate each time unit
    for _ in range(total_time):
        # Move cows
        distB += speedB
        distE += speedE
        # Decrease remaining times
        remB -= 1
        remE -= 1
        # Advance Bessie segment
        if remB == 0 and iB + 1 < N:
            iB += 1
            speedB, remB = bessie[iB]
        # Advance Elsie segment
        if remE == 0 and iE + 1 < M:
            iE += 1
            speedE, remE = elsie[iE]

        # Determine current leader
        if distB > distE:
            new_leader = 'B'
        elif distE > distB:
            new_leader = 'E'
        else:
            new_leader = None

        # Count leadership change (ignore initial take)
        if new_leader is not None and new_leader != last_leader:
            if last_leader is not None:
                changes += 1
            last_leader = new_leader

    # Output result
    print(changes)

if __name__ == '__main__':
    main()
