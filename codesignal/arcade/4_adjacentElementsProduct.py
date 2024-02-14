"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
"""

import heapq


def solution(inputArray):
    result_production = []
    for idx_i in range(len(inputArray) - 1):
        idx_j = idx_i + 1
        product = inputArray[idx_i] * inputArray[idx_j]
        heapq.heappush(result_production, -product)

    return -heapq.heappop(result_production)
