#!/usr/bin/env python3
import sys

def rotate(stamp):
    """Rotate stamp 90 degrees clockwise"""
    K = len(stamp)
    return [''.join(stamp[K-1-r][c] for r in range(K)) for c in range(K)]

def can_paint(target, stamp):
    N = len(target)
    K = len(stamp)
    # coverage of painted cells
    covered = [[False]*N for _ in range(N)]
    # for each rotation
    cur = stamp
    for _ in range(4):
        # try all positions
        for i in range(N-K+1):
            for j in range(N-K+1):
                ok = True
                for x in range(K):
                    for y in range(K):
                        if cur[x][y] == '*' and target[i+x][j+y] != '*':
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    # apply stamp
                    for x in range(K):
                        for y in range(K):
                            if cur[x][y] == '*':
                                covered[i+x][j+y] = True
        # rotate for next
        cur = rotate(cur)
    # verify all target '*' are covered
    for i in range(len(target)):
        for j in range(len(target)):
            if target[i][j] == '*' and not covered[i][j]:
                return False
    return True

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        N = int(next(it))
        target = [next(it).strip() for _ in range(N)]
        K = int(next(it))
        stamp = [next(it).strip() for _ in range(K)]
        res = can_paint(target, stamp)
        out.append('YES' if res else 'NO')
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
