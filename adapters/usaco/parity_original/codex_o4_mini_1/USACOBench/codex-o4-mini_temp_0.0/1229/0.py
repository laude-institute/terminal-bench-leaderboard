import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    # initial quantities of metals 1..N
    a = [0] * (N + 1)
    for i in range(1, N + 1):
        a[i] = int(next(it))
    K = int(next(it))
    # recipes: for metal L, list of required metals
    recipe = {}
    for _ in range(K):
        L = int(next(it))
        M = int(next(it))
        cs = [int(next(it)) for _ in range(M)]
        recipe[L] = cs
    # process in increasing metal order
    for L in range(1, N + 1):
        if L in recipe:
            cs = recipe[L]
            # max times we can apply this recipe
            t = min(a[c] for c in cs)
            if t > 0:
                for c in cs:
                    a[c] -= t
                a[L] += t
    # output maximum units of metal N
    print(a[N])


if __name__ == '__main__':
    main()
