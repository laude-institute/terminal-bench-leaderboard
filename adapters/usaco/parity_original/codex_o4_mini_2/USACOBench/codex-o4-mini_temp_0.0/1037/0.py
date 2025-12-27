#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    t = int(next(it))
    state_str = next(it).strip()
    final_state = [c == '1' for c in state_str]
    events = []
    for _ in range(t):
        tm = int(next(it))
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        events.append((tm, x, y))
    # sort by time
    events.sort(key=lambda e: e[0])

    valid_zero = 0
    ks_global = set()
    infinite = False

    # Try each cow as patient zero
    for i in range(n):
        ks = []
        # try K from 0 to t
        for K in range(t+1):
            infected = [False] * n
            infected[i] = True
            shakes = [0] * n
            # simulate
            for _, x, y in events:
                inf_x = infected[x]
                inf_y = infected[y]
                to_inf = []
                if inf_x:
                    shakes[x] += 1
                    if shakes[x] <= K and not infected[y]:
                        to_inf.append(y)
                if inf_y:
                    shakes[y] += 1
                    if shakes[y] <= K and not infected[x]:
                        to_inf.append(x)
                for j in to_inf:
                    infected[j] = True
            # check match
            ok = True
            for idx in range(n):
                if infected[idx] != final_state[idx]:
                    ok = False
                    break
            if ok:
                ks.append(K)
        if ks:
            valid_zero += 1
            ks_global.update(ks)
            if t in ks:
                infinite = True
    # determine y and z
    if ks_global:
        y = min(ks_global)
        if infinite:
            z = 'Infinity'
        else:
            z = max(ks_global)
    else:
        y = 0
        z = 0
    # output
    print(valid_zero, y, z)

if __name__ == '__main__':
    main()
