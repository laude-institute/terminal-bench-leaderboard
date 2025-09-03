#!/usr/bin/env python3
"""
Formats an essay with words on lines no longer than K characters (excluding spaces).
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    # First two entries are N and K
    N, K = map(int, data[:2])
    words = data[2:]
    curr_len = 0
    first = True
    for w in words:
        wlen = len(w)
        # If word fits on current line
        if curr_len + wlen <= K:
            if not first:
                # separate with space
                sys.stdout.write(' ')
            sys.stdout.write(w)
            curr_len += wlen
        else:
            # new line
            sys.stdout.write('\n' + w)
            curr_len = wlen
        first = False
    sys.stdout.write('\n')

if __name__ == '__main__':
    main()
