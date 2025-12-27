#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        N = int(next(it))
        a = [int(next(it)) for _ in range(N)]
        S = sum(a)
        # If total is zero, all entries are zero already
        if S == 0:
            out.append("0")
            continue
        # Collect divisors of S (possible numbers of segments)
        divs = []
        i = 1
        while i * i <= S:
            if S % i == 0:
                divs.append(i)
                if i != S // i:
                    divs.append(S // i)
            i += 1
        # Try largest k (segments) first to minimize merges
        divs.sort(reverse=True)
        ans = N - 1
        for k in divs:
            if k > N:
                continue
            target = S // k
            cur = 0
            cnt = 0
            ok = True
            for v in a:
                cur += v
                if cur == target:
                    cnt += 1
                    cur = 0
                elif cur > target:
                    ok = False
                    break
            if ok and cnt == k:
                ans = N - k
                break
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
