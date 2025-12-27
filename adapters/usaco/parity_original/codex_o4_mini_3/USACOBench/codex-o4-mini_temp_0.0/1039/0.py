#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    fav = [0] * (N + 1)
    sec = [0] * (N + 1)
    for i in range(1, N + 1):
        f, s = map(int, input().split())
        fav[i] = f
        sec[i] = s

    taken = [0] * (M + 1)  # which cow holds each cereal
    nxt = [0] * (N + 1)    # next choice index for each cow (0:first, 1:second)
    ans = [0] * (N + 2)
    count = 0

    # Process cows in reverse
    for i in range(N, 0, -1):
        cur = i
        # try to assign this cow, possibly displacing others
        while nxt[cur] < 2:
            choice = fav[cur] if nxt[cur] == 0 else sec[cur]
            if taken[choice] == 0:
                taken[choice] = cur
                count += 1
                break
            elif taken[choice] < cur:
                # current owner has priority
                break
            else:
                # displace the current owner
                prev = taken[choice]
                taken[choice] = cur
                nxt[prev] += 1
                cur = prev
        ans[i] = count

    # Output results for removing first i-1 cows: i from 1 to N
    out = sys.stdout
    for i in range(1, N + 1):
        out.write(str(ans[i]) + '\n')

if __name__ == '__main__':
    main()
