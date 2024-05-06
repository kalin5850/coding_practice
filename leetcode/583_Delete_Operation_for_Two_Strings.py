"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
 

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


def min_distance(w1: str, w2: str) -> int:
    m, n = len(w1), len(w2)

    def dfs(idxi: int, idxj: int, total: int) -> int:
        if idxi >= m:
            return n - idxj
        if idxj >= n:
            return m - idxi
        if w1[idxi] == w2[idxj]:
            total = dfs(idxi + 1, idxj + 1, total)
        else:
            total = 1 + min(dfs(idxi + 1, idxj, total), dfs(idxi, idxj + 1, total))
        return total

    print(dfs(0, 0, 0))

    return ""


if __name__ == "__main__":
    word1 = "sea"
    word2 = "eat"
    res = min_distance(word1, word2)
    print(res)
    word1 = "leetcode"
    word2 = "etco"
    res = min_distance(word1, word2)
    print(res)
    word1 = "almost"
    word2 = "algomonster"
    res = min_distance(word1, word2)
    print(res)
    word1 = "intention"
    word2 = "execution"
    res = min_distance(word1, word2)
    print(res)
