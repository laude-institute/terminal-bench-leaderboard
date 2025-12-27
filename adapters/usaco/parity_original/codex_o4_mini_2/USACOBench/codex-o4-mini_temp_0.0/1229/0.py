"""
Solution to the metal transformations problem.
Reads metal counts and recipes, computes maximum units of metal N.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    counts = [0] + list(map(int, input().split()))
    K = int(input())
    recipes = {}
    for _ in range(K):
        parts = list(map(int, input().split()))
        L, M = parts[0], parts[1]
        ingredients = parts[2:]
        recipes[L] = ingredients

    # Find metals that can contribute to metal N
    reachable = set([N])
    stack = [N]
    while stack:
        m = stack.pop()
        if m in recipes:
            for s in recipes[m]:
                if s not in reachable:
                    reachable.add(s)
                    stack.append(s)

    # Process metals in increasing order
    for i in range(1, N+1):
        if i in recipes and i in reachable:
            ingr = recipes[i]
            # Max times we can apply recipe
            times = min(counts[s] for s in ingr)
            if times > 0:
                for s in ingr:
                    counts[s] -= times
                counts[i] += times

    print(counts[N])

if __name__ == "__main__":
    main()
