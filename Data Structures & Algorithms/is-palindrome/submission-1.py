class Solution:
    def isPalindrome(self, s: str) -> bool:
        standard = "".join(ch for ch in s if ch.isalnum()).lower()

        i = 0;
        j = len(standard) - 1;

        print(standard)
        

        while i < j:
            if not standard[i] == standard[j]:
                return False;
            i += 1;
            j -= 1;

        return True;
