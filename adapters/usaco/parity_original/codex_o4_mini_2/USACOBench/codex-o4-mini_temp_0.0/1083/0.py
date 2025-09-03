#!/usr/bin/env python3
import sys

def main():
    # Read cowphabet ordering and heard string
    cowphabet = sys.stdin.readline().strip()
    heard = sys.stdin.readline().strip()

    # Map each cowphabet letter to its index
    order = {ch: i for i, ch in enumerate(cowphabet)}

    # Count how many full sequences are needed
    cycles = 1
    last_pos = -1
    for ch in heard:
        pos = order[ch]
        # If current letter is not after previous, start new cycle
        if pos <= last_pos:
            cycles += 1
        last_pos = pos

    # Output result
    print(cycles)

if __name__ == '__main__':
    main()
