#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    A = [int(next(it)) for _ in range(n)]

    # Perform one full forward and backward pass
    B = A[:]
    # Forward bubble
    for i in range(n-1):
        if B[i+1] < B[i]:
            B[i], B[i+1] = B[i+1], B[i]
    # Backward bubble
    for i in range(n-2, -1, -1):
        if B[i+1] < B[i]:
            B[i], B[i+1] = B[i+1], B[i]

    # Check if fully sorted
    for i in range(n-1):
        if B[i+1] < B[i]:
            print(2)
            return
    print(1)

if __name__ == '__main__':
    main()
