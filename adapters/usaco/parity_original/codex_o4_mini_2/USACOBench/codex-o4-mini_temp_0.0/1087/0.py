#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    s = next(it)
    # Compute prefix strokes for s[0..i-1]
    prefix = [0] * (n + 1)
    stack = []
    strokes = 0
    for i, c in enumerate(s):
        # Pop darker colors
        while stack and stack[-1] > c:
            stack.pop()
        # Push if new darker color
        if not stack or stack[-1] < c:
            stack.append(c)
            strokes += 1
        prefix[i + 1] = strokes

    # Compute prefix strokes on reversed for suffix calculation
    rev = s[::-1]
    rev_prefix = [0] * (n + 1)
    stack = []
    strokes = 0
    for i, c in enumerate(rev):
        while stack and stack[-1] > c:
            stack.pop()
        if not stack or stack[-1] < c:
            stack.append(c)
            strokes += 1
        rev_prefix[i + 1] = strokes

    out = []
    for _ in range(q):
        a = int(next(it))
        b = int(next(it))
        # strokes for left part 1..a-1
        left = prefix[a - 1]
        # strokes for right part b+1..n via reversed prefix
        # length of suffix = n - b, rev_prefix index = n - b
        right = rev_prefix[n - b]
        out.append(str(left + right))

    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
