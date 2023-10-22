class Solution:
    def climb_stairs1(self, n: int) -> int:
        """
        Brute Force, the time complexity is O(n) and space complexity is O(n)
        """
        stairs_cache = [1, 1]
        for i in range(2, n + 1):
            p_i = stairs_cache[i - 1] + stairs_cache[i - 2]
            stairs_cache.insert(i, p_i)

        return stairs_cache[n]

    def climb_stairs2(self, n: int) -> int:
        """
        Recursive
        """
        stairs_cache = {0: 1, 1: 1}

        def recure_climb_stair(n):
            if n in stairs_cache:
                return stairs_cache.get(n)
            else:
                if n < 2:
                    return stairs_cache.get(n)
                else:
                    stairs_cache[n] = recure_climb_stair(
                        n - 1
                    ) + recure_climb_stair(n - 2)
                    return stairs_cache[n]

        return recure_climb_stair(n)


if __name__ == "__main__":
    n = 10
    print(Solution().climb_stairs2(n))
