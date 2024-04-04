from typing import List


# bottom to top
def minimum_total(triangle: List[List[int]]) -> int:
    dp = [[float("inf") for _ in range(len(triangle))] for _ in range(len(triangle))]

    # base
    for col in range(len(triangle)):
        dp[len(triangle) - 1][col] = triangle[len(triangle) - 1][col]

    for r in range(len(triangle) - 2, -1, -1):
        for c in range(0, r + 1):
            dp[r][c] = min(dp[r + 1][c], dp[r + 1][c + 1]) + triangle[r][c]

    return dp[0][0]


# top to bottom
def minimum_total(triangle: List[List[int]]) -> int:
    dp = [[float("inf") for _ in range(len(triangle))] for _ in range(len(triangle))]

    # base
    dp[0][0] = triangle[0][0]

    for r in range(1, len(triangle)):
        for c in range(0, r + 1):
            if c - 1 < 0:
                dp[r][c] = dp[r - 1][c] + triangle[r][c]
            else:
                dp[r][c] = min(dp[r - 1][c], dp[r - 1][c - 1]) + triangle[r][c]

    return min(dp[len(triangle) - 1])


# Brute force
def minimum_total(triangle: List[List[int]]) -> int:
    result = []

    def dfs(node, total):
        row, col = node
        if row >= len(triangle) or col >= len(triangle):
            return result.append(total)

        # left: row + 1, right: row + 1 and col + 1
        dfs((row + 1, col), total + triangle[row][col])
        dfs((row + 1, col + 1), total + triangle[row][col])

        return

    dfs((0, 0), 0)

    return min(result)


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    res = minimum_total(triangle)
    print(res)
    triangle = [
        [10],
        [4, 4],
        [6, 6, 5],
        [7, 7, 8, 3],
        [8, 9, 7, 2, 1],
        [8, 6, 9, 5, 2, 0],
    ]

    res = minimum_total(triangle)
    print(res)
    triangle = [[2], [8, 6], [1, 5, 7]]
    res = minimum_total(triangle)
    print(res)
    triangle = [
        [9],
        [2, 1],
        [3, 4, 1],
        [6, 5, 7, 7],
        [2, 4, 5, 8, 8],
        [3, 4, 1, 2, 3, 3],
        [6, 5, 7, 2, 4, 1, 6],
        [2, 5, 8, 6, 2, 3, 4, 7],
        [3, 4, 8, 2, 1, 8, 9, 2, 1],
        [6, 5, 7, 8, 3, 7, 9, 9, 9, 9],
    ]
    res = minimum_total(triangle)
    print(res)
