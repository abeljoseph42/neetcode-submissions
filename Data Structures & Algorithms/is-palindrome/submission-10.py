class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1


        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            
            while not s[r].isalnum()and l < r:
                r -= 1
            
            if s[l].lower() == s[r].lower():
                r -= 1
                l += 1
            else:
                return False
        
        return True
            
