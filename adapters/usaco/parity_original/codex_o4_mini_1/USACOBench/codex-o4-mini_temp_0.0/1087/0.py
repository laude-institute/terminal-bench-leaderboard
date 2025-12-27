#!/usr/bin/env python3
import sys

def compute_strokes(s: str) -> list:
    """
    Compute prefix strokes for string s (1-indexed).
    Returns a list strokes where strokes[i] is the strokes for s[:i].
    """
    n = len(s)
    strokes = [0] * (n + 1)
    stack = []
    cnt = 0
    for i, c in enumerate(s, 1):
        # pop darker colors
        while stack and stack[-1] > c:
            stack.pop()
        # if new color, push and count stroke
        if not stack or stack[-1] < c:
            stack.append(c)
            cnt += 1
        strokes[i] = cnt
    return strokes

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    s = next(it).strip()
    # prefix strokes on original string
    pref = compute_strokes(s)
    # prefix strokes on reversed string
    pref_r = compute_strokes(s[::-1])
    # build suffix strokes: suff[i] = strokes for s[i-1:]
    # using pref_r: substring s[i-1:] corresponds to reversed prefix of length n-i+1
    suff = [0] * (n + 2)
    for i in range(1, n + 1):
        # reversed index = n - (i-1)
        suff[i] = pref_r[n - i + 1]
    suff[n+1] = 0

    out = []
    for _ in range(q):
        a = int(next(it))
        b = int(next(it))
        # strokes for [1..a-1] + [b+1..n]
        res = pref[a-1] + (suff[b+1] if b+1 <= n else 0)
        out.append(str(res))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
