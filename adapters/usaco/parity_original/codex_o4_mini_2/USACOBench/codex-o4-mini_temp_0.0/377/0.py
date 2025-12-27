#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    time_events = []
    dist_events = []
    for _ in range(n):
        typ = next(it)
        x = int(next(it))
        if typ == 'T':
            time_events.append(x)
        else:
            dist_events.append(x)
    time_events.sort()
    dist_events.sort()
    i = j = 0
    slows = 0
    cur_t = 0.0
    cur_d = 0.0
    INF = float('inf')
    EPS = 1e-9
    # speed = 1 / (slows + 1)
    while cur_d < 1000 - EPS:
        next_t = time_events[i] if i < len(time_events) else INF
        next_d = dist_events[j] if j < len(dist_events) else INF
        speed_factor = slows + 1
        # time to finish
        dt_finish = (1000 - cur_d) * speed_factor
        # time to next events
        dt_time = next_t - cur_t
        dt_dist = (next_d - cur_d) * speed_factor
        # finish before next event
        if dt_finish < min(dt_time, dt_dist) - EPS:
            cur_t += dt_finish
            cur_d = 1000.0
            break
        # determine event order
        if dt_time < dt_dist - EPS:
            # time event first
            cur_t = next_t
            cur_d += (dt_time) / speed_factor
            # handle all time events at this time
            while i < len(time_events) and abs(time_events[i] - next_t) < EPS:
                slows += 1
                i += 1
        elif dt_dist < dt_time - EPS:
            # distance event first
            cur_d = next_d
            cur_t += dt_dist
            # handle all dist events at this distance
            while j < len(dist_events) and abs(dist_events[j] - next_d) < EPS:
                slows += 1
                j += 1
        else:
            # simultaneous
            cur_t = next_t
            cur_d = next_d
            # handle both
            # time events
            while i < len(time_events) and abs(time_events[i] - next_t) < EPS:
                slows += 1
                i += 1
            # dist events
            while j < len(dist_events) and abs(dist_events[j] - next_d) < EPS:
                slows += 1
                j += 1
    # round to nearest integer
    result = int(cur_t + 0.5)
    print(result)

if __name__ == '__main__':
    main()
