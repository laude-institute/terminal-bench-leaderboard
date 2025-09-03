from fractions import Fraction
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    time_events = []
    dist_events = []
    for _ in range(N):
        typ, x = input().split()
        x = int(x)
        if typ == 'T':
            time_events.append(x)
        else:
            dist_events.append(x)
    time_events.sort()
    dist_events.sort()
    current_time = Fraction(0, 1)
    current_distance = Fraction(0, 1)
    slow_count = 0
    speed = Fraction(1, slow_count + 1)
    time_idx = 0
    dist_idx = 0
    len_time = len(time_events)
    len_dist = len(dist_events)
    INF = Fraction(10**18, 1)
    # Process events in order of occurrence
    while time_idx < len_time or dist_idx < len_dist:
        if time_idx < len_time:
            t_event = Fraction(time_events[time_idx], 1)
            dt_time = t_event - current_time
        else:
            dt_time = INF
        if dist_idx < len_dist:
            d_event = Fraction(dist_events[dist_idx], 1)
            dt_dist = (d_event - current_distance) / speed
        else:
            dt_dist = INF
        if dt_time < dt_dist:
            # next slowdown by time
            current_time = t_event
            current_distance += speed * dt_time
            slow_count += 1
            speed = Fraction(1, slow_count + 1)
            time_idx += 1
        elif dt_dist < dt_time:
            # next slowdown by distance
            current_time += dt_dist
            current_distance = d_event
            slow_count += 1
            speed = Fraction(1, slow_count + 1)
            dist_idx += 1
        else:
            # simultaneous events
            current_time = t_event
            current_distance = d_event
            slow_count += 2
            speed = Fraction(1, slow_count + 1)
            time_idx += 1
            dist_idx += 1
    # Finish remaining distance
    remaining = Fraction(1000, 1) - current_distance
    current_time += remaining / speed
    # Round to nearest integer (0.5 rounds up)
    result = int(current_time + Fraction(1, 2))
    print(result)

if __name__ == '__main__':
    main()
