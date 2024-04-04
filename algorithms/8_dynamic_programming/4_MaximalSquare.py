from typing import List


# dynamic programming
def maximal_square(matrix: List[List[int]]) -> int:
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    max_value = -1
    # base
    for r in range(len(matrix)):
        dp[r][len(matrix[0]) - 1] = matrix[r][len(matrix[0]) - 1]
    for c in range(len(matrix[0])):
        dp[len(matrix) - 1][c] = matrix[len(matrix) - 1][c]

    for r in range(len(matrix) - 2, -1, -1):
        for c in range(len(matrix[0]) - 2, -1, -1):
            right = dp[r][c + 1]
            down = dp[r + 1][c]
            diag = dp[r + 1][c + 1]
            dp[r][c] = matrix[r][c] + min(right, down, diag)
            max_value = max(max_value, dp[r][c])

    return max_value**2


#  dfs + cached
def maximal_square(matrix: List[List[int]]) -> int:
    cached = {}

    def dfs(node):
        row, col = node
        if node in cached:
            return cached[node]

        if row >= len(matrix) or col >= len(matrix[0]):
            return 0

        # dfs to right
        right = dfs((row + 1, col))
        # dfs to down
        down = dfs((row, col + 1))
        # dfs to diag
        diag = dfs((row + 1, col + 1))

        if matrix[row][col] == 1:
            cached[node] = 1 + min(right, down, diag)
        else:
            cached[node] = 0

        return cached[node]

    dfs((0, 0))
    max(cached.values()) ** 2
    return max(cached.values()) ** 2


if __name__ == "__main__":
    matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 0, 0, 0, 1]]
    res = maximal_square(matrix)
    print(res)
    matrix = [[1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]
    res = maximal_square(matrix)
    print(res)
    matrix = [[1, 0, 0], [1, 0, 1], [0, 1, 1]]
    res = maximal_square(matrix)
    print(res)
    matrix = [[1, 1, 0], [0, 0, 0], [1, 0, 0]]
    res = maximal_square(matrix)
    print(res)
    matrix = [
        [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0],
    ]
    res = maximal_square(matrix)
    print(res)
    matrix = [
        [1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 1],
    ]
    res = maximal_square(matrix)
    print(res)
