"""
You are given coins of different denominations and an amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11

Output: 3

Explanation:

11 = 5 + 5 + 1, 3 total coins

Example 2:

Input: coins = [3], amount = 1

Output: -1

"""

from typing import List


# brute force
def list_all_coin_change(coins: List[int], amount: int) -> int:
    all_changes = []

    def dfs(idx: int, path: List[int], remaining: int) -> int:
        if remaining == 0:
            all_changes.append(path[:])
            return

        if coins[idx] > amount or idx < 0 or remaining < 0:
            return

        for i in range(len(coins) - 1, -1, -1):
            path.append(coins[i])
            dfs(i - 1, path, remaining - coins[i])
            path.pop()

        return

    dfs(len(coins) - 1, [], amount)
    print(all_changes)


def coin_change(coins: List[int], amount: int) -> int:

    def backtracking(cached, remain):
        if remain in cached:
            return cached[remain]
        if remain == 0:
            return 0
        if remain < 0:
            return float("inf")

        min_coins = float("inf")
        for coin in coins:
            min_coins = min(min_coins, backtracking(cached, remain - coin) + 1)

        cached[remain] = min_coins

        return min_coins

    result = backtracking({}, amount)

    return -1 if result == float("inf") else result


if __name__ == "__main__":
    # coins = [int(x) for x in input().split()]
    coins = [1, 2, 5]
    # amount = int(input())
    amount = 11
    res = coin_change(coins, amount)
    print(res)

    list_all_coin_change(coins, amount)
