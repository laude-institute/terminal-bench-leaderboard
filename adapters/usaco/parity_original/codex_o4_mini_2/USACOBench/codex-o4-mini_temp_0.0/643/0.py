#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, k = map(int, data[:2])
    sizes = list(map(int, data[2:2+n]))
    sizes.sort()
    # Compute for each i the farthest index r[i] such that sizes[r] - sizes[i] <= k
    n = len(sizes)
    r = [0] * n
    j = 0
    for i in range(n):
        while j < n and sizes[j] - sizes[i] <= k:
            j += 1
        r[i] = j - 1
    # w[i] is number of diamonds in window starting at i
    w = [r[i] - i + 1 for i in range(n)]
    # suffix_max[i] = max(w[i], w[i+1], ...)
    suffix_max = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_max[i] = max(w[i], suffix_max[i+1])
    # Compute best total by picking first window at i and second after r[i]
    ans = 0
    for i in range(n):
        total = w[i]
        if r[i] + 1 < n:
            total += suffix_max[r[i] + 1]
        ans = max(ans, total)
    print(ans)


if __name__ == '__main__':
    main()
