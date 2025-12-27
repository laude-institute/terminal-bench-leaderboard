#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    N = int(data.readline())
    # read directions and right boundary costs
    sign = [None] * (N+2)
    cost = [[0] * (N+2) for _ in range(N+2)]
    sign[0] = None
    for i in range(1, N+1):
        parts = data.readline().split()
        dirs = parts[0].strip()
        sign[i] = [''] + list(dirs) + ['']
        cost[i][N+1] = int(parts[1])
    # last line: bottom boundary costs
    last = list(map(int, data.readline().split()))
    for j in range(1, N+1):
        cost[N+1][j] = last[j-1]
    # compute cnt: number of cows reaching each cell
    cnt = [[0] * (N+2) for _ in range(N+2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            cnt[i][j] = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            c = cnt[i][j]
            if sign[i][j] == 'R':
                cnt[i][j+1] += c
            else:
                cnt[i+1][j] += c
    # initial total cost
    total = 0
    for i in range(1, N+1):
        total += cnt[i][N+1] * cost[i][N+1]
    for j in range(1, N+1):
        total += cnt[N+1][j] * cost[N+1][j]
    out = [str(total)]
    # function to get exit cost from a starting cell
    def exit_cost(i, j):
        # follow signs until boundary
        while i <= N and j <= N:
            if sign[i][j] == 'R':
                j += 1
            else:
                i += 1
        return cost[i][j]

    Q = int(data.readline())
    for _ in range(Q):
        line = data.readline().split()
        x, y = int(line[0]), int(line[1])
        w = cnt[x][y]
        # compute old cost
        if sign[x][y] == 'R':
            old = exit_cost(x, y+1)
            new = exit_cost(x+1, y)
            sign[x][y] = 'D'
        else:
            old = exit_cost(x+1, y)
            new = exit_cost(x, y+1)
            sign[x][y] = 'R'
        total += w * (new - old)
        out.append(str(total))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
