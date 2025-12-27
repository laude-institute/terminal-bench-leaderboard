import heapq

def main():
    # Read number of cows
    n = int(input())
    # Read cows as (deadline, milk) pairs
    cows = []
    for _ in range(n):
        g, d = map(int, input().split())
        cows.append((d, g))
    # Sort cows by deadline
    cows.sort()
    # Min-heap to keep selected cows' milk amounts
    heap = []
    for d, g in cows:
        heapq.heappush(heap, g)
        # If too many cows by this deadline, discard lowest milk
        if len(heap) > d:
            heapq.heappop(heap)
    # Total milk is sum of selected cows
    print(sum(heap))

if __name__ == "__main__":
    main()
