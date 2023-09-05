class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        for idx, ch in enumerate(s):
            if idx < len(s) - 1 and roman_dict.get(ch) < roman_dict.get(
                s[idx + 1]
            ):
                result -= roman_dict[ch]
            else:
                result += roman_dict[ch]

        return result
