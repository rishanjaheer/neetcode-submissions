class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = sorted(s, key=str.lower)
        sorted_t = sorted(t, key=str.lower) 

        for i in range(len(s)):
            if sorted_s[i] != sorted_t[i]:
                return False

        return True

