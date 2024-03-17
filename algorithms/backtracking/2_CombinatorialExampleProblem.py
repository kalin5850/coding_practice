"""
Given a non-negative integer n, find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

Input: 2
Output: ["aa", "ab", "ba", "bb"]

Input: 4
Output: ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"]
"""

from typing import List


def letter_combination(n: int) -> List[str]:
    result = []

    def dfs(start_idx: int, path: List[str]):
        if start_idx == n:
            return result.append("".join(path))

        for ch in ["a", "b"]:
            path.append(ch)
            dfs(start_idx + 1, path)
            path.pop()

        return result

    dfs(0, [])

    return result


if __name__ == "__main__":
    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)
