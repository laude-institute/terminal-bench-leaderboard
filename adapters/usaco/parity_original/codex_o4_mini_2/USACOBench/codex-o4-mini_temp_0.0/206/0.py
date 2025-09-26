#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    LOs = []
    HIs = []
    for _ in range(n):
        s = next(it)
        lo = ''.join(sorted(s))
        hi = ''.join(sorted(s, reverse=True))
        LOs.append(lo)
        HIs.append(hi)
    sortedHIs = sorted(HIs)
    sortedLOs = sorted(LOs)
    output = []
    for lo, hi in zip(LOs, HIs):
        # minimal possible position
        min_rank = bisect.bisect_left(sortedHIs, lo) + 1
        # maximal possible position
        max_rank = bisect.bisect_right(sortedLOs, hi)
        output.append(f"{min_rank} {max_rank}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
