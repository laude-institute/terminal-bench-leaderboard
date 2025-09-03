#!/usr/bin/env python3
"""
Solution to trap Bessie by adding minimum hay to one bale.

Approach:
1. Read N, B and list of bales (size, pos).
2. Sort bales by position.
3. Use two pointers l, r bracketing B.
4. While pointers valid:
   - Compute required run distance D = pos[r] - pos[l].
   - If both sizes >= D: trapped (ans=0), break.
   - Else if one side size < D and the other >= D: candidate add = D - size[weak].
   - Move pointer at weaker bale inward (expand gap where break happens).
5. Track minimal addition; if none, print -1, else print it.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    B = int(next(it))
    bales = []  # (pos, size)
    for _ in range(N):
        s = int(next(it))
        p = int(next(it))
        bales.append((p, s))
    bales.sort()
    pos = [p for p, _ in bales]
    size = [s for _, s in bales]
    # Find initial bracket around B
    import bisect
    r = bisect.bisect_left(pos, B)
    l = r - 1
    # If B not between any two bales, immediate escape
    if l < 0 or r >= N:
        print(-1)
        return

    ans = None
    # Expand pointers
    while l >= 0 and r < N:
        D = pos[r] - pos[l]
        sl = size[l]
        sr = size[r]
        # Check if both sides can hold
        if sl >= D and sr >= D:
            ans = 0
            break
        # One side holds, other weak -> candidate
        if sl >= D and sr < D:
            need = D - sr
            ans = need if ans is None else min(ans, need)
        elif sr >= D and sl < D:
            need = D - sl
            ans = need if ans is None else min(ans, need)
        # Move the weaker bale pointer inward
        # If equal, move either; choose left
        if sl < sr:
            l -= 1
        else:
            r += 1
    # Output result
    print(ans if ans is not None else -1)

if __name__ == '__main__':
    main()
