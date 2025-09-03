#!/usr/bin/env python3
import sys

def main():
    import sys
    data = sys.stdin
    n = int(data.readline())
    # Read bales as (position, size)
    bales = []
    for _ in range(n):
        size, pos = map(int, data.readline().split())
        bales.append((pos, size))
    # Sort by position
    bales.sort()
    # Stack of potential left barriers: list of (position, size)
    stack = []
    trapped_length = 0
    for pos, size in bales:
        # Try to form a trapping interval with stack top
        while stack:
            left_pos, left_size = stack[-1]
            gap = pos - left_pos
            # If left barrier is breakable, remove it
            if left_size < gap:
                stack.pop()
            # If current barrier is breakable, cannot trap with this left
            elif size < gap:
                break
            else:
                # Both barriers strong enough: trap interval
                trapped_length += gap
                break
        # Push current as a potential barrier
        stack.append((pos, size))
    # Output total trapped area
    print(trapped_length)

if __name__ == '__main__':
    main()
