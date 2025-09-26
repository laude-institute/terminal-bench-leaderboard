"""
Solution to USACO Proximity Problem:
Two cows of the same breed are "crowded" if their positions differ by at most K.
We track the last seen index of each breed and update the answer whenever a repeat occurs within K.
Time complexity: O(N), space complexity: O(N).
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    breeds = list(map(int, data[2:]))
    last = {}
    ans = -1
    for i, b in enumerate(breeds):
        if b in last and i - last[b] <= K:
            ans = b if b > ans else ans
        last[b] = i
    print(ans)

if __name__ == "__main__":
    main()
