import math
from typing import List


class Solution:
    """
    Brute force:
      scan each character for each word.
    """

    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs.pop()
        for word in strs:
            temp = ""
            for idx, ch in enumerate(word):
                if idx < len(prefix) and ch == prefix[idx]:
                    temp = temp + ch
                else:
                    break
            prefix = temp

        return prefix

    """
    Brute force:
    vertical scanning
    """

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs.pop()
        for idx, ch in enumerate(prefix):
            for j in range(len(strs)):
                if (idx == len(strs[j])) or ch != strs[j][idx]:
                    return prefix[:idx]
        return prefix

    """
    Binary search
    """

    def common_prefix(self, str1, str2):
        if str2 == "":
            return str1

        if str1 == "":
            return str2

        for idx, ch in enumerate(str1):
            if idx == len(str1) - 1 or idx + 1 == len(str2):
                return str1[: idx + 1]
            elif ch != str2[idx]:
                return str1[: idx + 1]
        return ""

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        if len(strs) > 1:
            low = 0
            middle = math.floor(len(strs) - low) // 2
            str1 = self.longestCommonPrefix3(strs[low:middle])
            str2 = self.longestCommonPrefix3(strs[middle : len(strs)])

        return self.common_prefix(strs[0], strs[1])


if __name__ == "__main__":
    strs = ["flower", "flow", "flight", "found", "flin", "fa", "f"]
    result = Solution().longestCommonPrefix3(strs=strs)
    print(result)
