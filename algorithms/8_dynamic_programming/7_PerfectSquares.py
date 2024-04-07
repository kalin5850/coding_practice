import math
from typing import List


def list_perfect_squares(n: int) -> int:
    val = math.sqrt(n)
    values = [i for i in range(1, int(val) + 1)]
    result = []

    def dfs(idx: int, path: List[int], remaining: int):
        if remaining == 0:
            result.append(path[:])
            return

        if values[idx] > remaining or idx < 0 or remaining < 0:
            return

        for i in range(len(values) - 1, -1, -1):
            path.append(values[i])
            dfs(i - 1, path, remaining - values[i] ** 2)
            path.pop()

    dfs(len(values) - 1, [], n)
    print(result)
    return 0


def perfect_squares(n: int) -> int:
    val = math.sqrt(n)
    values = [i for i in range(1, int(val) + 1)]

    def dfs(cached, remain) -> int:
        if remain in cached:
            return cached[remain]
        if remain < 0:
            return float("inf")
        if remain == 0:
            return 0

        min_val = float("inf")
        for val in values:
            min_val = min(min_val, dfs(cached, remain - val**2) + 1)
        cached[remain] = min_val

        return min_val

    res = dfs({}, n)
    print(res)
    return 0


if __name__ == "__main__":
    # n = 12
    # res = list_perfect_squares(n)
    # print(res)
    n = 13
    res = perfect_squares(n)
    print(res)
    # n = 10000
    # res = perfect_squares(n)
    # print(res)
    # n = 5360
    # res = perfect_squares(n)
    # print(res)
    # n = 2167
    # res = perfect_squares(n)
    # print(res)
    # n = 9997
    # res = perfect_squares(n)
    # print(res)
    # n = 50
    # res = list_perfect_squares(n)
    # print(res)
