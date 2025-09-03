#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    L = int(next(it))
    cows = []  # list of (w, x, d)
    total_weight = 0
    for _ in range(N):
        w = int(next(it)); x = int(next(it)); d = int(next(it))
        cows.append((w, x, d))
        total_weight += w
    # Compute times to barns
    times = []  # list of (time_to_barn, weight)
    for w, x, d in cows:
        if d == -1:
            t = x
        else:
            t = L - x
        times.append((t, w))
    times.sort(key=lambda p: p[0])
    # Find T when accumulated stopped weight >= half total
    half = (total_weight + 1) // 2
    acc = 0
    T = 0
    for t, w in times:
        acc += w
        if acc >= half:
            T = t
            break
    # Collect positions of right-moving and left-moving cows
    R = []  # positions of d=1
    Ls = []  # positions of d=-1
    for w, x, d in cows:
        if d == 1:
            R.append(x)
        else:
            Ls.append(x)
    R.sort()
    # Count meetings: for each left-moving cow at xj, count R positions xi with xi < xj and xj - xi <= 2*T
    import bisect
    meetings = 0
    twoT = 2 * T
    for xj in Ls:
        # xi in [xj - twoT, xj)
        lo = xj - twoT
        left = bisect.bisect_left(R, lo)
        right = bisect.bisect_left(R, xj)
        meetings += max(0, right - left)
    # Output result
    print(meetings)

if __name__ == '__main__':
    main()
