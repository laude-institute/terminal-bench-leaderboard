#!/usr/bin/env python3
import sys

def compare(d1, d2):
    """
    Compare two dice d1 and d2.
    Return 1 if d1 beats d2, -1 if d2 beats d1, 0 otherwise.
    """
    wins1 = wins2 = 0
    for x in d1:
        for y in d2:
            if x > y:
                wins1 += 1
            elif x < y:
                wins2 += 1
    if wins1 > wins2:
        return 1
    if wins2 > wins1:
        return -1
    return 0

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        A = [int(next(it)) for _ in range(4)]
        B = [int(next(it)) for _ in range(4)]
        cmp_ab = compare(A, B)
        # If neither A beats B nor B beats A, impossible
        if cmp_ab == 0:
            out.append("no")
            continue
        found = False
        # Determine required relation: if A beats B, need B > C > A
        # else B beats A, need A > C > B
        if cmp_ab > 0:
            # A beats B, so search C such that B beats C and C beats A
            for c1 in range(1, 11):
                for c2 in range(1, 11):
                    for c3 in range(1, 11):
                        for c4 in range(1, 11):
                            C = [c1, c2, c3, c4]
                            if compare(B, C) > 0 and compare(C, A) > 0:
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break
        else:
            # B beats A, so search C such that A beats C and C beats B
            for c1 in range(1, 11):
                for c2 in range(1, 11):
                    for c3 in range(1, 11):
                        for c4 in range(1, 11):
                            C = [c1, c2, c3, c4]
                            if compare(A, C) > 0 and compare(C, B) > 0:
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break
        out.append("yes" if found else "no")
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    solve()
