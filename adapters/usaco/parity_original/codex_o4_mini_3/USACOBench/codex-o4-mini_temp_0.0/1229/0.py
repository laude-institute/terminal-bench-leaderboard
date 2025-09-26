#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    a = [0] + [int(next(it)) for _ in range(N)]
    K = int(next(it))
    recipes = {}
    for _ in range(K):
        L = int(next(it))
        M = int(next(it))
        ingredients = [int(next(it)) for _ in range(M)]
        recipes[L] = ingredients

    def can_make(x):
        demand = [0] * (N + 1)
        demand[N] = x
        # Propagate demands from N down to 1
        for metal in range(N, 0, -1):
            if demand[metal] <= a[metal]:
                continue
            need = demand[metal] - a[metal]
            if metal not in recipes:
                return False
            # Increase demand for each ingredient
            for ing in recipes[metal]:
                demand[ing] += need
        return True

    # Binary search max units of metal N
    low, high = 0, sum(a)
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if can_make(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)

if __name__ == "__main__":
    main()
