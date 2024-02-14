"""
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be solution(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be solution(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be solution(a) = -1.
"""

import heapq


def solution(a):
    """
    Brute force: O(n ^ 2)
    Improve algorithm:
    Optimal algorithm:
    BCR: O(n)
    """
    # # Brute force
    # mean_idx = None
    # mean_value = None
    # for i in range(0, len(a)):
    #     for j in range(i + 1, len(a)):
    #         if a[i] == a[j] and (mean_idx == None or j < mean_idx):
    #             mean_idx = j
    #             mean_value = a[j]

    # print("idx %s, value %s" % (mean_idx, mean_value))

    # return mean_value if mean_idx is not None else -1

    adict = {}
    for i in a:
        if i in adict:
            return i
        else:
            adict[i] = 1

    return -1
