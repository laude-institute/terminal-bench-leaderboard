import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        S = sum(a)
        if S == 0:
            out.append("0")
            continue
        M = max(a)
        # find divisors of S
        import math
        divs = []
        r = int(math.isqrt(S))
        for i in range(1, r + 1):
            if S % i == 0:
                divs.append(i)
                j = S // i
                if j != i:
                    divs.append(j)
        divs.sort()
        ans = n - 1  # worst case combining all into one
        for t in divs:
            if t < M:
                continue
            curr = 0
            ok = True
            for x in a:
                curr += x
                if curr == t:
                    curr = 0
                elif curr > t:
                    ok = False
                    break
            if ok and curr == 0:
                k = S // t
                ans = n - k
                break
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
