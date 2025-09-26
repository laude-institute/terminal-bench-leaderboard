#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    cows = []
    for _ in range(N):
        x = int(next(it)); b = int(next(it))
        cows.append((x, b))
    cows.sort(key=lambda t: t[0])
    xs = [c[0] for c in cows]
    bs = [c[1] for c in cows]
    res = -1
    # iterate over subsets of breeds
    for mask in range(1, 1<<8):
        # skip subsets smaller than K
        if mask.bit_count() < K:
            continue
        # identify breeds in this subset
        breeds = [i+1 for i in range(8) if (mask >> i) & 1]
        b0 = breeds[0]
        other = breeds[1:]
        # scan runs without outside breeds
        i = 0
        while i < N:
            # skip blockers
            if not ((mask >> (bs[i]-1)) & 1):
                i += 1
                continue
            # start run
            start = i
            while i < N and ((mask >> (bs[i]-1)) & 1):
                i += 1
            end = i  # cows in [start, end)
            length = end - start
            if length >= len(breeds):
                # process this run
                # prefix counts
                pc = [0]*9
                # map key to earliest prefix idx
                init_key = tuple(0 for _ in other)
                seen = {init_key: 0}
                # positions in run
                run_x = xs[start:end]
                run_b = bs[start:end]
                for k in range(1, length+1):
                    b = run_b[k-1]
                    pc[b] += 1
                    base = pc[b0]
                    key = tuple(pc[bk] - base for bk in other)
                    if key in seen:
                        j = seen[key]
                        # segment from j to k-1
                        span = run_x[k-1] - run_x[j]
                        if span > res:
                            res = span
                    else:
                        seen[key] = k
            # continue after run
        # end while runs
    # output result
    sys.stdout.write(str(res))

if __name__ == '__main__':
    main()
