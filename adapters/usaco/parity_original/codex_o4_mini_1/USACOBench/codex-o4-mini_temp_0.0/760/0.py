#!/usr/bin/env python3

def main():
    import sys
    data = sys.stdin.read().strip().split()
    # Number of cows
    N = int(data[0])
    # Shuffle mapping a_i (1-based positions)
    a = list(map(int, data[1:1+N]))
    # Cow IDs after three shuffles
    ids = list(map(int, data[1+N:1+2*N]))

    # Reverse the shuffle three times
    for _ in range(3):
        prev = [0] * N
        for i in range(N):
            # Cow at position i before shuffle comes from position a[i]
            prev[i] = ids[a[i] - 1]
        ids = prev

    # Output original ordering
    out = '\n'.join(str(x) for x in ids)
    sys.stdout.write(out)


if __name__ == '__main__':
    main()
