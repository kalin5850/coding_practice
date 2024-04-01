"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Examples

Example 1:

Input: aab

Output:

[
  ["aa","b"],
  ["a","a","b"]
]
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    result = []

    def is_palidrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1

        return True

    def dfs(start_idx, path):
        if start_idx >= len(s):
            result.append(path[:])
            return

        for edge in range(start_idx, len(s)):
            if not is_palidrome(s, start_idx, edge):
                continue
            path.append(s[start_idx : edge + 1])
            dfs(start_idx + len(s[start_idx : edge + 1]), path)
            path.pop()

        return

    dfs(0, [])
    return result


if __name__ == "__main__":
    # s = input()
    s = "aab"
    res = partition(s)
    for row in res:
        print(" ".join(row))
