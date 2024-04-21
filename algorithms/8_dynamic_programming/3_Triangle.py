from typing import List, Dict


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


def minimum_total(triangle: List[List[int]]) -> int:
    m = len(triangle)

    # bottom-up recursion with cached
    def dfs_bottom_up_cached(
        row: int, col: int, total: int, cached: Dict[int, int]
    ) -> int:
        if (row, col) in cached:
            return cached[(row, col)]
        if row == m - 1:
            return triangle[row][col]

        total += min(
            dfs_bottom_up_cached(row + 1, col, total, cached) + triangle[row][col],
            dfs_bottom_up_cached(row + 1, col + 1, total, cached) + triangle[row][col],
        )
        cached[(row, col)] = total

        return total

    # top-bottom: list all path
    def dfs_top_bottom_all_path(
        row: int, col: int, path: List[int], result: List[int]
    ) -> List[int]:
        print("row: %s and col: %s" % (row, col))
        if row >= m or col > len(triangle[row - 1]):
            result.append(path[:])
            return result
        path.append(triangle[row][col])
        dfs_top_bottom_all_path(row + 1, col, path, result)
        dfs_top_bottom_all_path(row + 1, col + 1, path, result)
        path.pop()

        return result

    # top-bottom
    def dfs_top_bottom(row: int, col: int, total: int, result: List[int]) -> List[int]:
        if row >= m:
            result.append(total)
            return result
        dfs_top_bottom(row + 1, col, total + triangle[row][col], result)
        dfs_top_bottom(row + 1, col + 1, total + triangle[row][col], result)

        return result

    # bottom-up recursion
    def dfs_bottom_up(row: int, col: int, total: int) -> int:
        """
        If the function returns the local variable, that variable have to be in the arguement; otherwise, UnboundLocalError: cannot access local variable 'total' where it is not associated with a value.

            def dfs(row: int, col: int) -> int:
                if row == m - 1:
                    return triangle[row][col]

                total += min(
                    dfs(row + 1, col) + triangle[row][col],
                    dfs(row + 1, col + 1) + triangle[row][col],
                )

                return total
        """
        if row == m - 1:
            return triangle[row][col]

        total += min(
            dfs_bottom_up(row + 1, col, total) + triangle[row][col],
            dfs_bottom_up(row + 1, col + 1, total) + triangle[row][col],
        )

        return total

    return dfs_bottom_up(0, 0, 0), min(dfs_top_bottom(0, 0, 0, []))


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
