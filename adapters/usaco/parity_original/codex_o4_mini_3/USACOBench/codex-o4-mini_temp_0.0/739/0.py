#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    spot = [input().strip() for _ in range(N)]
    plain = [input().strip() for _ in range(N)]
    count = 0
    # Check all triples of positions
    for i in range(M - 2):
        for j in range(i + 1, M - 1):
            for k in range(j + 1, M):
                seen = set()
                # Record spotty signatures
                for s in spot:
                    seen.add((s[i], s[j], s[k]))
                # Ensure no plain cow matches any spotty signature
                valid = True
                for p in plain:
                    if (p[i], p[j], p[k]) in seen:
                        valid = False
                        break
                if valid:
                    count += 1
    print(count)

if __name__ == "__main__":
    main()
