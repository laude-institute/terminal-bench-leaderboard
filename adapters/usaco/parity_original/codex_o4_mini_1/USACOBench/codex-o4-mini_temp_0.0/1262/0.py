#!/usr/bin/env python3
import sys

def min_swaps_to_palindrome(s):
    # greedy two-pointer adjacent swap count
    arr = list(s)
    i, j = 0, len(arr) - 1
    swaps = 0
    while i < j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            k = j
            # find matching for arr[i]
            while k > i and arr[k] != arr[i]:
                k -= 1
            if k == i:
                # no match, swap toward center
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
            else:
                # bring arr[k] to position j
                for m in range(k, j):
                    arr[m], arr[m+1] = arr[m+1], arr[m]
                    swaps += 1
                i += 1
                j -= 1
    return swaps

def main():
    S = sys.stdin.read().strip()
    n = len(S)
    # prefix sum of G counts
    prefix = [0] * (n + 1)
    for i, c in enumerate(S):
        prefix[i+1] = prefix[i] + (1 if c == 'G' else 0)
    total = 0
    for l in range(n):
        for r in range(l, n):
            L = r - l + 1
            g = prefix[r+1] - prefix[l]
            # impossible if even length and odd Gs
            if L % 2 == 0 and g % 2 == 1:
                total -= 1
            else:
                total += min_swaps_to_palindrome(S[l:r+1])
    print(total)

if __name__ == '__main__':
    main()
