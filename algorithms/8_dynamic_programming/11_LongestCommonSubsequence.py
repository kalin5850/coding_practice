from typing import Dict


def longest_common_subsequence(word1: str, word2: str) -> int:

    def dynamic_programming():
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                if word1[r] == word2[c]:
                    dp[r + 1][c + 1] = 1 + dp[r][c]
                else:
                    dp[r + 1][c + 1] = max(dp[r][c + 1], dp[r + 1][c])

        return dp[-1][-1]

    def dfs_cached(idx1: int, idx2: int, length: int, cached: Dict[int, int]) -> int:
        if (idx1, idx2) in cached:
            return cached[(idx1, idx2)]
        if idx1 >= len(word1) or idx2 >= len(word2):
            return 0
        if word1[idx1] == word2[idx2]:
            length = dfs_cached(idx1 + 1, idx2 + 1, length, cached) + 1
        else:
            length = max(
                dfs_cached(idx1 + 1, idx2, length, cached),
                dfs_cached(idx1, idx2 + 1, length, cached),
            )
        cached[(idx1, idx2)] = length
        return length

    def dfs(idx1: int, idx2: int, length: int) -> int:
        if idx1 >= len(word1) or idx2 >= len(word2):
            return 0
        if word1[idx1] == word2[idx2]:
            length = dfs(idx1 + 1, idx2 + 1, length) + 1
        else:
            length = max(dfs(idx1 + 1, idx2, length), dfs(idx1, idx2 + 1, length))
        return length

    print(dfs(0, 0, 0))
    print(dfs_cached(0, 0, 0, {}))
    print(dynamic_programming())
    return 0


if __name__ == "__main__":
    word1 = "abcde"
    word2 = "ace"
    res = longest_common_subsequence(word1, word2)
    print(res)
    word1 = "almost"
    word2 = "algomonster"
    res = longest_common_subsequence(word1, word2)
    print(res)
    word1 = "abcd"
    word2 = "hjkl"
    res = longest_common_subsequence(word1, word2)
    print(res)
    word1 = "inspire"
    word2 = "aspire"
    res = longest_common_subsequence(word1, word2)
    print(res)
