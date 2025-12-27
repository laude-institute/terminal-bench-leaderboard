#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    jobs = []
    idx = 1
    for _ in range(n):
        u = int(data[idx]); d = int(data[idx+1])
        idx += 2
        jobs.append((u, d))

    # Johnson's rule: schedule U<=D first by increasing U, then U>D by decreasing D
    group1 = [job for job in jobs if job[0] <= job[1]]
    group2 = [job for job in jobs if job[0] > job[1]]
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    sequence = group1 + group2

    time_up = 0
    time_down = 0
    for u, d in sequence:
        time_up += u
        time_down = max(time_down, time_up) + d

    print(time_down)

if __name__ == "__main__":
    main()
