#!/usr/bin/env python3
import sys

def valid(prefix, K):
    # Check if first K plates can be washed into sorted clean stack
    A = prefix[:K]
    # sorted target order for this prefix
    S = sorted(A)
    need_idx = 0
    # soapy stacks: each is list, and tops parallel
    stacks = []
    tops = []
    import bisect
    for a in A:
        # rinse as much as possible before soaping next
        while stacks and need_idx < K and stacks[0][-1] == S[need_idx]:
            stacks[0].pop()
            need_idx += 1
            if not stacks[0]:
                stacks.pop(0)
                tops.pop(0)
            else:
                tops[0] = stacks[0][-1]
        # soap this plate: place in leftmost stack with top >= a
        i = bisect.bisect_left(tops, a)
        if i == len(stacks):
            stacks.append([a])
            tops.append(a)
        else:
            stacks[i].append(a)
            tops[i] = a
    # final rinse pass
    while stacks and need_idx < K and stacks[0][-1] == S[need_idx]:
        stacks[0].pop()
        need_idx += 1
        if not stacks[0]:
            stacks.pop(0)
            tops.pop(0)
        else:
            tops[0] = stacks[0][-1]
    return need_idx == K

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = [int(x) for x in data[1:]]
    # binary search largest K where valid
    lo, hi = 0, n+1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if valid(A, mid):
            lo = mid
        else:
            hi = mid
    print(lo)

if __name__ == '__main__':
    main()
