#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    MOD = 10**9 + 7
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s.sort()
    t.sort()
    # Precompute for each cow the first barn index with size >= cow size
    l = [bisect_left(t, s[i]) for i in range(n)]
    result = 0
    # consider k matches, k from 0 to n
    for k in range(0, n+1):
        # check maximality condition: largest unmatched barn < smallest unmatched cow
        # unmatched barns are t[0..n-k-1], unmatched cows are s[k..n-1]
        if k == 0:
            # all cows unmatched, require t[n-1] < s[0]
            if n > 0 and t[n-1] >= s[0]:
                continue
        elif k < n:
            # require t[n-k-1] < s[k]
            if t[n-k-1] >= s[k]:
                continue
        # else k == n always ok
        # count matchings between s[0..k-1] and t[n-k..n-1]
        ways = 1
        # for each cow i (0-based) in matched set
        for i in range(k):
            # barns available for this cow: indices j in [n-k..n-1] with t[j] >= s[i]
            # first possible j is max(l[i], n-k)
            start = max(l[i], n-k)
            d = n - start
            # subtract already matched previous i cows
            choices = d - i
            if choices <= 0:
                ways = 0
                break
            ways = ways * choices % MOD
        result = (result + ways) % MOD
    print(result)

if __name__ == '__main__':
    main()
