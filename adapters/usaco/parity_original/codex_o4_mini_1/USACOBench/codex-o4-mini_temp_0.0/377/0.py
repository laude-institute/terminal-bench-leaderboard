#!/usr/bin/env python3
import sys
from fractions import Fraction as F

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    times = []
    ds = []
    idx = 1
    for _ in range(N):
        typ = data[idx]
        x = int(data[idx+1])
        idx += 2
        if typ == 'T':
            times.append(x)
        else:
            ds.append(x)
    times.sort()
    ds.sort()
    t = F(0, 1)
    d = F(0, 1)
    k = 0
    i = j = 0
    N_t = len(times)
    N_d = len(ds)
    # Process events until reaching 1000 meters
    while d < 1000:
        # If no more events, break
        if i >= N_t and j >= N_d:
            break
        # Next time-based event
        next_time = F(times[i], 1) if i < N_t else None
        # Next distance-based event time
        if j < N_d:
            next_dist = ds[j]
            delta_d = F(next_dist, 1) - d
            next_dist_time = t + delta_d * (k + 1)
        else:
            next_dist_time = None
        # Decide which event comes first
        if next_time is not None and (next_dist_time is None or next_time <= next_dist_time):
            # Advance to next time event
            delta_t = next_time - t
            d += delta_t / (k + 1)
            t = next_time
            # Apply all time events at this time
            while i < N_t and F(times[i], 1) == next_time:
                k += 1
                i += 1
        else:
            # Advance to next distance event
            next_dist = ds[j]
            delta_t = (F(next_dist, 1) - d) * (k + 1)
            t += delta_t
            d = F(next_dist, 1)
            # Apply all distance events at this location
            while j < N_d and ds[j] == next_dist:
                k += 1
                j += 1
    # Finish remaining distance
    if d < 1000:
        delta_d = F(1000, 1) - d
        t += delta_d * (k + 1)
    # Round to nearest integer (0.5 rounds up)
    result = int(t + F(1, 2))
    print(result)

if __name__ == "__main__":
    main()
