#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = data[1].strip()
    B = data[2].strip()
    count = 0
    in_segment = False
    for i in range(n):
        if A[i] != B[i]:
            if not in_segment:
                count += 1
                in_segment = True
        else:
            in_segment = False
    print(count)

if __name__ == "__main__":
    main()
