#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    # Read segments: list of (type, lo, hi)
    segments = []
    idx = 1
    for _ in range(n):
        typ = data[idx]; a = int(data[idx+1]); b = int(data[idx+2])
        segments.append((typ, a, b))
        idx += 3

    # Compute initial range by reversing from end to start
    lo, hi = 0, 10**9
    for typ, a, b in reversed(segments):
        if typ == "none":
            lo = max(lo, a)
            hi = min(hi, b)
        elif typ == "on":
            # On ramp added going forward => subtract to reverse
            lo = max(0, lo - b)
            hi = hi - a
        elif typ == "off":
            # Off ramp removed going forward => add to reverse
            lo = lo + a
            hi = hi + b
    # Record initial range
    init_lo, init_hi = lo, hi

    # Compute final range by forward simulation
    lo, hi = 0, 10**9
    for typ, a, b in segments:
        if typ == "none":
            lo = max(lo, a)
            hi = min(hi, b)
        elif typ == "on":
            lo = lo + a
            hi = hi + b
        elif typ == "off":
            lo = max(0, lo - b)
            hi = hi - a
    fin_lo, fin_hi = lo, hi

    # Output results
    print(f"{init_lo} {init_hi}")
    print(f"{fin_lo} {fin_hi}")

if __name__ == "__main__":
    main()
