from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if r - 1 < 0 and c - 1 < 0:
                dp[0][0] = grid[0][0]
            elif r - 1 < 0:
                dp[r][c] = dp[r][c - 1] + grid[r][c]
            elif c - 1 < 0:
                dp[r][c] = dp[r - 1][c] + grid[r][c]
            else:
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

    return dp[-1][-1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = min_path_sum(grid)
    print(res)
    grid = [[1, 3, 6], [1, 0, 6], [4, 2, 1]]
    res = min_path_sum(grid)
    print(res)
    grid = [[0, 0, 2], [1, 3, 0], [1, 0, 1]]
    res = min_path_sum(grid)
    print(res)
    grid = [
        [1, 0, 0, 0, 3, 0],
        [0, 0, 2, 0, 0, 0],
        [0, 2, 0, 3, 0, 0],
        [0, 0, 0, 0, 3, 0],
        [0, 0, 0, 4, 0, 0],
        [1, 1, 5, 0, 0, 0],
    ]

    res = min_path_sum(grid)
    print(res)
    grid = [
        [1, 0, 0, 0, 3, 0],
        [0, 0, 2, 0, 1, 0],
        [0, 2, 0, 3, 0, 0],
        [0, 0, 0, 0, 3, 0],
        [0, 0, 0, 4, 0, 0],
        [1, 1, 5, 0, 0, 1],
    ]
    res = min_path_sum(grid)
    print(res)
