#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        if n == 1:
            # Single pile: losing when a % 4 == 0
            if a[0] % 4 == 0:
                out.append("Farmer Nhoj")
            else:
                out.append("Farmer John")
        else:
            # Count piles not divisible by 4
            cnt = sum(1 for x in a if x % 4 != 0)
            # If odd count, second player wins
            if cnt % 2 == 1:
                out.append("Farmer Nhoj")
            else:
                out.append("Farmer John")
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
