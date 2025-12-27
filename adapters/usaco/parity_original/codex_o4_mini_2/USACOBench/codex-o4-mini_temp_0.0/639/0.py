#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    sizes = list(map(int, data[2:]))
    sizes.sort()
    ans = 0
    j = 0
    for i in range(N):
        while sizes[i] - sizes[j] > K:
            j += 1
        current_count = i - j + 1
        if current_count > ans:
            ans = current_count
    print(ans)

if __name__ == '__main__':
    main()
