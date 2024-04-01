"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example 1:

Input: nums = [1,2,3]

Output:

1[
2  [3],
3  [1],
4  [2],
5  [1,2,3],
6  [1,3],
7  [2,3],
8  [1,2],
9  []
10]
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    result = []

    def dfs(idx: int, path: List[int]):
        if idx == len(nums):
            result.append(path[:])
            return

        path.append(nums[idx])
        dfs(idx + 1, path)
        path.pop()
        dfs(idx + 1, path)

    dfs(0, [])

    return result


if __name__ == "__main__":
    # nums = [int(x) for x in input().split()]
    nums = [1, 2, 3]
    res = subsets(nums)
    res = [" ".join(str(x) for x in sorted(subset)) for subset in res]
    res.sort()
    for row in res:
        print(row)
