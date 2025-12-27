#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    B, E = map(int, data[:2])
    idx = 2
    dirs1 = []
    for _ in range(B):
        dist = int(data[idx])
        d = data[idx+1]
        idx += 2
        dirs1.extend(d for _ in range(dist))
    dirs2 = []
    for _ in range(E):
        dist = int(data[idx])
        d = data[idx+1]
        idx += 2
        dirs2.extend(d for _ in range(dist))
    max_time = max(len(dirs1), len(dirs2))
    pos1 = pos2 = 0
    prev_meet = True
    moos = 0
    for t in range(max_time):
        if t < len(dirs1):
            pos1 += 1 if dirs1[t] == 'R' else -1
        if t < len(dirs2):
            pos2 += 1 if dirs2[t] == 'R' else -1
        curr_meet = (pos1 == pos2)
        if curr_meet and not prev_meet:
            moos += 1
        prev_meet = curr_meet
    print(moos)

if __name__ == "__main__":
    main()
