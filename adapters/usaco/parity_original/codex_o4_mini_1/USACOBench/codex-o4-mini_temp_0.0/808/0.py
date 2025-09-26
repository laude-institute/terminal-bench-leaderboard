#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    xs = list(map(int, data[1:]))
    # pair positions with original indices
    cows = sorted([(xs[i], i) for i in range(N)])
    # determine pass target for each cow
    t = [0] * N
    for k in range(N):
        pos, idx = cows[k]
        if k == 0:
            neighbor = cows[1][1]
        elif k == N-1:
            neighbor = cows[N-2][1]
        else:
            left_pos, left_idx = cows[k-1]
            right_pos, right_idx = cows[k+1]
            if abs(pos - left_pos) <= abs(right_pos - pos):
                neighbor = left_idx
            else:
                neighbor = right_idx
        t[idx] = neighbor
    # compute indegrees
    indegree = [0] * N
    for i in range(N):
        indegree[t[i]] += 1
    # balls needed for cows with no incoming passes
    result = sum(1 for i in range(N) if indegree[i] == 0)
    # handle mutual pairs with no other incoming
    for i in range(N):
        j = t[i]
        if t[j] == i and i < j:
            # mutual pair i<->j
            if indegree[i] == 1 and indegree[j] == 1:
                result += 1
    print(result)

if __name__ == '__main__':
    main()
