#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    t = [int(next(it)) for _ in range(n)]
    # Sort ancestors by years ago descending
    t.sort(reverse=True)
    # Compute portal-aligned years
    u = [((x + 11) // 12) * 12 for x in t]  # arrival Ox year
    v = [(x // 12) * 12 for x in t]         # departure Ox year
    # Initial cost covering all in one segment
    initial = u[0] - (v[-1] if n > 0 else 0)
    # Compute benefits of splitting between j and j+1
    benefits = []
    for j in range(n-1):
        b = v[j] - u[j+1]
        if b > 0:
            benefits.append(b)
    # Take up to k-1 largest benefits
    benefits.sort(reverse=True)
    s = sum(benefits[:max(0, min(len(benefits), k-1))])
    result = initial - s
    print(result)

if __name__ == '__main__':
    main()
