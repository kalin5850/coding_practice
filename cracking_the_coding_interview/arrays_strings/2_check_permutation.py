"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""
from collections import Counter


class Solution:
    def check_permutation1(self, string_a: str, string_b) -> bool:
        """
        sort two strings and compare two sorted strings. time complexity is
        O(nlogn) and space complexity is O(n)
        """
        sort = lambda string: sorted(string)
        sorted_string_a = sort(string=string_a)
        sorted_string_b = sort(string=string_b)

        return sorted_string_a == sorted_string_b

    def check_permutation2(self, string_a: str, string_b: str) -> bool:
        """
        use hashmap
        """
        return Counter(list(string_a)) == Counter(list(string_b))


if __name__ == "__main__":
    string_a = "abcd"
    string_b = "dcab"
    string_c = "aacd"

    # print(Solution().check_permutation1(string_a=string_a, string_b=string_b))
    # print(Solution().check_permutation1(string_a=string_a, string_b=string_c))
    print(Solution().check_permutation2(string_a=string_a, string_b=string_b))
    print(Solution().check_permutation2(string_a=string_a, string_b=string_c))
