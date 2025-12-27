#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    # Read input
    n = int(input().strip())
    a = input().strip()
    b = input().strip()
    # Count contiguous mismatch segments
    ans = 0
    in_mismatch = False
    for i in range(n):
        if a[i] != b[i]:
            if not in_mismatch:
                ans += 1
                in_mismatch = True
        else:
            in_mismatch = False
    # Output result
    print(ans)

if __name__ == "__main__":
    main()
