"""Solution to Mountain Climbing problem using Johnson's algorithm."""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    # Read up/down times
    pairs = [(int(data[i]), int(data[i+1])) for i in range(1, 2*N, 2)]
    # Partition cows for Johnson's rule
    group1 = []  # cows with up < down
    group2 = []  # cows with up >= down
    for u, d in pairs:
        if u < d:
            group1.append((u, d))
        else:
            group2.append((u, d))
    # Sort group1 by increasing up times, group2 by decreasing down times
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: -x[1])
    # Combine sequence
    sequence = group1 + group2
    # Simulate the two-stage process
    t1 = 0  # time when Farmer John finishes guiding up
    t2 = 0  # time when Farmer Don finishes guiding down
    for u, d in sequence:
        t1 += u
        # Farmer Don can start only after both conditions
        t2 = max(t2, t1) + d
    # The makespan is when all cows are down
    print(t2)

if __name__ == "__main__":
    main()
