#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n
        total = sum(a)
        # If total is zero, all entries are zero already
        if total == 0:
            results.append('0')
            continue
        # Find all divisors of total
        divisors = []
        i = 1
        while i * i <= total:
            if total % i == 0:
                divisors.append(i)
                if i != total // i:
                    divisors.append(total // i)
            i += 1
        divisors.sort()
        # Try smallest segment sum first (max segments)
        best_mods = n  # initialize with worst-case
        for seg_sum in divisors:
            target_segments = total // seg_sum
            curr = 0
            count = 0
            ok = True
            for v in a:
                curr += v
                if curr == seg_sum:
                    count += 1
                    curr = 0
                elif curr > seg_sum:
                    ok = False
                    break
            if ok and curr == 0 and count == target_segments:
                # modifications = original segments - final segments
                best_mods = n - target_segments
                break
        results.append(str(best_mods))
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    main()
