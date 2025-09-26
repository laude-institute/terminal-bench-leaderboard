#!/usr/bin/env python3
"""
Solution for combination lock problem.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    combo1 = list(map(int, data[1:4]))
    combo2 = list(map(int, data[4:7]))
    # If N <= 5, every setting is within tolerance
    if N <= 5:
        print(N**3)
        return
    # Normalize dial position with wraparound
    def norm(x):
        return (x - 1) % N + 1
    settings = set()
    # Generate all settings within +/-2 of each combination
    for combo in (combo1, combo2):
        a, b, c = combo
        for da in range(-2, 3):
            for db in range(-2, 3):
                for dc in range(-2, 3):
                    settings.add((norm(a + da), norm(b + db), norm(c + dc)))
    # Output distinct count
    print(len(settings))

if __name__ == '__main__':
    main()
