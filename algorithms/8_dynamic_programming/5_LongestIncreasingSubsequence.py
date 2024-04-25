"""
Input

nums: the integer sequence
Output

the length of longest increasing subsequence

Examples

Example 1:

Input:

nums = [50, 3, 10, 7, 40, 80]
Output: 4

Explanation:

The longest increasing subsequence is [3, 7, 40, 80] which has length 4.

Example 2:

Input:

nums = [1, 2, 4, 3]
Output: 3

Explanation:

Both [1, 2, 4] and [1, 2, 3] are longest increasing subsequences which have length 3.
"""

from typing import List


def longest_sub_len(nums: List[int]) -> int:
    dp = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


if __name__ == "__main__":
    nums = [1, 100, 2, 7, 40, 80]  # should be 5 [1, 2, 7, 40, 80]
    res = longest_sub_len(nums)
    print(res)
    nums = [50, 3, 10, 7, 40, 80]
    res = longest_sub_len(nums)
    print(res)
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = longest_sub_len(nums)
    print(res)
    nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    res = longest_sub_len(nums)
    print(res)
    nums = [5, 46, 85, 26, 1, 5, 78, 45, 122, 56, 47, 26]
    res = longest_sub_len(nums)
    print(res)
    nums = [0, 0, 1, 6, 0, 0, 0]
    res = longest_sub_len(nums)
    print(res)
    nums = []
    res = longest_sub_len(nums)
    print(res)
