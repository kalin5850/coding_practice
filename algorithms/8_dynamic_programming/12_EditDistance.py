"""
There are two words, word1 and word2. You have to find the minimum number of operations required to convert word1 to word2.

You are allowed to use the following 3 operations on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input:

word1 = "almost"
word2 = "algomonster"
Output:5

Explanation:

almost    ->  algmost    (insert 'g')
algmost   ->  algomost   (insert 'o')
algomost  ->  algmonst   (insert 'n')
algomonst ->  algomoste  (insert 'e')
algomoste ->  algomoster (insert 'r')
Example 2:

Input:

word1 = "intention"
word2 = "execution"
Output:5

Explanation:

intention  ->  inention   (remove 't')
inention   ->  enention   (replace 'i' with 'e')
enention   ->  exention   (replace 'n' with 'x')
exention   ->  exection   (replace 'n' with 'c')
exection   ->  execution  (insert 'u')
"""


def min_distance(word1: str, word2: str) -> int:
    row, col = len(word1), len(word2)
    dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

    for r in range(row):
        dp[r][col] = row - r
    for c in range(col):
        dp[row][c] = col - c

    for r in range(row - 1, -1, -1):
        for c in range(col - 1, -1, -1):
            #             print("dp[%s][%s]=%s" % (r, c, dp[r + 1][c + 1]))
            if word1[r] == word2[c]:
                dp[r][c] = dp[r + 1][c + 1]
            else:
                dp[r][c] = 1 + min(dp[r][c + 1], dp[r + 1][c], dp[r + 1][c + 1])

    return dp[0][0]


if __name__ == "__main__":
    word1 = "almost"
    word2 = "algomonster"
    res = min_distance(word1, word2)
    print(res)
    word1 = "intention"
    word2 = "execution"
    res = min_distance(word1, word2)
    print(res)
    word1 = "brainstorming"
    word2 = "imagination"
    res = min_distance(word1, word2)
    print(res)
    word1 = "dj"
    word2 = "abcdef"
    res = min_distance(word1, word2)
    print(res)
