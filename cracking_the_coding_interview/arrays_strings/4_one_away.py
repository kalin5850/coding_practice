class Solution:
    def one_away(self, string1: str, string2: str) -> str:
        """Brute force"""

        def one_edit_away_update(string1: str, string2: str) -> bool:
            "update"
            count = 0
            for i in range(len(string1)):
                if string1[i] != string2[i]:
                    count += 1
            return count == 1

        def one_edit_away_add(string1: str, string2: str) -> bool:
            "len(string1) > len(string2)"
            idx_i = 0
            idx_j = 0
            count = 0
            while True:
                if idx_i == len(string1) - 1:
                    return count == 1
                if string1[idx_i] == string2[idx_j]:
                    idx_i += 1
                    idx_j += 1
                if string1[idx_i] != string2[idx_j]:
                    idx_i += 1
                    count += 1

        if abs(len(string1) - len(string2)) == 0:
            return one_edit_away_update(string1, string2)
        if abs(len(string1) - len(string2)) == 1:
            if len(string1) > len(string2):
                return one_edit_away_add(string1, string2)
            else:
                return one_edit_away_add(string2, string1)


if __name__ == "__main__":
    input1 = ("pale", "ple")
    input2 = ("pasle", "pale")
    input3 = ("pale", "bale")
    input4 = ("pale", "bae")
    print(Solution().one_away(string1=input1[0], string2=input1[1]))
    print(Solution().one_away(string1=input2[0], string2=input2[1]))
    print(Solution().one_away(string1=input3[0], string2=input3[1]))
    print(Solution().one_away(string1=input4[0], string2=input4[1]))
