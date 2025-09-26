#!/usr/bin/env python3
import sys

def main():
    N = int(sys.stdin.readline().strip())
    # Build lengths of S(k) until it covers N
    lengths = [3]
    k = 0
    while lengths[k] < N:
        k += 1
        lengths.append(2 * lengths[k-1] + (k + 3))

    def find_char(k, n):
        if k == 0:
            return 'm' if n == 1 else 'o'
        left = lengths[k-1]
        mid = k + 3
        if n <= left:
            return find_char(k-1, n)
        elif n <= left + mid:
            return 'm' if n - left == 1 else 'o'
        else:
            return find_char(k-1, n - left - mid)

    result = find_char(k, N)
    sys.stdout.write(result)

if __name__ == '__main__':
    main()
