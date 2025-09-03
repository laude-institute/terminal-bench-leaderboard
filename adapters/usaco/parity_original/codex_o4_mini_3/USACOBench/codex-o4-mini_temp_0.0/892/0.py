"""
1. Restate the problem in plain English:
   Farmer John has N cows standing in a line in some order. Only the cow at the front
   listens, and he can take that cow and insert her deeper in the line by k positions.
   The goal is to sort the cows into the increasing order 1..N using the fewest moves.

2. Conceptualize a solution in plain English:
   Observe that cows already forming a strictly increasing suffix at the end of the line
   never need to move, because we only move the front cow. Thus, only the prefix before
   this longest increasing suffix requires moves—one per cow in that prefix.

3. Pseudocode:
   Read N and list p of length N
   Initialize count k = 1  // length of increasing suffix
   For i from N-2 down to 0:
       If p[i] < p[i+1]:
           Increment k
       Else:
           Break the loop
   Answer = N - k
   Print Answer
"""

def main():
    import sys
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    p = list(map(int, data[1:1+N]))
    k = 1
    # Count length of strictly increasing suffix
    for i in range(N-2, -1, -1):
        if p[i] < p[i+1]:
            k += 1
        else:
            break
    # Minimum moves equals number of cows before that suffix
    print(N - k)

if __name__ == "__main__":
    main()
