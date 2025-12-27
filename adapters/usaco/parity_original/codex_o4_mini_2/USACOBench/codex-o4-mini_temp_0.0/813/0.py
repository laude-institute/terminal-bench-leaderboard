#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, B = map(int, input().split())
    f = list(map(int, input().split()))
    boots = []
    for i in range(B):
        s, d = map(int, input().split())
        boots.append((s, d, i))

    # Sort tiles by snow depth descending
    tiles = [(f[i], i+1) for i in range(N)]
    tiles.sort(reverse=True)

    # Sort boots by max depth descending
    boots_sorted = sorted(boots, key=lambda x: x[0], reverse=True)

    # Doubly-linked list for tiles
    prev = [i-1 for i in range(N+2)]
    next = [i+1 for i in range(N+2)]
    max_gap = 1
    ans = [0] * B
    j = 0

    for s, d, idx in boots_sorted:
        # Remove tiles too deep for this boot
        while j < N and tiles[j][0] > s:
            pos = tiles[j][1]
            l = prev[pos]
            r = next[pos]
            next[l] = r
            prev[r] = l
            max_gap = max(max_gap, r - l)
            j += 1
        # Can we step across the largest gap?
        ans[idx] = 1 if max_gap <= d else 0

    # Output results in original order
    sys.stdout.write("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()
