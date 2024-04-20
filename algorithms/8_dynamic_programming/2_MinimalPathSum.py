"""
Suppose we have a m by n matrix filled with non-negative integers, find a path from top left corner to bottom right corner which minimizes the sum of all numbers along its path.

Note: Movements can only be either down or right at any point in time.

Example:

Input:

  [
    [1,3,1],
    [1,5,1],
    [4,2,1]
  ]

Output:

7
"""

from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    def dfs(row, col, path: List[int], result: List[int]) -> List[int]:
        # trick: because need to get grid[m][n], col == n not col == n - 1
        if row == m - 1 and col == n:
            result.append(sum(path))
            return result
        if row == m or col == n:
            return result
        path.append(grid[row][col])
        dfs(row + 1, col, path, result)
        dfs(row, col + 1, path, result)
        path.pop()  # backtracking

        return min(result)

    return dfs(0, 0, [], [])


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
