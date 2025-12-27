#!/usr/bin/env python3
import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    cows = []
    for _ in range(N):
        x,y = map(int, input().split())
        cows.append((x,y))
    # sort by x and assign x-index
    cows_x = sorted(cows, key=lambda p: p[0])
    # sort by y and assign y-rank
    cows_y = sorted(cows, key=lambda p: p[1])
    y_rank = {p:i for i,p in enumerate(cows_y)}
    # build p[x_index] = y_rank
    p = [0]*N
    for i,(x,y) in enumerate(cows_x):
        p[i] = y_rank[(x,y)]
    # build reverse map y->x_index
    y_to_x = [0]*N
    for i in range(N):
        y_to_x[p[i]] = i
    # precompute minx[a][b] and maxx[a][b] for y-ranges
    INF = N+1
    minx = [[INF]*N for _ in range(N)]
    maxx = [[-1]*N for _ in range(N)]
    for a in range(N):
        cur_min = INF
        cur_max = -1
        for b in range(a, N):
            xidx = y_to_x[b]
            if xidx < cur_min: cur_min = xidx
            if xidx > cur_max: cur_max = xidx
            minx[a][b] = cur_min
            maxx[a][b] = cur_max
    # count subsets
    total = 1  # empty subset
    # for each x-interval
    for l in range(N):
        # gather and sort y-ranks in this interval
        Ys = sorted(p[l:r+1] for r in range(l, l+1))  # placeholder
        # inefficient simple loop: brute subarray over all y
        for r in range(l, N):
            # extract y-ranks in cows_x[l:r+1]
            segment = [p[i] for i in range(l, r+1)]
            segment.sort()
            k = len(segment)
            for i in range(k):
                for j in range(i, k):
                    a = segment[i]
                    b = segment[j]
                    # check no cow outside x-range has y in [a,b]
                    if minx[a][b] >= l and maxx[a][b] <= r:
                        total += 1
    print(total)

if __name__ == '__main__':
    main()
