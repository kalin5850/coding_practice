"""
Given an array (list) nums consisted of only non-negative integers, find the largest sum among all subarrays of length k in nums.

For example, if the input is nums = [1, 2, 3, 7, 4, 1], k = 3, then the output would be 14 as the largest length 3 subarray sum is given by [3, 7, 4] which sums to 14.
"""

from typing import List


def subarray_sum_fixed(nums: List[int], k: int) -> int:
    max_sum = 0
    for i in range(0, len(nums) - k):
        tmp = sum(nums[i : i + k])
        if tmp > max_sum:
            max_sum = tmp
    return max_sum


if __name__ == "__main__":
    # nums = [int(x) for x in input().split()]
    nums = [1, 2, 3, 7, 4, 1]
    k = int(input())
    res = subarray_sum_fixed(nums, k)
    print(res)
