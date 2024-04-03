"""
A robot starts its journey at the top-left corner of a grid that measures m x n (m rows by n columns).

At each step, the robot has only two possible directions: it can either move to the right or move downward. Its destination is the bottom-right corner of the grid.

Determine the total number of unique paths the robot can take to reach its destination.

Example 1:

Input: m = 2, n = 3

Output: 3

Explanation:

From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

Right -> Right -> Down

Right -> Down -> Right

Down -> Right -> Right

Example 2:

Input: m = 5, n = 3

Output: 15
"""


#  dynamic programming
def unique_paths(m: int, n: int) -> int:
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # base
    for r in range(m):
        dp[r][0] = 1
    for c in range(n):
        dp[0][c] = 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[-1][-1]


#  dfs and cached
def unique_paths(m: int, n: int) -> int:

    def dfs(node, count, cached):
        row, col = node
        if (row, col) in cached:
            return cached[(row, col)]
        if row == m - 1 or col == n - 1:
            return 1

        count = dfs((row + 1, col), count, cached) + dfs((row, col + 1), count, cached)
        cached[(row, col)] = count

        return count


# dfs
def unique_paths(m: int, n: int) -> int:

    def dfs(node, count):
        row, col = node
        if row == m - 1 or col == n - 1:
            return 1

        count = dfs((row + 1, col), count) + dfs((row, col + 1), count)

        return count

    return dfs((0, 0), 0)


if __name__ == "__main__":
    m = 3
    n = 2
    res = unique_paths(m, n)
    print(res)
    m = 7
    n = 3
    res = unique_paths(m, n)
    print(res)
    m = 1
    n = 1
    res = unique_paths(m, n)
    print(res)
    m = 10
    n = 5
    res = unique_paths(m, n)
    print(res)
