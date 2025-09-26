#!/usr/bin/env python3
"""
Count sets of three genome positions that distinguish spotty and plain cows.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    spot = data[2:2+N]
    plain = data[2+N:2+2*N]
    # Map nucleotides to integers
    code = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    # Convert genomes to numeric arrays
    s = [[code[ch] for ch in spot[i]] for i in range(N)]
    p = [[code[ch] for ch in plain[i]] for i in range(N)]
    ans = 0
    # Iterate over all triples of positions
    for i in range(M-2):
        for j in range(i+1, M-1):
            for k in range(j+1, M):
                seen = [False] * 64
                # Mark spotty cow signatures
                for x in range(N):
                    sig = (s[x][i] << 4) | (s[x][j] << 2) | s[x][k]
                    seen[sig] = True
                # Check plain cows for conflicts
                ok = True
                for x in range(N):
                    sig = (p[x][i] << 4) | (p[x][j] << 2) | p[x][k]
                    if seen[sig]:
                        ok = False
                        break
                if ok:
                    ans += 1
    # Output result
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
