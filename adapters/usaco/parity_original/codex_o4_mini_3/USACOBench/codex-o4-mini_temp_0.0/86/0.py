#!/usr/bin/env python3
"""
Solution to Moo Sick problem.
Reads song notes and chord pattern, finds all starting indices of chord occurrences
considering transpositions and reorderings.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    # Number of notes in the song
    N = int(next(it))
    # Song notes
    song = [int(next(it)) for _ in range(N)]
    # Chord length
    C = int(next(it))
    # Chord pattern notes
    chord = [int(next(it)) for _ in range(C)]
    # Prepare chord signature: sorted offsets from the minimum note
    chord.sort()
    chord_signature = tuple(c - chord[0] for c in chord)

    results = []
    # Slide through the song
    for i in range(N - C + 1):
        window = song[i:i + C]
        window.sort()
        # Compute signature of this window
        window_signature = tuple(w - window[0] for w in window)
        if window_signature == chord_signature:
            # Record 1-based starting index
            results.append(i + 1)

    # Output results
    print(len(results))
    for idx in results:
        print(idx)

if __name__ == '__main__':
    main()
