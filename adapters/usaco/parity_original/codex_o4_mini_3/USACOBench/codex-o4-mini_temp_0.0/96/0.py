#!/usr/bin/env python3
import sys
import itertools

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    weights = [int(next(it)) for _ in range(N)]
    # Precompute digits of each weight (least significant first)
    weights_digits = []
    for w in weights:
        digits = []
        while w > 0:
            digits.append(w % 10)
            w //= 10
        weights_digits.append(digits)
    # Try groups from largest to smallest
    for k in range(N, 0, -1):
        # combinations of indices of size k
        for combo in itertools.combinations(range(N), k):
            digits_sum = [0] * 10
            valid = True
            # Sum digits and check for carries
            for idx in combo:
                for pos, d in enumerate(weights_digits[idx]):
                    digits_sum[pos] += d
                    if digits_sum[pos] >= 10:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                print(k)
                return

if __name__ == "__main__":
    main()
