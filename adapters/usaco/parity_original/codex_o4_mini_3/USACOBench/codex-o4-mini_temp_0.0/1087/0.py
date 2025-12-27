#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N, Q = map(int, data[:2])
    s = data[2].strip()
    # Prefix strokes
    f = [0] * (N + 1)
    stack = []
    strokes = 0
    for i in range(1, N + 1):
        c = s[i-1]
        # Pop darker colors
        while stack and stack[-1] > c:
            stack.pop()
        # If same color on top, no new stroke
        if not stack or stack[-1] != c:
            stack.append(c)
            strokes += 1
        f[i] = strokes

    # Suffix strokes
    g = [0] * (N + 2)
    stack = []
    strokes = 0
    for i in range(N, 0, -1):
        c = s[i-1]
        while stack and stack[-1] > c:
            stack.pop()
        if not stack or stack[-1] != c:
            stack.append(c)
            strokes += 1
        g[i] = strokes

    out = []
    idx = 3
    for _ in range(Q):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        left = f[a-1]
        right = g[b+1] if b < N else 0
        out.append(str(left + right))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
