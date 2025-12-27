#!/usr/bin/env python3
"""
Solution for delegation selection problem.
Counts contiguous intervals [l, r] where outer breeds are unique in interval.
Uses BIT for range counting with activation events.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    b = list(map(int, data[1:]))

    # Compute previous occurrences
    prev = [0] * n
    last = {}
    for i in range(n):
        prev[i] = last.get(b[i], -1)
        last[b[i]] = i

    # Compute next occurrences
    nxt = [n] * n
    last.clear()
    for i in range(n - 1, -1, -1):
        nxt[i] = last.get(b[i], n)
        last[b[i]] = i

    # Activation list: at l, activate all r with prev[r] + 1 == l
    activation = [[] for _ in range(n + 1)]
    for r in range(n):
        act = prev[r] + 1
        activation[act].append(r)

    # BIT for counting active r positions
    class BIT:
        def __init__(self, size):
            self.n = size
            self.ft = [0] * (size + 1)

        def add(self, i, v):
            i += 1
            while i <= self.n:
                self.ft[i] += v
                i += i & -i

        def sum(self, i):
            s = 0
            i += 1
            while i > 0:
                s += self.ft[i]
                i -= i & -i
            return s

    bit = BIT(n)
    ans = 0

    # Sweep l from 0 to n-1
    for l in range(n):
        # Activate r's where prev[r] < l
        for r in activation[l]:
            bit.add(r, 1)

        # Count r in [l+1, nxt[l]-1]
        left = l + 1
        right = nxt[l] - 1
        if left <= right:
            ans += bit.sum(right) - bit.sum(l)

    # Output result
    print(ans)


if __name__ == '__main__':
    main()
