# Pseudocode solution for counting good prefixes of gen_string(A, B)
# No outside libraries are used.

def count_good(a: int, b: int) -> int:
    # Base cases: if one is zero, no good prefixes
    if a == 0 or b == 0:
        return 0

    if b >= a:
        # Use Euclidean-style recursion when b >= a
        q = b // a
        r = b % a
        if r != 0:
            # We get q good prefixes from the blocks of ones
            return q + count_good(a, r)
        else:
            # When exact multiple, we count full runs
            # There are (q) runs of size a, with 2*a-1 good prefixes in the final block
            return q + 2 * a - 2
    else:
        # Mirror the logic when a > b
        q = a // b
        r = a % b
        if r != 0:
            return q + count_good(r, b)
        else:
            return q + 2 * b - 2


def main():
    import sys
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        A = int(data[idx]); B = int(data[idx+1])
        idx += 2
        print(count_good(A, B))

if __name__ == '__main__':
    main()
