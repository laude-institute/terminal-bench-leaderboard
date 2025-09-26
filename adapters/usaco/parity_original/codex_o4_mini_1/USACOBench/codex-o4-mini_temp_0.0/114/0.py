#!/usr/bin/env python3
import sys

def main():
    input_data = sys.stdin.read().strip()
    N = int(input_data)

    # Precompute lengths of S(k) until >= N
    lengths = [3]
    k = 0
    while lengths[k] < N:
        k += 1
        lengths.append(lengths[k-1] * 2 + (k + 3))

    # Recursive function to find Nth character in S(k)
    def find_char(n, k):
        if k == 0:
            # S(0) = "moo"
            return 'm' if n == 1 else 'o'
        left_len = lengths[k-1]
        mid_len = k + 3
        if n <= left_len:
            return find_char(n, k-1)
        elif n <= left_len + mid_len:
            # Middle block: 'm' followed by o's
            return 'm' if n - left_len == 1 else 'o'
        else:
            return find_char(n - left_len - mid_len, k-1)

    # Output result
    sys.stdout.write(find_char(N, k))


if __name__ == '__main__':
    main()
