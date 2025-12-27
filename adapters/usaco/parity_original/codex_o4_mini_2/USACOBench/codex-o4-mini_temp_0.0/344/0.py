# Restate the problem in plain English:
# We have N cows on a number line, each at position x[i] with height h[i].
# A cow feels "crowded" if there is at least one cow of height >= 2*h[i]
# within distance D to its left AND at least one such cow within distance D to its right.
# We need to count the number of crowded cows.

# Conceptual solution in plain English:
# 1. Sort cows by their positions.
# 2. For each cow, find the maximum height among cows whose positions are
#    within D to the left; store as left_max[i].
# 3. Similarly, find the maximum height within D to the right; store as right_max[i].
# 4. A cow is crowded if left_max[i] >= 2*h[i] AND right_max[i] >= 2*h[i].
# 5. Count and output the number of such cows.

# Pseudocode:
# read N, D
# read list of (x, h) pairs
# sort pairs by x
# initialize left_max and right_max arrays of size N with 0
#
# # compute left_max:
# create empty deque
# for i from 0 to N-1:
#     while deque not empty and x[i] - x[deque.front] > D:
#         pop front of deque
#     left_max[i] = h[deque.front] if deque not empty else 0
#     while deque not empty and h[i] >= h[deque.back]:
#         pop back of deque
#     append i to back of deque
#
# # compute right_max similarly by iterating from N-1 down to 0
# create empty deque
# for i from N-1 down to 0:
#     while deque not empty and x[deque.front] - x[i] > D:
#         pop front of deque
#     right_max[i] = h[deque.front] if deque not empty else 0
#     while deque not empty and h[i] >= h[deque.back]:
#         pop back of deque
#     append i to back of deque
#
# # count crowded cows:
# count = 0
# for i from 0 to N-1:
#     if left_max[i] >= 2*h[i] and right_max[i] >= 2*h[i]:
#         count += 1
# print(count)
