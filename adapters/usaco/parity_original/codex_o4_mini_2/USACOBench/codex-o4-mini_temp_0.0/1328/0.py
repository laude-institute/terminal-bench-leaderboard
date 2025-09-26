#!/usr/bin/env python3
import sys

def main():
    t = sys.stdin.readline().strip()
    # Pattern and mapping for transitions
    # States 0..5 represent matched prefix length of "bessie"
    cnt = [0] * 6
    # Map characters to pattern indices where they match
    char_map = {'b': [0], 'e': [1, 5], 's': [2, 3], 'i': [4]}
    total = 0
    g_sum = 0
    for c in t:
        # Extend existing substrings by c
        if c in char_map:
            for k in reversed(char_map[c]):
                move = cnt[k]
                if move:
                    cnt[k] -= move
                    if k < 5:
                        cnt[k+1] += move
                    else:
                        # Completed a "bessie"
                        cnt[0] += move
                        g_sum += move
        # Add new substring starting at this character
        if c == 'b':
            cnt[1] += 1
        else:
            cnt[0] += 1
        # Accumulate total patterns over all substrings ending here
        total += g_sum
    # Output result
    print(total)

if __name__ == '__main__':
    main()
