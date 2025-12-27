#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    events = []
    pos = 0
    idx = 2
    for _ in range(N):
        d = int(data[idx]); direction = data[idx+1]; idx += 2
        if direction == 'R':
            new_pos = pos + d
        else:
            new_pos = pos - d
        start = min(pos, new_pos)
        end = max(pos, new_pos)
        events.append((start, 1))
        events.append((end, -1))
        pos = new_pos
    # Sort events by position
    events.sort(key=lambda x: x[0])
    ans = 0
    cov = 0
    prev_x = events[0][0]
    for x, delta in events:
        if x > prev_x:
            if cov >= K:
                ans += x - prev_x
            prev_x = x
        cov += delta
    print(ans)

if __name__ == '__main__':
    main()
