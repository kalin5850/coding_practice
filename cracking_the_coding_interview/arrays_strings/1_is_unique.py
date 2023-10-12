"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""


class Solution:
    def is_unique1(self, strings: str) -> bool:
        """
        brute force: time complexity is O(n^2) and space complexity is O(1)
        """
        for idx_x, ch in enumerate(strings):
            for idx_y in range(idx_x + 1, len(strings)):
                if ch == strings[idx_y]:
                    return False
        return True

    def is_unique2(self, strings: str) -> bool:
        """
        sort strings and compare character, time complexity is O(nlogn) and
        space complexity is O(n)
        """
        sort_strings = lambda strings: sorted(strings)
        sorted_strings = sort_strings(strings=strings)
        for idx_x in range(len(sorted_strings) - 1):
            idx_y = idx_x + 1
            if sorted_strings[idx_x] == sorted_strings[idx_y]:
                return False
        return True

    def is_unique3(self, strings: str) -> bool:
        """
        use data structure with hashmap, time complexity is O(n), and space
        complexity is O(n)
        """
        counter = {}
        for ch in strings:
            if ch not in counter:
                counter[ch] = 1
            else:
                return False
        return True


if __name__ == "__main__":
    string_a = "sfwefvtwcdsfsfgsfwe"
    string_b = "abcdef12345"

    # print(Solution().is_unique1(strings=string_a))
    # print(Solution().is_unique1(strings=string_b))
    # print(Solution().is_unique2(strings=string_a))
    # print(Solution().is_unique2(strings=string_b))
    print(Solution().is_unique3(strings=string_a))
    print(Solution().is_unique3(strings=string_b))
