#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    spot = [input().strip() for _ in range(N)]
    plain = [input().strip() for _ in range(N)]
    count = 0
    # Iterate over all triplets of positions
    for i in range(M):
        for j in range(i + 1, M):
            for k in range(j + 1, M):
                seen = set()
                # Record spotty triples
                for s in spot:
                    seen.add((s[i], s[j], s[k]))
                # Check plain triples for intersection
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
