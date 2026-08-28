class Solution:
    def isPalindrome(self, s: str) -> bool:
        palStr = ""
        for c in s:
            if c.isalnum():
                palStr += c.lower()
        
        return palStr == palStr[::-1]
