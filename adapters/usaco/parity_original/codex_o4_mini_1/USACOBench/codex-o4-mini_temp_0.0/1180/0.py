#!/usr/bin/env python3
import sys
import itertools

def beats(X, Y):
    """Return True if die X beats die Y (more winning pairs than losing)."""
    wins = losses = 0
    for x in X:
        for y in Y:
            if x > y:
                wins += 1
            elif x < y:
                losses += 1
    return wins > losses

def main():
    data = list(map(int, sys.stdin.read().split()))
    T = data[0]
    idx = 1
    # Precompute all candidate dice C (multisets of 4 faces 1..10)
    candidates = list(itertools.combinations_with_replacement(range(1, 11), 4))
    results = []
    for _ in range(T):
        A = data[idx:idx+4]
        B = data[idx+4:idx+8]
        idx += 8
        # Determine relationship between A and B
        ab = beats(A, B)
        ba = beats(B, A)
        # If A and B tie, can't form non-transitive
        if ab == ba:
            results.append("no")
            continue
        found = False
        if ab:
            # A beats B, need B beats C and C beats A
            for C in candidates:
                if beats(B, C) and beats(C, A):
                    found = True
                    break
        else:
            # B beats A, need A beats C and C beats B
            for C in candidates:
                if beats(A, C) and beats(C, B):
                    found = True
                    break
        results.append("yes" if found else "no")
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
