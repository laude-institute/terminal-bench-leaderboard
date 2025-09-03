#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    counts = list(map(int, data[1:1+n]))
    prev = 0
    result = 0
    for x in counts:
        if x > prev:
            result += x - prev
        prev = x
    print(result)

if __name__ == "__main__":
    main()
