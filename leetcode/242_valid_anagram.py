class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for ch in s:
            if ch not in dict_s:
                dict_s[ch] = 1
            else:
                dict_s[ch] = dict_s[ch] + 1
        for ch in t:
            if ch not in dict_t:
                dict_t[ch] = 1
            else:
                dict_t[ch] = dict_t[ch] + 1
        for key, value in dict_s.items():
            if key not in dict_t:
                return False
            elif key in dict_t and dict_s[key] != dict_t[key]:
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        s = "".join(sorted(list(s)))
        t = "".join(sorted(list(t)))

        return s == t
