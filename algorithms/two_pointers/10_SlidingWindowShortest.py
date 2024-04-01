"""
Let's continue on finding the sum of subarrays. This time given a positive integer array nums, we want to find the length of the shortest subarray such that the subarray sum is at least target. Recall the same example with input nums = [1, 4, 1, 7, 3, 0, 2, 5] and target = 10, then the smallest window with the sum >= 10 is [7, 3] with length 2. So the output is 2.

We'll assume for this problem that it's guaranteed target will not exceed the sum of all elements in nums.


"""

from typing import List


def subarray_sum_shortest(nums: List[int], target: int) -> int:
    slow, fast = 0, 0
    min_length = len(nums) + 1

    while fast < len(nums):
        if sum(nums[slow:fast]) < target:
            fast += 1
        elif sum(nums[slow:fast]) > target:
            slow += 1
        else:
            min_length = min(min_length, len(nums[slow:fast]))
            slow += 1
            fast += 1

    return min_lengt
