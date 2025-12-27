"""
Problem 1: Bessie Slows Down

1. Restatement:
   Bessie starts skiing at 1 m/s but slows down each time she hits certain times or distances.
   After k slowdowns, her speed becomes 1/(k+1) m/s. Given events when she slows (by time or distance),
   compute how many seconds to finish 1000 meters, rounding to nearest integer.

2. Solution Concept:
   - Parse events into two sorted lists: time events and distance events.
   - Simulate race with state (current time, distance, slowdown count).
   - At each step, compute next time when a time event occurs and when the next distance event occurs,
     compare which comes first, advance state to that event, and increase slowdown count.
   - If finish (1000m) occurs before the next event, compute remaining time at current speed.
   - Sum total time and round to nearest integer (0.5 rounds up).

3. Pseudocode:
   read N
   for each event:
       if type is 'T': add to time_list
       else: add to dist_list
   sort time_list; sort dist_list
   time = 0.0; dist = 0.0; slows = 0
   i = j = 0
   while True:
       speed = 1.0 / (slows + 1)
       next_time_event = time_list[i] or INF
       next_dist = dist_list[j] or INF
       time_to_next_dist = (next_dist - dist) / speed
       time_to_finish = (1000 - dist) / speed
       if time_to_finish <= min(next_time_event - time, time_to_next_dist):
           time += time_to_finish; break
       if next_time_event - time < time_to_next_dist:
           dist += speed * (next_time_event - time)
           time = next_time_event; slows += 1; i += 1
       elif next_time_event - time > time_to_next_dist:
           time += time_to_next_dist; dist = next_dist; slows += 1; j += 1
       else:  # simultaneous
           time = next_time_event; dist = next_dist; slows += 2; i += 1; j += 1
   answer = int(time + 0.5)
   print(answer)
"""

import sys
import math

def main():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    times = []
    dists = []
    idx = 1
    for _ in range(N):
        typ = data[idx]; x = int(data[idx+1]); idx += 2
        if typ == 'T':
            times.append(x)
        else:
            dists.append(x)
    times.sort()
    dists.sort()

    curr_t = 0.0
    curr_d = 0.0
    slows = 0
    i = j = 0
    INF = float('inf')
    # simulate
    while True:
        speed = 1.0 / (slows + 1)
        next_time = times[i] if i < len(times) else INF
        next_dist = dists[j] if j < len(dists) else INF
        # time until next distance event
        t_to_dist = (next_dist - curr_d) / speed if next_dist < INF else INF
        # time until finish
        t_to_finish = (1000.0 - curr_d) / speed
        # time until next time event
        t_to_time = next_time - curr_t

        # finish before any event
        if t_to_finish <= min(t_to_time, t_to_dist):
            curr_t += t_to_finish
            break

        # time event first
        if t_to_time < t_to_dist:
            # advance to time event
            curr_d += speed * t_to_time
            curr_t = next_time
            slows += 1
            i += 1
        # distance event first
        elif t_to_time > t_to_dist:
            curr_t += t_to_dist
            curr_d = next_dist
            slows += 1
            j += 1
        else:
            # simultaneous event
            curr_t = next_time
            curr_d = next_dist
            slows += 2
            i += 1
            j += 1

    # output rounded time
    result = int(curr_t + 0.5)
    print(result)

if __name__ == '__main__':
    main()
