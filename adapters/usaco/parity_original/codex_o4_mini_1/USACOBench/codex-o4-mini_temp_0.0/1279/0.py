#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    N = int(data.readline())
    # directions: 0=R,1=D
    dir = [[0]*(N+2) for _ in range(N+2)]
    # sink costs, including vats
    sink = [[0]*(N+2) for _ in range(N+2)]
    # dp counts
    dp = [[0]*(N+2) for _ in range(N+2)]
    # read grid rows
    for i in range(1, N+1):
        parts = data.readline().split()
        s = parts[0]
        # directions
        for j, ch in enumerate(s, start=1):
            dir[i][j] = 0 if ch == 'R' else 1
        # vat at (i,N+1)
        sink[i][N+1] = int(parts[1])
    # last row vats
    parts = data.readline().split()
    for j in range(1, N+1):
        sink[N+1][j] = int(parts[j-1])
    # compute sink costs for internal cells
    for i in range(N, 0, -1):
        di = sink[i]
        di1 = sink[i+1]
        for j in range(N, 0, -1):
            if dir[i][j] == 0:
                di[j] = di[j+1]
            else:
                di[j] = di1[j]
    # compute dp counts
    total = 0
    for i in range(1, N+1):
        dpi = dp[i]
        dpi1 = dp[i-1] if i>1 else None
        for j in range(1, N+1):
            # start with own cow
            v = 1
            # from up
            if i > 1 and dir[i-1][j] == 1:
                v += dp[i-1][j]
            # from left
            if j > 1 and dir[i][j-1] == 0:
                v += dpi[j-1]
            dpi[j] = v
            total += sink[i][j]
    # sum initial cost
    # instead, sum sink for each cow
    # print initial
    out = sys.stdout
    out.write(str(total) + '\n')
    # process queries
    Q = int(data.readline())
    for _ in range(Q):
        line = data.readline().split()
        i = int(line[0]); j = int(line[1])
        # subtree size
        s = dp[i][j]
        # old next
        if dir[i][j] == 0:
            oi, oj = i, j+1
        else:
            oi, oj = i+1, j
        # find old sink
        ti, tj = oi, oj
        while ti <= N and tj <= N:
            if dir[ti][tj] == 0:
                tj += 1
            else:
                ti += 1
        old_cost = sink[ti][tj]
        # new direction and next
        dir[i][j] ^= 1
        if dir[i][j] == 0:
            ni, nj = i, j+1
        else:
            ni, nj = i+1, j
        # find new sink
        ti, tj = ni, nj
        while ti <= N and tj <= N:
            if dir[ti][tj] == 0:
                tj += 1
            else:
                ti += 1
        new_cost = sink[ti][tj]
        # update total cost
        total += s * (new_cost - old_cost)
        out.write(str(total) + '\n')
        # update dp along old path (decrement)
        xi, xj = oi, oj
        rem = s
        while xi <= N and xj <= N:
            dp[xi][xj] -= rem
            if dir[xi][xj] == 0:
                xj += 1
            else:
                xi += 1
        # update dp along new path (increment)
        xi, xj = ni, nj
        while xi <= N and xj <= N:
            dp[xi][xj] += rem
            if dir[xi][xj] == 0:
                xj += 1
            else:
                xi += 1

if __name__ == '__main__':
    main()
