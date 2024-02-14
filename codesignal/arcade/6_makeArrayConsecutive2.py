"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
"""

import heapq


def solution(statues):
    """
    brute force: O(nlog n)
    BCR: O(n)
    """

    if len(statues) == 1:
        return 0

    min_heap = []
    max_heap = []
    for num in statues:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, -(num))

    small_number = heapq.heappop(min_heap)
    max_number = abs(heapq.heappop(max_heap))

    return max_number - small_number + 1 - len(statues)
