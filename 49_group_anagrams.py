from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            sorted_string = "".join(sorted(list(string)))
            if sorted_string not in result:
                result[sorted_string] = [string]
            else:
                result[sorted_string].append(string)

        return list(result.values())
