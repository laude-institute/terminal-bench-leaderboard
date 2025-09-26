#!/usr/bin/env python3
"""
Determine if a third 4-sided die C can be constructed to form a non-transitive set
with given dice A and B. Non-transitive means each die beats one and loses to one.
"""
import sys
import itertools

def beats(X, Y):
    """
    Return True if die X beats die Y: the number of (x>y) outcomes exceeds (x<y).
    """
    wins = sum(1 for x in X for y in Y if x > y)
    losses = sum(1 for x in X for y in Y if x < y)
    return wins > losses

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        A = list(map(int, data[idx:idx+4])); idx += 4
        B = list(map(int, data[idx:idx+4])); idx += 4
        # Determine initial ordering between A and B
        A_beats_B = beats(A, B)
        B_beats_A = beats(B, A)
        if not (A_beats_B or B_beats_A):
            print("no")
            continue
        # Define target relations for C
        if A_beats_B:
            # A > B > C > A cycle
            predicate = lambda C: beats(B, C) and beats(C, A)
        else:
            # B > A > C > B cycle
            predicate = lambda C: beats(A, C) and beats(C, B)

        found = False
        # Brute-force all possible C faces (1..10)
        for C in itertools.product(range(1, 11), repeat=4):
            if predicate(C):
                found = True
                break
        print("yes" if found else "no")

if __name__ == '__main__':
    main()
