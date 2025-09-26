import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    try:
        n = int(next(it))
        k = int(next(it))
    except StopIteration:
        return
    patches = []
    for _ in range(n):
        g = int(next(it))
        x = int(next(it))
        patches.append((x, g))
    patches.sort()
    best = 0
    curr = 0
    left = 0
    # sliding window over [x, x + 2*k]
    for right in range(n):
        curr += patches[right][1]
        # shrink window if out of range
        while patches[right][0] - patches[left][0] > 2 * k:
            curr -= patches[left][1]
            left += 1
        if curr > best:
            best = curr
    print(best)

if __name__ == '__main__':
    main()
