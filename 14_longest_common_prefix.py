from typing import List


class Solution:
    """
    Brute force:
      scan each character for each word.
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
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

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs.pop()
        for idx, ch in enumerate(prefix):
            for j in range(len(strs)):
                if (idx == len(strs[j])) or ch != strs[j][idx]:
                    return prefix[:idx]
        return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    result = Solution().longestCommonPrefix(strs=strs)
    print(result)
