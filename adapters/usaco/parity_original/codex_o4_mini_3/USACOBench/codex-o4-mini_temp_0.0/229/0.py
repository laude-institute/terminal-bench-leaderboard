#!/usr/bin/env python3
"""
Problem: Cow Lineup
Find the largest contiguous block of same-breed cows after removing up to K other breeds.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    b = [int(next(it)) for _ in range(n)]

    # Frequency of each breed
    freq = {}
    for x in b:
        freq[x] = freq.get(x, 0) + 1

    # Sort breeds by descending frequency
    breeds = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    ans = 0
    # For each candidate breed, sliding window
    for x in breeds:
        # No better than current best
        if freq[x] <= ans:
            break
        count_x = 0
        l = 0
        removed = {}  # counts of non-x breeds in window
        distinct = 0
        # two pointers
        for r in range(n):
            if b[r] == x:
                count_x += 1
            else:
                cnt = removed.get(b[r], 0)
                if cnt == 0:
                    distinct += 1
                removed[b[r]] = cnt + 1
            # shrink window if too many distinct
            while distinct > k:
                if b[l] == x:
                    count_x -= 1
                else:
                    cnt = removed[b[l]] - 1
                    if cnt == 0:
                        distinct -= 1
                        del removed[b[l]]
                    else:
                        removed[b[l]] = cnt
                l += 1
            # update ans
            if count_x > ans:
                ans = count_x
        # small optimization: if ans equals total freq, can't do better
        if ans == freq[x]:
            break

    # Output result
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
