#!/usr/bin/env python3
"""
Solution to USACO 'moosick' problem.
Reads N notes and a chord pattern of length C, then finds all starting indices
where a window matches the chord under any transposition and reordering.
"""
import sys

def main():
    input = sys.stdin.readline
    # Read number of notes in the song
    N = int(input().strip())
    notes = [int(input().strip()) for _ in range(N)]
    # Read chord pattern length and notes
    C = int(input().strip())
    pattern = [int(input().strip()) for _ in range(C)]
    # Sort pattern and compute interval signature
    pattern.sort()
    diff_pattern = [pattern[i+1] - pattern[i] for i in range(C-1)]

    results = []
    # Slide window over the song
    for i in range(N - C + 1):
        window = notes[i:i+C]
        window.sort()
        # Compute window interval signature
        diff_window = [window[j+1] - window[j] for j in range(C-1)]
        # Compare signatures
        if diff_window == diff_pattern:
            # Record 1-based start index
            results.append(i+1)

    # Output results
    print(len(results))
    for idx in results:
        print(idx)

if __name__ == '__main__':
    main()
