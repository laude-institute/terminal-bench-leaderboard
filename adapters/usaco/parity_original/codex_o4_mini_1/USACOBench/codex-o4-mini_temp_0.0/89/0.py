#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    cows = []
    breeds = set()
    for _ in range(n):
        x = int(next(it))
        b = int(next(it))
        cows.append((x, b))
        breeds.add(b)
    cows.sort(key=lambda cb: cb[0])
    total_breeds = len(breeds)

    count = {}
    have = 0
    ans = float('inf')
    left = 0
    # sliding window over sorted cows
    for right in range(n):
        _, b = cows[right]
        count[b] = count.get(b, 0) + 1
        if count[b] == 1:
            have += 1
        # try to shrink window
        while have == total_breeds and left <= right:
            width = cows[right][0] - cows[left][0]
            if width < ans:
                ans = width
            # remove left cow
            _, bl = cows[left]
            count[bl] -= 1
            if count[bl] == 0:
                have -= 1
            left += 1
    # output result
    print(ans)

if __name__ == '__main__':
    main()
