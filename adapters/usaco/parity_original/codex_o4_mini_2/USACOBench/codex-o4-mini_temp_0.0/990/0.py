import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    B = list(map(int, input().split()))
    maxB = max(B)
    best = 0
    half = K // 2
    for x in range(1, maxB + 1):
        full_count = sum(b // x for b in B)
        full_taken = min(full_count, K)
        if full_taken < half:
            continue
        remainders = [b % x for b in B]
        remainders.sort(reverse=True)
        if full_taken >= K:
            bessie = x * half
        else:
            need = K - full_taken
            top_rems = remainders[:need]
            basket = [x] * full_taken + top_rems + [0] * max(0, need - len(top_rems))
            basket.sort(reverse=True)
            bessie = sum(basket[half:K])
        if bessie > best:
            best = bessie
    print(best)

if __name__ == "__main__":
    main()
