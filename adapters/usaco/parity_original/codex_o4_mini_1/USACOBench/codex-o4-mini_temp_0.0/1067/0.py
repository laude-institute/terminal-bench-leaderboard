#!/usr/bin/env python3
"""
Count subsets of points separable by an axis-aligned square fence.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    cows = [tuple(map(int, input().split())) for _ in range(N)]
    # Sort by x-coordinate
    cows.sort(key=lambda p: p[0])
    xs = [p[0] for p in cows]
    ys = [p[1] for p in cows]
    # Pre-sort unique y-values for possible compression? But use real coords
    total = 0
    # For each x-interval [i,j]
    for i in range(N):
        ylist = []  # sorted y's in current x-range
        for j in range(i, N):
            # insert ys[j] into ylist
            y = ys[j]
            # binary insert
            lo, hi = 0, len(ylist)
            while lo < hi:
                mid = (lo + hi) // 2
                if ylist[mid] < y:
                    lo = mid + 1
                else:
                    hi = mid
            ylist.insert(lo, y)
            D = xs[j] - xs[i]
            K = len(ylist)
            # bottom placements
            r_b = [0] * K
            flag_b = [False] * K
            r = 0
            for l in range(K):
                if r < l:
                    r = l
                while r + 1 < K and ylist[r+1] - ylist[l] <= D:
                    r += 1
                r_b[l] = r
                # minimal bottom if no extra cow just above
                if r + 1 == K or ylist[r+1] - ylist[l] > D:
                    flag_b[l] = True
            # top placements
            l_t = [0] * K
            flag_t = [False] * K
            lptr = K - 1
            for rr in range(K-1, -1, -1):
                if lptr > rr:
                    lptr = rr
                while lptr - 1 >= 0 and ylist[rr] - ylist[lptr-1] <= D:
                    lptr -= 1
                l_t[rr] = lptr
                # minimal top if no extra cow just below
                if lptr == 0 or ylist[rr] - ylist[lptr-1] > D:
                    flag_t[rr] = True
            # count unique subsets for this interval
            cnt_b = sum(flag_b)
            cnt_t = sum(flag_t)
            overlap = 0
            for l in range(K):
                if flag_b[l]:
                    r = r_b[l]
                    if ylist[r] - ylist[l] == D and flag_t[r]:
                        overlap += 1
            total += cnt_b + cnt_t - overlap
    # add empty subset
    total += 1
    print(total)

if __name__ == '__main__':
    main()
