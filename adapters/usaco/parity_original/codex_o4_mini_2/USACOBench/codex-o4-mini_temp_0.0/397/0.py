#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    W, N = map(int, data[:2])
    words = data[2:2+W]
    idx = 2 + W
    # Prepare sorted list of (word, original index)
    pairs = sorted([(w, i+1) for i, w in enumerate(words)], key=lambda x: x[0])
    sorted_words = [w for w, _ in pairs]
    out = []
    # Process each query
    for _ in range(N):
        K = int(data[idx])
        prefix = data[idx+1]
        idx += 2
        # Find range of words starting with prefix
        lo = bisect.bisect_left(sorted_words, prefix)
        hi = bisect.bisect_left(sorted_words, prefix + '{')
        # Check if K-th completion exists
        if K <= hi - lo:
            # Append original index of the K-th completion
            out.append(str(pairs[lo + K - 1][1]))
        else:
            out.append(str(-1))
    # Output results
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
