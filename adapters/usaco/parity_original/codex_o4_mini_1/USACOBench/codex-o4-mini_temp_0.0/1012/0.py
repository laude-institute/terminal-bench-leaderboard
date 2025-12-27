#!/usr/bin/env python3
"""
Count minimum substring flips to transform B into A by toggling breeds.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = data[1].strip()
    b = data[2].strip()
    flips = 0
    in_segment = False
    for i in range(n):
        if a[i] != b[i]:
            if not in_segment:
                flips += 1
                in_segment = True
        else:
            in_segment = False
    print(flips)

if __name__ == '__main__':
    main()
