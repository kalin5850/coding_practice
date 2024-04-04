from typing import List


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
