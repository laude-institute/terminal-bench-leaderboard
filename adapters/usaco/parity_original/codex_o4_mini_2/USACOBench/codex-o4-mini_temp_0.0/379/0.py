#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    times = []
    dists = []
    idx = 1
    for _ in range(n):
        typ = data[idx]; val = int(data[idx+1]); idx += 2
        if typ == 'T':
            times.append(val)
        else:
            dists.append(val)
    # sort events
    times.sort()
    dists.sort()

    k = 1              # current slow-down count, speed = 1/k
    cur_t = 0          # current time
    cur_d = 0          # current distance
    ti = 0             # time-event index
    di = 0             # dist-event index
    INF = 10**18

    # process events until reaching 1000m
    while cur_d < 1000:
        next_t = times[ti] if ti < len(times) else INF
        next_d = dists[di] if di < len(dists) else 1000
        # time to reach next time event
        dt_time = next_t - cur_t
        # time to reach next dist event
        dist_rem = next_d - cur_d
        dt_dist = dist_rem * k
        # which comes first
        if dt_time < dt_dist:
            # time event first
            cur_t = next_t
            k += 1
            ti += 1
        elif dt_time > dt_dist:
            # distance event first
            cur_t += dt_dist
            cur_d = next_d
            k += 1
            di += 1
        else:
            # simultaneous
            cur_t = next_t
            cur_d = next_d
            k += 1
            ti += 1
            di += 1
    # output rounded result
    # cur_t is integer
    print(int(cur_t))

if __name__ == '__main__':
    main()
