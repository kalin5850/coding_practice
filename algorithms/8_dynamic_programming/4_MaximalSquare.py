from typing import List


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
