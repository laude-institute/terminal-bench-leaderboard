#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    f = [0] * (N + 1)
    s = [0] * (N + 1)
    for i in range(1, N + 1):
        fi, si = map(int, input().split())
        f[i], s[i] = fi, si
    cereal = [0] * (M + 1)
    ans = [0] * (N + 2)
    # Process cows in reverse
    for i in range(N, 0, -1):
        ans[i] = ans[i + 1]
        cow = i
        choice = f[cow]
        # Try to claim cereals, potentially evicting later cows
        while True:
            if cereal[choice] == 0:
                cereal[choice] = cow
                ans[i] += 1
                break
            if cereal[choice] < cow:
                break
            evicted = cereal[choice]
            cereal[choice] = cow
            cow = evicted
            choice = s[cow]
    # Output results for each prefix removal
    out = sys.stdout.write
    for i in range(1, N + 1):
        out(str(ans[i]) + '\n')

if __name__ == '__main__':
    main()
