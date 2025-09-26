#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    cows = []
    idx = 1
    for _ in range(N):
        x = int(data[idx]); b = data[idx+1]; idx += 2
        cows.append((x, b))
    # Sort cows by position
    cows.sort(key=lambda cb: cb[0])
    xs = [c[0] for c in cows]
    bs = [c[1] for c in cows]
    ans = 0
    # Single-breed runs
    start = 0
    for i in range(1, N+1):
        if i == N or bs[i] != bs[start]:
            ans = max(ans, xs[i-1] - xs[start])
            start = i
    # Equal G/H counts via prefix diff
    diff = 0
    earliest = {0: 0}
    for i in range(1, N+1):
        diff += 1 if bs[i-1] == 'G' else -1
        if diff in earliest:
            j = earliest[diff]
            ans = max(ans, xs[i-1] - xs[j])
        else:
            earliest[diff] = i
    print(ans)

if __name__ == '__main__':
    main()
