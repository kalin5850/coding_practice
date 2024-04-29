import math
from typing import List


def list_perfect_squares(n: int) -> int:
    nums = list(reversed([i for i in range(1, int(math.sqrt(n)) + 1)]))

    def list_all_paths(
        amount: int, path: List[int], res: List[List[int]]
    ) -> List[List[int]]:
        if amount == 0:
            res.append(path[:])
            return res
        for num in nums:
            remain = amount - pow(num, 2)
            if remain >= 0:
                path.append(num)
                list_all_paths(remain, path, res)
                path.pop()

        return res

    print(list_all_paths(n, [], []))


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


#  dp
def perfect_squares(n: int) -> int:
    dp = [n] * (n + 1)
    dp[0] = 0

    for target in range(1, n + 1):
        for s in range(1, target + 1):
            square = s**2
            if target - square < 0:
                break
            dp[target] = min(dp[target], dp[target - square] + 1)

    return dp[n]


if __name__ == "__main__":
    n = 12
    res = perfect_squares(n)
    print(res)
    n = 13
    res = perfect_squares(n)
    print(res)
    n = 10000
    res = perfect_squares(n)
    print(res)
    n = 5360
    res = perfect_squares(n)
    print(res)
    n = 2167
    res = perfect_squares(n)
    print(res)
    n = 9997
    res = perfect_squares(n)
    print(res)
    n = 43
    res = list_perfect_squares(n)
    print(res)
