#!/usr/bin/env python3
import sys

def rotate(stamp):
    # Rotate a square matrix 90 degrees clockwise
    K = len(stamp)
    return [[stamp[K-1-j][i] for j in range(K)] for i in range(K)]

def can_build(target, stamp):
    N = len(target)
    K = len(stamp)
    # coverage grid
    covered = [[False]*N for _ in range(N)]
    # Try each rotation
    for _ in range(4):
        # For each possible placement
        for i in range(N-K+1):
            for j in range(N-K+1):
                valid = True
                # check stamp fits inside target stars
                for di in range(K):
                    for dj in range(K):
                        if stamp[di][dj] == '*' and target[i+di][j+dj] != '*':
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    # mark coverage
                    for di in range(K):
                        for dj in range(K):
                            if stamp[di][dj] == '*':
                                covered[i+di][j+dj] = True
        # rotate stamp for next iteration
        stamp = rotate(stamp)
    # check all target stars are covered
    for i in range(len(target)):
        for j in range(len(target)):
            if target[i][j] == '*' and not covered[i][j]:
                return False
    return True

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        N = int(next(it))
        target = [list(next(it).strip()) for _ in range(N)]
        K = int(next(it))
        stamp = [list(next(it).strip()) for _ in range(K)]
        res = can_build(target, stamp)
        out.append("YES" if res else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
