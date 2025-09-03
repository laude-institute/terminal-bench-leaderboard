#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    L = int(next(it))
    # Read knot positions and convert to doubled scale
    positions2 = []
    for _ in range(n):
        p = int(next(it))
        positions2.append(p * 2)
    L2 = L * 2
    pos_set = set(positions2)
    count = 0
    # Try every possible fold position f2 = 2*f, excluding endpoints
    for f2 in range(1, L2):
        # Determine which side is shorter
        if f2 <= L2 - f2:
            # Left side shorter or equal: check knots on [0, f]
            valid = True
            for p2 in positions2:
                if p2 <= f2:
                    t2 = f2 - p2
                    if (f2 + t2) not in pos_set:
                        valid = False
                        break
        else:
            # Right side shorter: check knots on [f, L]
            valid = True
            for p2 in positions2:
                if p2 >= f2:
                    t2 = p2 - f2
                    if (f2 - t2) not in pos_set:
                        valid = False
                        break
        if valid:
            count += 1
    # Print number of valid folds
    print(count)

if __name__ == '__main__':
    main()
