#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    t_list = []
    d_list = []
    idx = 1
    for _ in range(n):
        typ = data[idx]; idx += 1
        x = int(data[idx]); idx += 1
        if typ == 'T':
            t_list.append(float(x))
        else:
            d_list.append(float(x))
    t_list.sort()
    d_list.sort()
    i_t, i_d = 0, 0
    len_t, len_d = len(t_list), len(d_list)
    cur_t, cur_x, c = 0.0, 0.0, 0
    INF = float('inf')
    eps = 1e-9
    # Process events
    while i_t < len_t or i_d < len_d:
        speed = 1.0 / (c + 1)
        t_e = t_list[i_t] if i_t < len_t else INF
        d_e = d_list[i_d] if i_d < len_d else INF
        dt = t_e - cur_t
        dd = d_e - cur_x
        time_for_d = dd / speed if d_e < INF else INF
        # Determine which event happens first
        if dt < time_for_d - eps:
            # Time event first
            cur_x += speed * dt
            cur_t = t_e
            # apply all simultaneous time events
            while i_t < len_t and abs(t_list[i_t] - t_e) < eps:
                i_t += 1
                c += 1
        elif dt > time_for_d + eps:
            # Distance event first
            cur_t += time_for_d
            cur_x = d_e
            # apply all simultaneous distance events
            while i_d < len_d and abs(d_list[i_d] - d_e) < eps:
                i_d += 1
                c += 1
        else:
            # Simultaneous time and distance
            cur_x += speed * dt
            cur_t = t_e
            while i_t < len_t and abs(t_list[i_t] - t_e) < eps:
                i_t += 1
                c += 1
            while i_d < len_d and abs(d_list[i_d] - d_e) < eps:
                i_d += 1
                c += 1
    # Finish remaining distance to 1000m
    if cur_x < 1000 - eps:
        speed = 1.0 / (c + 1)
        cur_t += (1000 - cur_x) / speed
    # Round to nearest second (0.5 rounds up)
    result = int(cur_t + 0.5)
    print(result)

if __name__ == '__main__':
    main()
