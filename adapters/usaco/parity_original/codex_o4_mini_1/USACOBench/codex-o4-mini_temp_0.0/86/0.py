#!/usr/bin/env python3
"""
Solution to the Moo Sick problem:
Identifies all transposed/reordered occurrences of a given chord in a song.
"""
import sys

def main():
    input = sys.stdin.readline
    # Read number of notes in the song
    N = int(input().strip())
    # Read the song notes
    song = [int(input().strip()) for _ in range(N)]
    # Read chord size and chord notes
    C = int(input().strip())
    chord = [int(input().strip()) for _ in range(C)]

    # Compute the normalized interval pattern of the chord
    chord.sort()
    chord_pattern = [chord[i] - chord[0] for i in range(C)]

    # Slide a window over the song and compare patterns
    occurrences = []
    for i in range(N - C + 1):
        window = song[i:i+C]
        window.sort()
        window_pattern = [window[j] - window[0] for j in range(C)]
        if window_pattern == chord_pattern:
            # Record 1-based starting index
            occurrences.append(i + 1)

    # Output results
    print(len(occurrences))
    for idx in occurrences:
        print(idx)

if __name__ == '__main__':
    main()
