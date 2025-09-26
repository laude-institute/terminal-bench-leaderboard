#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    p = list(map(int, data[1:]))
    # Count length of longest increasing suffix
    count = 1
    for i in range(N - 2, -1, -1):
        if p[i] < p[i + 1]:
            count += 1
        else:
            break
    # Minimum moves is total cows minus suffix length
    print(N - count)


if __name__ == '__main__':
    main()
