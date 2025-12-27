#!/usr/bin/env python3
"""
Cow Race
Counts leadership changes between Bessie and Elsie.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    idx = 2
    bessie = []
    for _ in range(n):
        speed = int(data[idx])
        time = int(data[idx+1])
        idx += 2
        bessie.append((speed, time))
    elsie = []
    for _ in range(m):
        speed = int(data[idx])
        time = int(data[idx+1])
        idx += 2
        elsie.append((speed, time))

    total_time = sum(t for _, t in bessie)
    # Initialize pointers and counters
    di_b, di_e = 0, 0
    i_b, i_e = 0, 0
    rem_b = bessie[0][1]
    rem_e = elsie[0][1]
    sp_b = bessie[0][0]
    sp_e = elsie[0][0]
    prev_leader = 0  # 0=tie, 1=bessie, 2=elsie
    changes = 0

    for _ in range(total_time):
        # Advance distances
        di_b += sp_b
        di_e += sp_e
        # Decrease remaining times and update segments
        rem_b -= 1
        if rem_b == 0 and i_b + 1 < n:
            i_b += 1
            sp_b, rem_b = bessie[i_b]
        rem_e -= 1
        if rem_e == 0 and i_e + 1 < m:
            i_e += 1
            sp_e, rem_e = elsie[i_e]

        # Determine leader
        if di_b > di_e:
            new_leader = 1
        elif di_e > di_b:
            new_leader = 2
        else:
            new_leader = 0

        # Count leadership change
        if new_leader != prev_leader and new_leader != 0 and prev_leader != 0:
            changes += 1
        # Update previous leader when non-tie
        if new_leader != 0:
            prev_leader = new_leader

    print(changes)

if __name__ == '__main__':
    main()
