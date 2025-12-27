#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    b = list(map(int, data[1:]))
    # Try each possible first value to find lexicographically smallest
    for first in range(1, N+1):
        a = [first]
        ok = True
        for bi in b:
            nxt = bi - a[-1]
            # Check valid range
            if nxt < 1 or nxt > N:
                ok = False
                break
            a.append(nxt)
        # Check for valid permutation
        if ok and len(set(a)) == N:
            print(' '.join(map(str, a)))
            return

if __name__ == '__main__':
    main()
