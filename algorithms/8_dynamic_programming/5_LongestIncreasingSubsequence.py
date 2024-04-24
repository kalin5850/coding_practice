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

    def two_pointers(nums: List[int]) -> int:
        max_length = 0
        # result = []
        for curr, value in enumerate(nums):
            prev = curr
            tmp = [value]
            for check in range(curr, len(nums)):
                if nums[check] > nums[prev]:
                    prev = check
                    tmp.append(nums[check])
            # result.append(tmp[:])
            max_length = max(max_length, len(tmp))

        # print(result)
        return max_length

    longest_ln = 0
    if not nums:
        return longest_ln

    dp = [0 for _ in range(len(nums))]

    # bottom to top
    # base
    dp[len(nums) - 1] = [nums[len(nums) - 1]]

    for idx in range(len(nums) - 2, -1, -1):
        tmp = []
        current_value = nums[idx]
        tmp.append(current_value)
        for num in dp[idx + 1]:
            if num > current_value:
                tmp.append(num)

        dp[idx] = tmp
        longest_ln = max(longest_ln, len(tmp))

    return two_pointers(nums), longest_ln


if __name__ == "__main__":
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
