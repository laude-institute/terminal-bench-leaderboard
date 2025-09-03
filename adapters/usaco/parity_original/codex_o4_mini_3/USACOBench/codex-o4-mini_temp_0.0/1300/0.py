#!/usr/bin/env python3
import sys

def rotate(stamp):
    # Rotate a KxK stamp 90 degrees clockwise
    K = len(stamp)
    return [''.join(stamp[K-1-j][i] for j in range(K)) for i in range(K)]

def main():
    data = sys.stdin.read().strip().split()  # read all tokens
    it = iter(data)
    T = int(next(it))
    for _ in range(T):
        N = int(next(it))
        target = [list(next(it)) for _ in range(N)]
        K = int(next(it))
        stamp = [list(next(it)) for _ in range(K)]

        # Precompute all 4 rotations of the stamp
        stamps = []
        cur = [''.join(row) for row in stamp]
        for _ in range(4):
            stamps.append([list(row) for row in cur])
            cur = rotate(cur)

        # Coverage grid
        covered = [[False]*N for _ in range(N)]

        # Try stamping all valid positions for each rotation
        for s in stamps:
            for i in range(N - K + 1):
                for j in range(N - K + 1):
                    valid = True
                    for u in range(K):
                        for v in range(K):
                            if s[u][v] == '*' and target[i+u][j+v] == '.':
                                valid = False
                                break
                        if not valid:
                            break
                    if not valid:
                        continue
                    # Mark coverage
                    for u in range(K):
                        for v in range(K):
                            if s[u][v] == '*':
                                covered[i+u][j+v] = True

        # Check if all '*' in target are covered
        ok = True
        for i in range(N):
            for j in range(N):
                if target[i][j] == '*' and not covered[i][j]:
                    ok = False
                    break
            if not ok:
                break
        sys.stdout.write("YES\n" if ok else "NO\n")

if __name__ == '__main__':
    main()
