class Solution:
    def isPalindrome(self, s: str) -> bool:
        palStr = ""
        for i in range(len(s)):
            if not ('a' <= s[i].lower() <= 'z') and not ('0' <= s[i] <= '9'):
                continue
            palStr += s[i].lower()

        revStr = palStr[::-1]

        if revStr == palStr:
            return True
        else:
            return False